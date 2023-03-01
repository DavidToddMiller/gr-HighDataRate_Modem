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

#include "Frame_Extract_bb_impl.h"
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
Frame_Extract_bb::sptr
Frame_Extract_bb::make(int frame_length, int buffer_length, int ASM_length)
{
    return gnuradio::make_block_sptr<Frame_Extract_bb_impl>(
        frame_length, buffer_length, ASM_length);
}


/*
 * The private constructor
 */
Frame_Extract_bb_impl::Frame_Extract_bb_impl(int frame_length,
                                             int buffer_length,
                                             int ASM_length)
    : gr::block("Frame_Extract_bb",
                gr::io_signature::make(
                    1 /* min inputs */, 1 /* max inputs */, sizeof(input_type)),
                gr::io_signature::make(
                    1 /* min outputs */, 1 /*max outputs */, sizeof(output_type))),
      d_frame_length(frame_length), // 
      d_buffer_length(buffer_length), // 30000 items-samples for 15 Mbps and 15000 for low rate CCSDS
      d_ASM_length(ASM_length)
    {
        //set_tag_propagation_policy(TPP_DONT); 
        set_output_multiple(d_buffer_length); 
        n_dropped_times = 0;
    }


/*
 * Our virtual destructor.
 */
Frame_Extract_bb_impl::~Frame_Extract_bb_impl() {}

void Frame_Extract_bb_impl::forecast(int noutput_items,
                                     gr_vector_int& ninput_items_required)
{
 ninput_items_required[0] = noutput_items;
}

int Frame_Extract_bb_impl::general_work(int noutput_items,
                                        gr_vector_int& ninput_items,
                                        gr_vector_const_void_star& input_items,
                                        gr_vector_void_star& output_items)
    {
      //Remove tags from frames not "d_frame_length" bits in length that come from chunk chain discontinuities or ccsds flowgraph frame length
      uint64_t n_digested = 0; // set max for circular buffer to use
      uint64_t n_produced = 0;  // set max for circular buffer to use

      const char* in = (const char*)input_items[0];
      char* out = (char*)output_items[0];

      std::vector<tag_t> tags;
      get_tags_in_range(tags, 0, nitems_read(0) + d_ASM_length, nitems_read(0) + noutput_items);
      GR_LOG_DEBUG(d_logger, boost::format("writing tag size %llu") % (tags.size()));

      if (int(tags.size())<3)  // STOP and move on to next 30000 bits in next WORK Call
      {
      n_digested = d_buffer_length/3;  // 10000 for hdr 15.0 Mbps flowgraph but only 5000 for CCSDS low rate flowgraph
      n_produced = d_buffer_length/3;  // 10000 for hdr 15.0 Mbps flowgraph but only 5000 for CCSDS low rate flowgraph
      }

      if (int(tags.size())>2)  // Extract frames in WORK Call via ASM and maintain ASM
      {
      n_digested = tags[0].offset-nitems_read(0)-(d_ASM_length);//start point: function of ASM length
      int tags_length = int(tags.size()-2);  // -2 so no partial frames in WORK call extracted

      for(int i=0; i<tags_length; i++) {
         //int offset = int(tags[i].offset);
         int offset_start = int(tags[i].offset);
         int offset_end = int(tags[i+1].offset);
         int delta = offset_end - offset_start;
      
         GR_LOG_DEBUG(d_logger, boost::format("DELTA %llu") % (delta));

         if (delta == d_frame_length)  //4192 includes ASM for 15 Mbps flowgraph. For CCSDS flowgraphs with Reed-Solomon, frame length will be 2072 bits (255 bytes * 8 + 32 bit ASM)
         {
             memcpy((void*)(out+n_produced), (const void*)(in+n_digested), d_frame_length); // char item size
             n_digested += delta;  //15 Mbps 4192 or CCSDS 2072 or convolution CCSDS 4144; 
             n_produced += delta; //15 Mbps 4192 or CCSDS 2072 or convolution CCSDS 4144; 
         }  
         if (delta != d_frame_length)
         {
             // Drop Duplicate chunk chain discontinuity bits for 15 Mbps case of frame stitching
             n_digested += delta;
         }
         if (delta < 90)  // code here for 15 Mbps case of frame stitching
         {
                i = i + 1;
                n_digested += d_frame_length;
                n_dropped_times = n_dropped_times + 1;
         }  

      }  // End of FOR loop

      }   // End of IF Statement

      GR_LOG_DEBUG(d_logger, boost::format("DROPPED incrementer value %llu") % (n_dropped_times));

      consume_each (n_digested);   //tell scheduler runtime the amount of input items consum     
      return n_produced;    //tell scheduler runtime output items
    }

} /* namespace HighDataRate_Modem */
} /* namespace gr */
