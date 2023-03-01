/* -*- c++ -*- */
/* 
 * Copyright 2023 David T Miller
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

#include "Tag_FrameASM_bb_impl.h"
#include <gnuradio/io_signature.h>

#include <gnuradio/math.h>
#include <volk/volk.h>
#include <boost/format.hpp>
#include <cstdio>
#include <iostream>
#include <stdexcept>

namespace gr {
namespace HighDataRate_Modem {

using input_type = char;
using output_type = char;
Tag_FrameASM_bb::sptr Tag_FrameASM_bb::make(int waveform, int ASM_length, int threshold)
{
    return gnuradio::make_block_sptr<Tag_FrameASM_bb_impl>(
        waveform, ASM_length, threshold);
}


/*
 * The private constructor
 */
Tag_FrameASM_bb_impl::Tag_FrameASM_bb_impl(int waveform, int ASM_length, int threshold)
    : gr::sync_block("Tag_FrameASM_bb",
                     gr::io_signature::make(
                         1 /* min inputs */, 1 /* max inputs */, sizeof(input_type)),
                     gr::io_signature::make(
                         1 /* min outputs */, 1 /*max outputs */, sizeof(output_type))),
      d_data_reg(0),
      d_mask(0),
      d_mask90(0),    
      d_mask48(0),
      d_mask4890(0), 
      d_waveform(waveform),
      d_len(ASM_length),
      d_threshold(threshold),   // type cast int to uint64_t
            s32{"00011010110011111111110000011101"}, // 32 bit CCSDS ASM
      s32rotate{"10001111011001010101011010000100"}, // 32 bit CCSDS ASM with phase rotation 90 degrees
            s48{"000111001001011100011010101001110011110100111110"}, //48 ASM-32 ASM convoluted fixed bits
      s48rotate{"100001101100000110001111111100011001010010010111"} //48 bit CCSDS ASM (rotation 90 deg)
{
      const std::string& access_code = s32;  // 32 bit CCSDS ASM 
      set_access_code(access_code);
      const std::string& access_code90 = s32rotate; //32 bit ASM code for 90 degree rotation
      set_access_code90(access_code90);
 
      const std::string& access_code48 = s48;  // 48 bit CCSDS ASM (32 bit convolved)
      set_access_code48(access_code48);
      const std::string& access_code4890 = s48rotate; //48 bit ASM code for 90 degree rotation
      set_access_code4890(access_code4890);

    std::stringstream str;
    str << name() << unique_id();
    d_me = pmt::string_to_symbol(str.str());
    d_key = pmt::string_to_symbol("TagASM");
}

/*
 * Our virtual destructor.
 */
Tag_FrameASM_bb_impl::~Tag_FrameASM_bb_impl() {}

    bool Tag_FrameASM_bb_impl::set_access_code(const std::string& access_code)
    {
        gr::thread::scoped_lock l(d_mutex_access_code);
        //d_len = 32; // # of bytes in string
        
        // set len bottom bits to 1.
        d_mask = ((~0ULL) >> (64-d_len));

        d_access_code = 0;
        for (unsigned i = 0; i < d_len; i++) 
        {
            d_access_code = (d_access_code << 1) | (access_code[i] & 1);
        }  

        GR_LOG_DEBUG(d_logger, boost::format("Access code: %llx") % d_access_code);
        GR_LOG_DEBUG(d_logger, boost::format("Mask: %llx") % d_mask);

        return true;
    }       

    bool Tag_FrameASM_bb_impl::set_access_code90(const std::string& access_code90)
    {
        gr::thread::scoped_lock l(d_mutex_access_code90);
                
        // set len bottom bits to 1.
        d_mask90 = ((~0ULL) >> (64-d_len));
        d_access_code90 = 0;
        for (unsigned i = 0; i < d_len; i++) 
        {
            d_access_code90 = (d_access_code90 << 1) | (access_code90[i] & 1);
        }  
       GR_LOG_DEBUG(d_logger, boost::format("Access code90: %llx") % d_access_code90);
       GR_LOG_DEBUG(d_logger, boost::format("Mask90: %llx") % d_mask90);
       return true;
    }  

    bool Tag_FrameASM_bb_impl::set_access_code48(const std::string& access_code48)
    {
        gr::thread::scoped_lock l(d_mutex_access_code48);
        //d_len = 32; // # of bytes in string
        
        // set len bottom bits to 1.
        d_mask48 = ((~0ULL) >> (64-d_len));

        d_access_code48 = 0;
        for (unsigned i = 0; i < d_len; i++) 
        {
            d_access_code48 = (d_access_code48 << 1) | (access_code48[i] & 1);
        }  

        GR_LOG_DEBUG(d_logger, boost::format("Access code: %llx") % d_access_code48);
        GR_LOG_DEBUG(d_logger, boost::format("Mask: %llx") % d_mask48);

        return true;
    }       

    bool Tag_FrameASM_bb_impl::set_access_code4890(const std::string& access_code4890)
    {
        gr::thread::scoped_lock l(d_mutex_access_code4890);
                
        // set len bottom bits to 1.
        d_mask4890 = ((~0ULL) >> (64-d_len));
        d_access_code4890 = 0;
        for (unsigned i = 0; i < d_len; i++) 
        {
            d_access_code4890 = (d_access_code4890 << 1) | (access_code4890[i] & 1);
        }  
       GR_LOG_DEBUG(d_logger, boost::format("Access code90: %llx") % d_access_code4890);
       GR_LOG_DEBUG(d_logger, boost::format("Mask90: %llx") % d_mask4890);
       return true;
    }

