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

#ifndef INCLUDED_HIGHDATARATE_MODEM_TAG_FRAMEASM_FF_IMPL_H
#define INCLUDED_HIGHDATARATE_MODEM_TAG_FRAMEASM_FF_IMPL_H

#include <HighDataRate_Modem/Tag_FrameASM_ff.h>

namespace gr {
namespace HighDataRate_Modem {

class Tag_FrameASM_ff_impl : public Tag_FrameASM_ff
{
private:
    // Nothing to declare in this block.
       unsigned long long d_access_code; // access code to locate start of Frame 
                                      //   access code is left justified in the word
       unsigned long long d_access_code90; // access code to locate start of Frame
                                      //   access code is left justified in the word

       //48 bit convoluted ASM d_access codes
       unsigned long long d_access_code48; 
       unsigned long long d_access_code4890; 
                                     


       unsigned long long d_data_reg;    // used to look for access_code
       unsigned int d_data_reg_bits = 0; // used to make sure we've seen the whole code
       unsigned long long d_mask;        // masks access_code bits (top N bits are set where
                                      //   N is the number of bits in the access code)
       unsigned long long d_mask90;        // masks access_code bits (top N bits are set where
                                      //   N is the number of bits in the access code)
       //48 bit masks
       unsigned long long d_mask48;
       unsigned long long d_mask4890;

       unsigned int d_waveform;    
       unsigned int d_len;               // the length of the ASM
       uint64_t d_threshold;         // how many bits may be wrong in sync ASM

       const std::string s32;
       const std::string s32rotate;
       const std::string s48;
       const std::string s48rotate;       

       pmt::pmt_t d_key, d_me; // d_key is the tag name, d_me is the block name + unique ID
       gr::thread::mutex d_mutex_access_code;
       gr::thread::mutex d_mutex_access_code90;
       gr::thread::mutex d_mutex_access_code48;
       gr::thread::mutex d_mutex_access_code4890;

       const std::string* access_code;  
       const std::string* access_code90; 
       const std::string* access_code48;  
       const std::string* access_code4890;  


public:
    Tag_FrameASM_ff_impl(int waveform, int ASM_length, int threshold);
    ~Tag_FrameASM_ff_impl();

    // Where all the action really happens
    int work(int noutput_items,
             gr_vector_const_void_star& input_items,
             gr_vector_void_star& output_items);

       bool set_access_code(const std::string& access_code);
       bool set_access_code90(const std::string& access_code90);
       bool set_access_code48(const std::string& access_code48);
       bool set_access_code4890(const std::string& access_code4890);    
       
};

} // namespace HighDataRate_Modem
} // namespace gr

#endif /* INCLUDED_HIGHDATARATE_MODEM_TAG_FRAMEASM_FF_IMPL_H */
