# Copyright 2020 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

########################################################################
# Check if there is C++ code at all
########################################################################
if(NOT HighDataRate_Modem_sources)
    MESSAGE(STATUS "No C++ sources... skipping python bindings")
    return()
endif(NOT HighDataRate_Modem_sources)

########################################################################
# Check for pygccxml
########################################################################
GR_PYTHON_CHECK_MODULE_RAW(
    "pygccxml"
    "import pygccxml"
    PYGCCXML_FOUND
    )

include(GrPybind)

########################################################################
# Python Bindings
########################################################################
list(APPEND HighDataRate_Modem_python_files
    TAG_CHUNKpreamble_python.cc
    Chunk_ExtractQPSK_python.cc
    Tag_FrameASM_python.cc
    Chunk_ExtractBPSK_python.cc
    Frame_Extract_python.cc
    Resolve_Phase_python.cc
    Encode_RS_python.cc
    Decode_RS_python.cc python_bindings.cc)

GR_PYBIND_MAKE_OOT(HighDataRate_Modem
   ../..
   gr::HighDataRate_Modem
   "${HighDataRate_Modem_python_files}")

install(TARGETS HighDataRate_Modem_python DESTINATION ${GR_PYTHON_DIR}/HighDataRate_Modem COMPONENT pythonapi)