int Tag_FrameASM_bb_impl::work(int noutput_items,
                               gr_vector_const_void_star& input_items,
                               gr_vector_void_star& output_items)
{
    // gr::thread::scoped_lock l(d_mutex_access_code90);

      const char* in = (const char*)input_items[0];
      char* out = (char*)output_items[0];

    uint64_t abs_out_sample_cnt = nitems_written(0);

    //use int d_waveform = 1 if BPSK and d_waveform = 2 if QPSK
    switch(d_len + d_waveform) //{   /
    {   // bracket for "d_waveform" switch

      case 33:        //BPSK Waveform - 32 bits ASM
      for (int i = 0; i < noutput_items; i++) {
        out[i] = in[i];

        // compute hamming distance between desired access code and current data
        uint64_t wrong_bits = 0;
        uint64_t nwrong = d_threshold + 1;
        
        if (d_data_reg_bits < d_len) {
            d_data_reg_bits++;
        } else {
            wrong_bits = (d_data_reg ^ d_access_code) & d_mask;
            volk_64u_popcnt(&nwrong, wrong_bits);  // Volk kernal function - See Volk library
        }

        // shift in new data
        //d_data_reg = (d_data_reg << 1) | (gr::branchless_binary_slicer(in[i]) & 0x1);
        d_data_reg = (d_data_reg << 1) | ((in[i]) & 0x1);
        if ( (nwrong <= d_threshold) | (nwrong >= (d_len-d_threshold)) ) {  // logic for BPSK phases
            d_logger->debug("writing tag at sample {:d}", abs_out_sample_cnt + i);
            //GR_LOG_DEBUG(d_logger, boost::format("Bits wrong in ASM %llu") % (nwrong));
            add_item_tag(0,                      // stream ID
                         abs_out_sample_cnt + i, // sample
                         d_key,                  // frame info
                         pmt::from_long(nwrong), // data (number wrong or nwrong90)
                         d_me                    // block src id
            );
        }

      }  // END of FOR loop for i
            // GR_LOG_DEBUG(d_logger, boost::format("Case 1 %llu") % (d_waveform));
      break; //  break for CASE 1 32 bits ASM waveform BPSK

      case 49:        //BPSK Waveform - 48 bits convoluted ASM
      for (int i = 0; i < noutput_items; i++) {
        out[i] = in[i];

        // compute hamming distance between desired access code and current data
        uint64_t wrong_bits = 0;
        uint64_t nwrong = d_threshold + 1;
        
        if (d_data_reg_bits < d_len) {
            d_data_reg_bits++;
        } else {
            wrong_bits = (d_data_reg ^ d_access_code48) & d_mask48;
            volk_64u_popcnt(&nwrong, wrong_bits);  // Volk kernal function - See Volk library
        }

        // shift in new data
        //d_data_reg = (d_data_reg << 1) | (gr::branchless_binary_slicer(in[i]) & 0x1);
        d_data_reg = (d_data_reg << 1) | ((in[i]) & 0x1);
        if ( (nwrong <= d_threshold) | (nwrong >= (d_len-d_threshold)) ) {  // logic for BPSK phases
            d_logger->debug("writing tag at sample {:d}", abs_out_sample_cnt + i);
            //GR_LOG_DEBUG(d_logger, boost::format("Bits wrong in ASM %llu") % (nwrong));
            add_item_tag(0,                      // stream ID
                         abs_out_sample_cnt + i, // sample
                         d_key,                  // frame info
                         pmt::from_long(nwrong), // data (number wrong or nwrong90)
                         d_me                    // block src id
            );
        }

      }  // END of FOR loop for i
            // GR_LOG_DEBUG(d_logger, boost::format("Case 1 %llu") % (d_waveform));
      break; //  break for CASE 32 bits ASM waveform BPSK


      case 34:        //QPSK Waveform - 32 bits ASM
      for (int i = 0; i < noutput_items; i++) {
        out[i] = in[i];

        // compute hamming distance between desired access code and current data
        uint64_t wrong_bits = 0;
        uint64_t nwrong = d_threshold + 1;
        uint64_t wrong_bits90 = 0;
        uint64_t nwrong90 = d_threshold + 1;
        
        if (d_data_reg_bits < d_len) {
            d_data_reg_bits++;
        } else {
            wrong_bits = (d_data_reg ^ d_access_code) & d_mask;
            volk_64u_popcnt(&nwrong, wrong_bits);  // Volk kernal function - See Volk library
            wrong_bits90 = (d_data_reg ^ d_access_code90) & d_mask90;
            volk_64u_popcnt(&nwrong90, wrong_bits90);  // Volk kernal function - See Volk library
        }

        // shift in new data
        //d_data_reg = (d_data_reg << 1) | (gr::branchless_binary_slicer(in[i]) & 0x1);
        d_data_reg = (d_data_reg << 1) | ((in[i]) & 0x1);
        if ( (nwrong <= d_threshold) | (nwrong >= (d_len-d_threshold)) | (nwrong90 <= d_threshold) | (nwrong90 >= (d_len-d_threshold))  ) {  // logic for QPSK phases
            d_logger->debug("writing tag at sample {:d}", abs_out_sample_cnt + i);
            //GR_LOG_DEBUG(d_logger, boost::format("Bits wrong in ASM %llu") % (nwrong));
            add_item_tag(0,                      // stream ID
                         abs_out_sample_cnt + i, // sample
                         d_key,                  // frame info
                         pmt::from_long(nwrong), // data (number wrong or nwrong90)
                         d_me                    // block src id
            );
        }

      }  // END of FOR loop for i
      break;//  break for CASE 32 bits ASM waveform QPSK

      case 50:        //QPSK Waveform - 32 bits ASM
      for (int i = 0; i < noutput_items; i++) {
        out[i] = in[i];

        // compute hamming distance between desired access code and current data
        uint64_t wrong_bits = 0;
        uint64_t nwrong = d_threshold + 1;
        uint64_t wrong_bits90 = 0;
        uint64_t nwrong90 = d_threshold + 1;
                
        if (d_data_reg_bits < d_len) {
            d_data_reg_bits++;
        } else {
            wrong_bits = (d_data_reg ^ d_access_code48) & d_mask48;
            volk_64u_popcnt(&nwrong, wrong_bits);  // Volk kernal function - See Volk library
            wrong_bits90 = (d_data_reg ^ d_access_code4890) & d_mask4890;
            volk_64u_popcnt(&nwrong90, wrong_bits90);  // Volk kernal function - See Volk library
        }

        // shift in new data
        //d_data_reg = (d_data_reg << 1) | (gr::branchless_binary_slicer(in[i]) & 0x1);
        d_data_reg = (d_data_reg << 1) | ((in[i]) & 0x1);
       if ( (nwrong <= d_threshold) | (nwrong >= (d_len-d_threshold)) | (nwrong90 <= d_threshold) | (nwrong90 >= (d_len-d_threshold))  ) {  // logic for QPSK phases
            d_logger->debug("writing tag at sample {:d}", abs_out_sample_cnt + i);
            //GR_LOG_DEBUG(d_logger, boost::format("Bits wrong in ASM %llu") % (nwrong));
            add_item_tag(0,                      // stream ID
                         abs_out_sample_cnt + i, // sample
                         d_key,                  // frame info
                         pmt::from_long(nwrong), // data (number wrong or nwrong90)
                         d_me                    // block src id
            );
        }

      }  // END of FOR loop for i
            // GR_LOG_DEBUG(d_logger, boost::format("Case 1 %llu") % (d_waveform));
      break; //  //  break for CASE 48 bits convoluted ASM and waveform QPSK 

    } // END of SWITCH function for BPSK and QPSK cases

    return noutput_items;
}

} /* namespace HighDataRate_Modem */
} /* namespace gr */
