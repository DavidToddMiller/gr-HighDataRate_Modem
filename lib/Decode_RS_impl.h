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

#ifndef INCLUDED_HIGHDATARATE_MODEM_DECODE_RS_IMPL_H
#define INCLUDED_HIGHDATARATE_MODEM_DECODE_RS_IMPL_H

#include <HighDataRate_Modem/Decode_RS.h>

namespace gr {
namespace HighDataRate_Modem {

class Decode_RS_impl : public Decode_RS
{
private:
    // Nothing to declare in this block.
    bool d_dual_basis;
    int d_pad;
    int d_interleave;

    unsigned char* d_data;
    //std::function<void(unsigned char*)> d_encode_rs;
    int decode(const unsigned char* in, unsigned char* out);


public:
    Decode_RS_impl(bool dual_basis, int pad, int interleave);
    ~Decode_RS_impl() override;

    // Where all the action really happens
    void forecast(int noutput_items, gr_vector_int& ninput_items_required) override;

    int general_work(int noutput_items,
                     gr_vector_int& ninput_items,
                     gr_vector_const_void_star& input_items,
                     gr_vector_void_star& output_items);
};

} // namespace HighDataRate_Modem
} // namespace gr

#endif /* INCLUDED_HIGHDATARATE_MODEM_DECODE_RS_IMPL_H */
