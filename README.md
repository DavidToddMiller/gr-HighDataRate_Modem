                                                    gr-HighDataRate_Modem

gr-HighDataRate_Modem is a GNU Radio Out-Of-Tree (OOT) High Data Rate (HDR)_Modem module that include the blocks required to run GNU Radio at 7.5 Mbps with BPSK and at 15.0 Mbps with QPSK. This module is a much improved approach with blocks that were based on blocks introduced at a GNU Radio Conference 2021 lightning Talk and the associated paper in the GNU Radio Conference 2021 proceedings:

    • “Demonstration of GNU Radio High Data Rate BPSK 10 Mbps Modem Real-Time with Only Multi-Core General Purpose Processors (GRCON 2021)”

The conference paper is also provided in the “docs” folder of this github site and provides technical details on all three OOT blocks.

However, the GRCON 2021 paper required that each frame had a frame counter in addition to knowledge about the frame length and frame ASM. This improved algorithm approach with blocks in gr-HighDataRate_Modem does not require a frame counter, just knowledge about the frame ASM and frame length. The details on the approach and blocks are provided in the "docs" folder.

Also, example flowgraphs are provided in the “examples” folder of this github site:
    • Simulation .grc file if no LimeSDR-Mini is available
    • Full RF Transmit/Receive Loop .grc file when LimeSDR-Mini is used
    • Sample Modulator File in .zip format is available in folder also to quickly run the transmit Modulator in Flowgraphs
      (up to 24000 frames for about a 12 second run at 10 Mbps)
    • The original frame stream in baseband real bits before modulation that can be compared to the received stream for
      verification that no bits or frames had errors or were lost. Flowgraph to compare receive bits to original bits is also
      provided.
   

                                            INSTALLATION FROM SOURCE

The installation procedure of gr-HighDataRate_Modem source code is the usual of a GNU Radio out-of-tree module. The detailed instructions are as follows for building from source in a system where GNU Radio 3.9 has already been installed with Ubuntu 20.04:

                                                  DEPENDENCIES

There are some build dependencies for GNU Radio out-of-tree modules that are not required to run GNU Radio, so some distributions might not install them by default when GNU Radio is installed.

VERY IMPORTANT:  A Personal Computer With A CPU Containing At Least 8 Cores Is Required To Use These Blocks At The Full 7.5 Mbps with BPSK and 15.0 Mbps QPSK.  See The Conference Paper For Details On The Parallel Core Approached Used To Greatly Increase The Real-Time Data Rate Capability Of Gnu Radio. This new and approved approach that no longer requires a frame counter also uses the parallel core method.

                                                  DOWNLOADING

The gr-HighDataRate_Modem module and blocks within the module were developed in this DavidToddMiller/gr-HighDataRate_Modem Github repository. One can use the typical github clone command in the Ubuntu terminal to download all of the needed source code folders and files for example:

“ git clone https://github.com/DavidToddMiller/gr-hdr_modem.git ”

                                          BUILDING AND INSTALLING

After downloading, gr-HighDataRate_Modem can be built and installed using cmake. The following can be run inside the directory containing the gr-HighDataRate_Modem sources:

mkdir build

cd build

sudo cmake ../

sudo make

sudo make install

sudo ldconfig

                                        RUNNING THE .grc FLOWGRAPHS

The .py generated file in GNU Radio Companion should be run from the Ubuntu terminal because the files run at                 15 Megasamples/second with text printouts including frame count up to about 24000 frames during about a 12 second run when using the included provided BPSK Modulator File and QPSK Modulator File in the “examples” folder of this github site. 
The provided BPSK modulator file and QPSK Modulator File are provided for convenience, but a user can also generate their own modulator file with the provided BPSK Modulator .grc flowgraph file in the “examples” folder of this site.  The BPSK Modulator file also contains about 1.0 seconds of a 10101010 pattern that was placed at the beginning of the modulator file (.zip in "examples" folder) before the 24000 frames (length of each frame is 4192 bits including 32 bit ASM) generated by the .grc BPSK Modulator file and QPSK Modulator File.  Longer files can be generated with the Modulator .grc Flowgraph in the "example" folder, but just add at least 0.5 seconds of a prepended 101010101010 pattern when generating new BPSK Modulator files.

                                              
