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

#include "Chunk_ExtractBPSK_impl.h"
#include <gnuradio/io_signature.h>

namespace gr {
namespace HighDataRate_Modem {

using input_type = char;
using output_type = char;
Chunk_ExtractBPSK::sptr Chunk_ExtractBPSK::make()
{
    return gnuradio::make_block_sptr<Chunk_ExtractBPSK_impl>();
}

/*
 * The private constructor
 */
Chunk_ExtractBPSK_impl::Chunk_ExtractBPSK_impl()
    : gr::block("Chunk_ExtractBPSK",
                gr::io_signature::make(
                    1 /* min inputs */, 1 /* max inputs */, sizeof(input_type)),
                gr::io_signature::make(
                    1 /* min outputs */, 1 /*max outputs */, sizeof(output_type)))
    {
        set_tag_propagation_policy(TPP_DONT); 
        set_output_multiple(84000); 
    }

/*
 * Our virtual destructor.
 */
Chunk_ExtractBPSK_impl::~Chunk_ExtractBPSK_impl() {}

void Chunk_ExtractBPSK_impl::forecast(int noutput_items,
                                      gr_vector_int& ninput_items_required)
{
 ninput_items_required[0] = noutput_items;
}

int Chunk_ExtractBPSK_impl::general_work(int noutput_items,
                                         gr_vector_int& ninput_items,
                                         gr_vector_const_void_star& input_items,
                                         gr_vector_void_star& output_items)
    {
      //BPSK Chunk Extract - One chunk per WORK Call
      uint64_t n_digested = 0; // 
      uint64_t n_produced = 0;

      uint8_t* out = (uint8_t*)output_items[0];
      const uint8_t* in = (const uint8_t*)input_items[0];

      std::vector<tag_t> tags;
      get_tags_in_range(tags, 0, nitems_read(0), nitems_read(0) + noutput_items);
      GR_LOG_DEBUG(d_logger, boost::format("writing tag size %llu") % (tags.size()));
      GR_LOG_DEBUG(d_logger, boost::format("N_items_read 0 value    %llu") % (nitems_read(0)));
      GR_LOG_DEBUG(d_logger, boost::format("N_items_output items value    %llu") % (noutput_items));

      if (int(tags.size())<2)  // STOP and move on to next 38000 bits via new WORK call
      {
      n_digested = 38000;
      }

      if (int(tags.size())>1)  //
      {
      n_digested = tags[0].offset-nitems_read(0);  //

      for(int i=0; i<1; i++) {
           memcpy((void*)(out+n_produced), (const void*)(in+n_digested), 41510); //
           n_digested += 41510;  //Extrack Chunk after preamble
           n_produced += 41510; //Extract Chunk after preamble
      }  // End of FOR loop

      }  // End of IF statement

      consume_each (n_digested);   //tell scheduler runtime the amount of input items consumed     
      return n_produced;    //tell scheduler runtime output items produced
    }

} /* namespace HighDataRate_Modem */
} /* namespace gr */
