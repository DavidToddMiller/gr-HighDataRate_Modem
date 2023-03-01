/*
 * Copyright 2020 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 *
 */

#include <pybind11/pybind11.h>

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <numpy/arrayobject.h>

namespace py = pybind11;

// Headers for binding functions
/**************************************/
// The following comment block is used for
// gr_modtool to insert function prototypes
// Please do not delete
/**************************************/
// BINDING_FUNCTION_PROTOTYPES(
    void bind_TAG_CHUNKpreamble(py::module& m);
    void bind_Chunk_ExtractQPSK(py::module& m);
    void bind_Chunk_ExtractBPSK(py::module& m);
    void bind_Frame_Extract_ff(py::module& m);
    void bind_Frame_Extract_bb(py::module& m);
    void bind_Tag_FrameASM_ff(py::module& m);
    void bind_Tag_FrameASM_bb(py::module& m);
    void bind_Resolve_Phase(py::module& m);
    void bind_Decode_RS(py::module& m);
    void bind_Encode_RS(py::module& m);
// ) END BINDING_FUNCTION_PROTOTYPES


// We need this hack because import_array() returns NULL
// for newer Python versions.
// This function is also necessary because it ensures access to the C API
// and removes a warning.
void* init_numpy()
{
    import_array();
    return NULL;
}

PYBIND11_MODULE(HighDataRate_Modem_python, m)
{
    // Initialize the numpy C API
    // (otherwise we will see segmentation faults)
    init_numpy();

    // Allow access to base block methods
    py::module::import("gnuradio.gr");

    /**************************************/
    // The following comment block is used for
    // gr_modtool to insert binding function calls
    // Please do not delete
    /**************************************/
    // BINDING_FUNCTION_CALLS(
    bind_TAG_CHUNKpreamble(m);
    bind_Chunk_ExtractQPSK(m);
    bind_Chunk_ExtractBPSK(m);
    bind_Frame_Extract_ff(m);
    bind_Frame_Extract_bb(m);
    bind_Tag_FrameASM_ff(m);
    bind_Tag_FrameASM_bb(m);
    bind_Resolve_Phase(m);
    bind_Decode_RS(m);
    bind_Encode_RS(m);
    // ) END BINDING_FUNCTION_CALLS
}