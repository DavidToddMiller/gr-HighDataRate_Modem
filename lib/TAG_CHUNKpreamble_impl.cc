/* -*- c++ -*- */
/* 
 * Copyright 2022 David T Miller
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *  * 
 */

#include "TAG_CHUNKpreamble_impl.h"
#include <gnuradio/io_signature.h>

#include <volk/volk.h>
#include <boost/format.hpp>
#include <cstdio>
#include <iostream>
#include <stdexcept>

namespace gr {
namespace HighDataRate_Modem {

using input_type = char;
using output_type = char;
TAG_CHUNKpreamble::sptr TAG_CHUNKpreamble::make()
{
    return gnuradio::make_block_sptr<TAG_CHUNKpreamble_impl>();
}

/*
 * The private constructor
 */
TAG_CHUNKpreamble_impl::TAG_CHUNKpreamble_impl()
    : gr::sync_block("TAG_CHUNKpreamble",
                     gr::io_signature::make(
                         1 /* min inputs */, 1 /* max inputs */, sizeof(input_type)),
                     gr::io_signature::make(
                         1 /* min outputs */, 1 /*max outputs */, sizeof(output_type))),
        d_data_reg(0),
        d_mask(0),
        d_mask90(0),
        d_threshold(0),
        d_len(64),
        s{"1010110011011101101001001110001011110010100011000010000011111100"},  // Chunk Preamble flipped to check also
        s90{"1111011001000100111100100111101101011011111001101011101001010110"}  //Chunk Preamble 90 deg rotation check

    {
      const std::string& access_code = s;  // access_code via & is a reference to original object s
      set_access_code(access_code);

      const std::string& access_code90 = s90; //90 deg rotation access_code via a reference to original object s90
      set_access_code90(access_code90);

      std::stringstream str;
      str << name() << unique_id();
      d_me = pmt::string_to_symbol(str.str());
      d_key = pmt::string_to_symbol("TagASM1");
    }

/*
 * Our virtual destructor.
 */
TAG_CHUNKpreamble_impl::~TAG_CHUNKpreamble_impl() {}

    bool TAG_CHUNKpreamble_impl::set_access_code(const std::string& access_code)
    {
        gr::thread::scoped_lock l(d_mutex_access_code);
        d_len = 64; // # of bytes in string
        // d_len = 64; // # of bytes in string
        
        // set len bottom bits to 1.
        d_mask = ((~0ULL) >> (64 - 64));;
        //d_mask = ((~0ULL) >> (0));

        d_access_code = 0;
        for (unsigned i = 0; i < d_len; i++) 
        {
            d_access_code = (d_access_code << 1) | (access_code[i] & 1);
        }  

       GR_LOG_DEBUG(d_logger, boost::format("Access code: %llx") % d_access_code);
       GR_LOG_DEBUG(d_logger, boost::format("Mask: %llx") % d_mask);

       return true;
    }  

    bool TAG_CHUNKpreamble_impl::set_access_code90(const std::string& access_code90)
    {
        // gr::thread::scoped_lock l(d_mutex_access_code90);
                
        // set len bottom bits to 1.
        d_mask90 = ((~0ULL) >> (0));
        d_access_code90 = 0;
        for (unsigned i = 0; i < 64; i++) 
        {
            d_access_code90 = (d_access_code90 << 1) | (access_code90[i] & 1);
        }  
       GR_LOG_DEBUG(d_logger, boost::format("Access code90: %llx") % d_access_code90);
       GR_LOG_DEBUG(d_logger, boost::format("Mask90: %llx") % d_mask90);
       return true;
    }  

int TAG_CHUNKpreamble_impl::work(int noutput_items,
                                 gr_vector_const_void_star& input_items,
                                 gr_vector_void_star& output_items)

    {
      gr::thread::scoped_lock l(d_mutex_access_code);

      const unsigned char* in = (const unsigned char*)input_items[0];
      unsigned char* out = (unsigned char*)output_items[0];

      uint64_t abs_out_sample_cnt = nitems_written(0);

      // Phase Ambiguity resolution for BPSK based on ASM pattern
      for (int i = 0; i < noutput_items; i++) {
        out[i] = in[i];

        // compute hamming distance between desired access code and current data
        uint64_t wrong_bits = 0;
        uint64_t nwrong = d_threshold + 1;

        if (d_data_reg_bits < 64) {
           d_data_reg_bits++;
           //d_data_reg_bits++;  //increment in 2 steps now
        } 
        else
        {
           wrong_bits = (d_data_reg ^ d_access_code) & d_mask90;
           volk_64u_popcnt(&nwrong, wrong_bits);
        }      //  end of IF statement for  if (d_data_reg_bits < 64) {

        if (nwrong == 32) {
           wrong_bits = (d_data_reg ^ d_access_code90) & d_mask;
           volk_64u_popcnt(&nwrong, wrong_bits);           
        } 

        // shift in new data
        d_data_reg = (d_data_reg << 1) | (in[i] & 0x1);

        if (nwrong == 0 || nwrong == 64) {
            GR_LOG_DEBUG(d_logger,
                         boost::format("writing tag at sample %llu") %
                             (abs_out_sample_cnt + i));
            add_item_tag(0,                      // stream ID
                         abs_out_sample_cnt + i, // sample
                         d_key,                  // frame info
                         pmt::from_long(nwrong), // data (number wrong)
                         d_me                    // block src id
            );  // add tag function endibg
        }
        // 
      }   // end of  FOR  I loop

      return noutput_items;
    }

} /* namespace HighDataRate_Modem */
} /* namespace gr */
