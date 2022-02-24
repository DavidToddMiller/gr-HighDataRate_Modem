                                  gr-HighDataRate_Modem

gr-HighDataRate_Modem is a GNU Radio Out-Of-Tree (OOT) High Data Rate (HDR)_Modem module that include the blocks required to run GNU Radio at 15.0 Mbps with QPSK. This module is a much improved approach with blocks that were based on blocks introduced at a GNU Radio Conference 2021 lightning Talk and the associated paper in the GNU Radio Conference 2021 proceedings:

    • “Demonstration of GNU Radio High Data Rate BPSK 10 Mbps Modem Real-Time with Only Multi-Core General Purpose Processors (GRCON 2021)”

The conference paper is also provided in the “docs” folder of this github site and provides technical details on all three OOT blocks. The new gr-HighDataRate_Modem design is also in "docs" folder titled  "gr-HighDataRate_Modem Design Document (version #1 - DRAFT).odt"

The GRCON 2021 paper required that each frame had a frame counter in addition to knowledge about the frame length and frame ASM. This improved algorithm approach with blocks in gr-HighDataRate_Modem does not require a frame counter, just knowledge about the frame ASM and frame length. The details on the approach and blocks are provided in the design document in "docs" folder.

Also, example flowgraphs are provided in the “examples” folder of this github site:
    • Sample Modulator Files in .zip format are available in folder also to quickly run the transmit Modulator in Flowgraphs
      (up to about 40000 frames for about a 10-12 second run at 15 Mbps)
    • The original frame stream in baseband real bits before modulation is provided that can be compared to the received stream for verification that no bits or frames had errors or were lost. First 2 frames are deleted for comparison to received frame stream that may have first 0-2 frames missing. 
    • The provided flowgraphs run with frame length of 4192 bits that includes 32 bit CCSDS ASM.  See Design Document in "doc" folder for details.  Other frame length options will be available in future.
    • For simulation, a separate simulation .grc file for QPSK in "examples" folder has "throttle" block available for those that do not have a LimeSDR-Mini to try out gr-HighDataRate_Modem without LimeSDR-Mini with QPSK.
    • Full RF Transmit/Receive Loop .grc file when LimeSDR-Mini is used is in "examples" folder.
   

                               INSTALLATION FROM SOURCE

The installation procedure of gr-HighDataRate_Modem source code is the usual of a GNU Radio out-of-tree (OOT) module. The detailed instructions are as follows for building from source in a system where GNU Radio 3.10 (should work with GNU Radio version 3.9 also) has already been installed with Ubuntu 20.04:

                                DEPENDENCIES

There are some build dependencies for GNU Radio out-of-tree modules that are not required to run GNU Radio, so some distributions might not install them by default when GNU Radio is installed.

VERY IMPORTANT:  A Personal Computer With A CPU Containing At Least 8 Cores Is Required To Use These Blocks At The Full 15.0 Mbps QPSK.  See The Conference Paper For Details On The Parallel Core Approached Used To Greatly Increase The Real-Time Data Rate Capability Of GNU Radio. This new and approved approach that no longer requires a frame counter also uses the parallel core method.

                                                  DOWNLOADING

The gr-HighDataRate_Modem module and blocks within the module were developed in this DavidToddMiller/gr-HighDataRate_Modem Github repository. One can use the typical github clone command in the Ubuntu terminal to download all of the needed source code folders and files for example:

“ git clone https://github.com/DavidToddMiller/gr-HighDataRate_Modem.git ”

                          BUILDING AND INSTALLING

After downloading, gr-HighDataRate_Modem can be built and installed using cmake. The following can be run inside the directory containing the gr-HighDataRate_Modem sources:

mkdir build

cd build

sudo cmake ../

sudo make

sudo make install

sudo ldconfig

                         RUNNING THE .grc FLOWGRAPHS

The .py generated file in GNU Radio Companion should be run from the Ubuntu terminal because the files run at                 15.0 Megasamples/second with text printouts including frame count up to about 40000 frames during about a 10-12 second run when using the included provided QPSK Modulator File in the “examples” folder of this github site. The provided QPSK Modulator File is provided for convenience, but a user can also generate their own modulator file with the provided QPSK Modulator .grc flowgraph files in the “examples/QPSK_Generate_Modulator_Files” folder of this site.

                         FUTURE WORK

1.  Add BPSK at 15.0 Megasamples per second (7.5 Mbps)
2.  Add support for more frame lengths beyond just 4192 bit length frames

                                              
