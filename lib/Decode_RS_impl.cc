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

#include "Decode_RS_impl.h"
#include <gnuradio/io_signature.h>

#include <algorithm>
#include <exception>

extern "C" {
#include "libfec/fec.h"
}

#include "rs.h"

namespace gr {
namespace HighDataRate_Modem {

using input_type = char;
using output_type = char;
Decode_RS::sptr Decode_RS::make(bool dual_basis, int pad, int interleave)
{
    return gnuradio::make_block_sptr<Decode_RS_impl>(dual_basis, pad, interleave);
}


/*
 * The private constructor
 */
Decode_RS_impl::Decode_RS_impl(bool dual_basis, int pad, int interleave)
    : gr::block("Decode_RS",
                gr::io_signature::make(
                    1 /* min inputs */, 1 /* max inputs */, sizeof(input_type) * (255 - pad)),
                gr::io_signature::make(
                    1 /* min outputs */, 1 /*max outputs */, sizeof(output_type) * (223 - pad))),
      d_dual_basis(dual_basis),
      d_pad(pad),
      d_interleave(interleave)  // future feature/option
{
}

/*
 * Our virtual destructor.
 */
Decode_RS_impl::~Decode_RS_impl() {}

void Decode_RS_impl::forecast(int noutput_items, gr_vector_int& ninput_items_required)
{
  ninput_items_required[0] = noutput_items;
}

int Decode_RS_impl::decode(const unsigned char* in, unsigned char* out)
{
    unsigned char data[255-d_pad];

    // Shortened Reed-Solomon: prepend zero bytes to message "d_pad" (discarded after encoding)
    //std::memset(d_data, 0, d_s);
    // This is the number of data bytes we need from the input stream.
    //int shortened_k = d_k - d_s;
    int ncorrections;
    std::memcpy(data, in, 255-d_pad); // if d_pad = 3, then (252,220) frame size

    // Copy input message to output then append Reed-Solomon bits
    //std::memcpy(out, in, 223);
    //encode_rs_char(d_rs, d_data, &out[shortened_k]);
    if (d_dual_basis)
    {
        ncorrections = decode_rs_ccsds(data, NULL, 0, d_pad);  // "Dual Basis"
    }
    else
    {
        ncorrections = decode_rs_8(data, NULL, 0, d_pad);  // else "Conventional"
    }

    //ncorrections = decode_rs_8(data, NULL, 0, d_interleave);
    //d_encode_rs = [](unsigned char* data) {  };
    std::memcpy(out, data, 223-d_pad);
    return ncorrections;
}



int Decode_RS_impl::general_work(int noutput_items,
                                 gr_vector_int& ninput_items,
                                 gr_vector_const_void_star& input_items,
                                 gr_vector_void_star& output_items)
{
    const unsigned char* in = (const unsigned char*)input_items[0];
    unsigned char* out = (unsigned char*)output_items[0];
    int j = 0;
    int k = 0;

    for (int i = 0; i < (noutput_items); i++) {
        int nerrors_corrected = decode(in + j,out + k);

        GR_LOG_DEBUG(d_logger, boost::format("Reed-Solomon decode corrected bytes %llu") % (nerrors_corrected));

        j += 255-(d_pad);
        k += 223-(d_pad);
    }

    consume_each(noutput_items);

    // Tell runtime system how many output items we produced.
    return noutput_items;
}

} /* namespace HighDataRate_Modem */
} /* namespace gr */
