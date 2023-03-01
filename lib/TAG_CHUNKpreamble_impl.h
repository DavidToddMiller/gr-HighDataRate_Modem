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

#ifndef INCLUDED_HIGHDATARATE_MODEM_TAG_CHUNKPREAMBLE_IMPL_H
#define INCLUDED_HIGHDATARATE_MODEM_TAG_CHUNKPREAMBLE_IMPL_H

#include <HighDataRate_Modem/TAG_CHUNKpreamble.h>

namespace gr {
namespace HighDataRate_Modem {

class TAG_CHUNKpreamble_impl : public TAG_CHUNKpreamble
{
private:
       unsigned long long d_access_code; // access code to locate start of chunk
                                      //   access code is left justified in the word
       unsigned long long d_access_code90; // access code to locate start of chunk
                                      //   access code is left justified in the word
       unsigned long long d_data_reg;    // used to look for access_code of preamble
       unsigned int d_data_reg_bits = 0; // used to make sure we've seen the whole code
       unsigned long long d_mask;        // masks access_code bits (top N bits are set where
                                      //   N is the number of bits in the access code)
       unsigned long long d_mask90;        // masks access_code bits (top N bits are set where
                                      //   N is the number of bits in the access code)
       unsigned int d_threshold;         // how many bits may be wrong in sync preamble
       unsigned int d_len;               // the length of the access code of chunk preamble
       const std::string s;
       const std::string s90;

       pmt::pmt_t d_key, d_me; // d_key is the tag name, d_me is the block name + unique ID
       gr::thread::mutex d_mutex_access_code;

       const std::string* access_code;

public:
    TAG_CHUNKpreamble_impl();
    ~TAG_CHUNKpreamble_impl();

        bool set_access_code(const std::string& access_code);
        bool set_access_code90(const std::string& access_code90);    

    // Where all the action really happens
    int work(int noutput_items,
             gr_vector_const_void_star& input_items,
             gr_vector_void_star& output_items);
};

} // namespace HighDataRate_Modem
} // namespace gr

#endif /* INCLUDED_HIGHDATARATE_MODEM_TAG_CHUNKPREAMBLE_IMPL_H */
