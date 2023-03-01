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

#include "Resolve_Phase_impl.h"
#include <gnuradio/io_signature.h>



namespace gr {
namespace HighDataRate_Modem {

using input_type = char;
using output_type = char;
Resolve_Phase::sptr
Resolve_Phase::make(int waveform, int frame_length, int buffer_length, int threshold)
{
    return gnuradio::make_block_sptr<Resolve_Phase_impl>(
        waveform, frame_length, buffer_length, threshold);
}


/*
 * The private constructor
 */
Resolve_Phase_impl::Resolve_Phase_impl(int waveform,
                                       int frame_length,
                                       int buffer_length,
                                       int threshold)
    : gr::block("Resolve_Phase",
                gr::io_signature::make(
                    1 /* min inputs */, 1 /* max inputs */, sizeof(input_type)),
                gr::io_signature::make(
                    1 /* min outputs */, 1 /*max outputs */, sizeof(output_type))),
       // CCSDS 32 Bit ASM Resolution BPSK and QPSK
      s{0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1},
      s90{1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0},
      d_waveform(waveform),
      d_frame_length(frame_length), // 
      d_buffer_length(buffer_length), // 30000 items-samples for 15 Mbps and 15000 for low rate CCSDS
      d_threshold(threshold)
    {
        set_tag_propagation_policy(TPP_DONT); 
        set_output_multiple(d_buffer_length); 
    }

/*
 * Our virtual destructor.
 */
Resolve_Phase_impl::~Resolve_Phase_impl() {}

void Resolve_Phase_impl::forecast(int noutput_items, gr_vector_int& ninput_items_required)
{
 ninput_items_required[0] = noutput_items;
}

int Resolve_Phase_impl::general_work(int noutput_items,
                                     gr_vector_int& ninput_items,
                                     gr_vector_const_void_star& input_items,
                                     gr_vector_void_star& output_items)
    {
      uint64_t n_digested = 13*d_frame_length; // 13 frames for frame length 2072 
      uint64_t n_produced = 13*d_frame_length; // 13 frames for frame length 2072 
      int d_phase = 0;
      int d_compare = 0;
      int d_compare90 = 0;

      uint8_t* out = (uint8_t*)output_items[0];
      const uint8_t* in = (const uint8_t*)input_items[0];

    switch(d_waveform) //{   //use int d_waveform = 1 if BPSK and d_waveform = 2 if QPSK
    {
      case 1:        //BPSK Phases to Resolve CASE 1 option: BPSK
      // Do 13 frames per WORK call for now
      for(int i=0; i<13; i++) {
           
           // ASM determination of phase first as 0 deg or 180 deg for BPSK
           for(int j=0; j<32; j++) {
              if(in[j+i*d_frame_length] == s[j]){d_compare += 1;}
              GR_LOG_DEBUG(d_logger, boost::format("d_compare %llu") % (d_compare));
           } // End of j FOR loop

           if(d_compare >= 32-d_threshold) // threshold set to 1 allowed error
           {    
           d_phase = 0;  //0 degrees lock
           GR_LOG_DEBUG(d_logger, boost::format("Resolve Block PHASE in DEGREES %llu") % (d_phase));
           }

           if(d_compare <= d_threshold)   //threshold set to 1 allowed error
           {    
           d_phase = 180;  //180 degrees lock so need to flip bits
           GR_LOG_DEBUG(d_logger, boost::format("Resolve Block PHASE in DEGREES %llu") % (d_phase));
           }

           //GR_LOG_DEBUG(d_logger, boost::format("Resolve Block PHASE in DEGREES %llu") % (d_phase));
           d_compare = 0;  //reset d_compare for each run through 13 ASMs per WORK call

           for(int m=0; m<d_frame_length; m++) {      // rotate frame and its ASM and output it
           switch(d_phase) 
           {   // bracket for "d_phase" switch
           case 0:        //for 45 degree phase, no rotation and so no flip bits, just output it
                out[m+i*d_frame_length] = in[m+i*d_frame_length];  
                // GR_LOG_DEBUG(d_logger, boost::format("Dont flip code  ?????????? %llu") % (d_waveform));
                break; 

           case 180:        //for 225 deg, 180 deg rotation - flip all bits
                out[m+i*d_frame_length] = in[m+i*d_frame_length] ^ 0x01; //mask 0000 0001 is 0x01
                // GR_LOG_DEBUG(d_logger, boost::format("FLIP Bit code  ?????????? %llu") % (d_waveform));
                break;
           } // end of SWITCH function for d_phase 

           if (d_phase != 0)  
           {
              if (d_phase != 180)  
              {
              out[m+i*d_frame_length] = in[m+i*d_frame_length];  
              GR_LOG_DEBUG(d_logger, boost::format("Rotate Phase Undetermined ??????? %llu") % (d_phase));
              }
           }

           } // End of m FOR loop for each frame in Case 1 BPSK
    
      } // CASE 1, BPSK: End of i "FOR" loop in Case 1 for 13 frames and end of Case 1 BPSK code lines
      break;

 
      case 2:        //QPSK Phases to Resolve - CASE 2 option: QPSK
      // Do 13 frames per WORK call for now
      for(int i=0; i<13; i++) {
           
           // ASM determination of phase first as 45 deg, 135 deg, 225 deg, 315 deg for QPSK
           for(int j=0; j<32; j++) {
              if(in[j+i*d_frame_length] == s[j]){d_compare += 1;}
              if(in[j+i*d_frame_length] == s90[j]){d_compare90 += 1;}
              // GR_LOG_DEBUG(d_logger, boost::format("d_compare %llu") % (d_compare));
           } // End of j FOR loop

           if(d_compare >= 32-d_threshold)  //threshold set to 1 error
           {    
           d_phase = 45;  //45 degrees lock
           GR_LOG_DEBUG(d_logger, boost::format("Resolve Block PHASE in DEGREES %llu") % (d_phase));
           }

           if(d_compare <= d_threshold)  //threshold set to 1 error
           {    
           d_phase = 225;  //225 degrees lock so need to flip bits
           GR_LOG_DEBUG(d_logger, boost::format("Resolve Block PHASE in DEGREES %llu") % (d_phase));
           }

           if(d_compare90 >= 32-d_threshold)  //threshold set to 1 error
           {    
           d_phase = 135;  //135 degrees lock
           GR_LOG_DEBUG(d_logger, boost::format("Resolve Block PHASE in DEGREES %llu") % (d_phase));
           }

           if(d_compare90 <= d_threshold)  //threshold set to 1 error
           {    
           d_phase = 315;  //315 degrees lock so need to flip bits
           GR_LOG_DEBUG(d_logger, boost::format("Resolve Block PHASE in DEGREES %llu") % (d_phase));
           }

           //GR_LOG_DEBUG(d_logger, boost::format("Resolve Block PHASE in DEGREES %llu") % (d_phase));
           d_compare = 0;  //reset d_compare for each run through 13 ASMs per WORK call
           d_compare90 = 0;  //reset d_compare for each run through 13 ASMs per WORK call

           for(int m=0; m<d_frame_length; m++) {      // rotate frame and its ASM and output it
           switch(d_phase) //{   //use int d_waveform = 1 if BPSK and d_waveform = 2 if QPSK
           {   // bracket for "d_phase" switch
           case 45:        //for 45 degree phase, no rotation and so no flip bits, just output it
                out[m+i*d_frame_length] = in[m+i*d_frame_length];  
                out[m+1+i*d_frame_length] = in[m+1+i*d_frame_length];  
                m += 1;                
                break; 

           case 225:        //for 225 deg, 180 deg rotation - flip all bits
                out[m+i*d_frame_length] = in[m+i*d_frame_length] ^ 0x01; //mask 0000 0001 is 0x01
                out[m+1+i*d_frame_length] = in[m+1+i*d_frame_length] ^ 0x01;                 
                m += 1;    
                break;

           case 135:     //for 135 deg, 90 deg rotation so exactly half bits will be flipped only 
                if(in[m+i*d_frame_length] == 1 && in[m+1+i*d_frame_length] == 1)
                {
                     out[m+i*d_frame_length] = 1;
                     out[m+1+i*d_frame_length] = 0;
                }
                else if(in[m+i*d_frame_length] == 0 && in[m+1+i*d_frame_length] == 1)
                {
                     out[m+i*d_frame_length] = 1;
                     out[m+1+i*d_frame_length] = 1;
                }
                else if(in[m+i*d_frame_length] == 0 && in[m+1+i*d_frame_length] == 0)
                {
                     out[m+i*d_frame_length] = 0;
                     out[m+1+i*d_frame_length] = 1;
                }
                else // must be (in[m+i*frame_length] == 1 && in[m+1+i*frame_length] == 0)
                {
                     out[m+i*d_frame_length] = 0;
                     out[m+1+i*d_frame_length] = 0;
                }
                m += 1;    
                break;

                case 315:     //for 315 deg, 270 deg rotation so exactly half bits will be flipped only 
                if(in[m+i*d_frame_length] == 1 && in[m+1+i*d_frame_length] == 1)
                {
                     out[m+i*d_frame_length] = 0;
                     out[m+1+i*d_frame_length] = 1;
                }
                else if(in[m+i*d_frame_length] == 0 && in[m+1+i*d_frame_length] == 1)
                {
                     out[m+i*d_frame_length] = 0;
                     out[m+1+i*d_frame_length] = 0;
                }
                else if(in[m+i*d_frame_length] == 0 && in[m+1+i*d_frame_length] == 0)
                {
                     out[m+i*d_frame_length] = 1;
                     out[m+1+i*d_frame_length] = 0;
                }
                else  // must be (in[m+i*4192] == 1 && in[m+1+i*4192] == 0)
                {
                     out[m+i*d_frame_length] = 1;
                     out[m+1+i*d_frame_length] = 1;
                }
                m += 1;
                break;

            } // end of SWITCH function for d_phase
            } // End of m FOR loop for each frame
    
      } // CASE 2, QPSK: End of i FOR loop in Case 2 for 13 frames and End of QPSK Case 2
      break;
    }                  // SWITCH end for "Case 1" (BPSK) or "Case 2" (QPSK)
 
      consume_each (n_digested);   //tell scheduler runtime the amount of input items consum     
      return n_produced;    //tell scheduler runtime output items
    }    // end of WORK function 

} /* namespace HighDataRate_Modem */
} /* namespace gr */
