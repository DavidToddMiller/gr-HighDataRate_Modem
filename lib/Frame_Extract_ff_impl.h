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

#ifndef INCLUDED_HIGHDATARATE_MODEM_FRAME_EXTRACT_FF_IMPL_H
#define INCLUDED_HIGHDATARATE_MODEM_FRAME_EXTRACT_FF_IMPL_H

#include <HighDataRate_Modem/Frame_Extract_ff.h>

namespace gr {
namespace HighDataRate_Modem {

class Frame_Extract_ff_impl : public Frame_Extract_ff
{
private:
    // Nothing to declare in this block.
    int d_frame_length;
    int d_buffer_length;
    int d_ASM_length;
    int n_dropped_times;


public:
    Frame_Extract_ff_impl(int frame_length, int buffer_length, int ASM_length);
    ~Frame_Extract_ff_impl();

    // Where all the action really happens
    void forecast(int noutput_items, gr_vector_int& ninput_items_required);

    int general_work(int noutput_items,
                     gr_vector_int& ninput_items,
                     gr_vector_const_void_star& input_items,
                     gr_vector_void_star& output_items);
};

} // namespace HighDataRate_Modem
} // namespace gr

#endif /* INCLUDED_HIGHDATARATE_MODEM_FRAME_EXTRACT_FF_IMPL_H */
