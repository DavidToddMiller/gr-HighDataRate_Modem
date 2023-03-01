                                  gr-HighDataRate_Modem

gr-HighDataRate_Modem is a GNU Radio Out-Of-Tree (OOT) High Data Rate (HDR)_Modem and Front End Processor (FEP)/Gateway module that includes:
 
  1) Blocks and flowgraphs required to run GNU Radio at 15.0 Mbps with QPSK with parallel CPU cores

  2) New as of December 2022: FEP/Gateway CCSDS encoding/decoding and also baseband processing and data transport IP data interface (ZeroMQ) blocks and flowgraphs for high data rate operation with parallel CPU cores. (Includes CCSDS DVB-S2)
  
  3) New as of January 2023: Updated CCSDS Phase Modulation (PM) with a subcarrier and Concatenated Coding flowgraphs with streaming blocks for processing efficiency and stability (No message blocks) (includes processing Doppler removal also via FFTs for flowgraphs to support actual LEO spacecraft links)
  

  
This module is based on the approach that was introduced during a GNU Radio Conference 2022 Talk and in the associated paper in the GNU Radio Conference 2022 proceedings and Conference 2022 website:

   - "Demonstration of GNU Radio High Data Rate QPSK Modem at 15.0 Mbps Real-Time with Multi-Core General Purpose Processor (GRCON 2022)"

The 2022 conference paper is also provided in the “docs” folder of this github site and provides technical details on all the Out-Of-Tree (OOT) blocks for uncoded QPSK up to 15.0 Mbps. The gr-HighDataRate_Modem design document is also in the "docs" folder titled: "gr-HighDataRate_Modem Design Document (version #1 - DRAFT).odt"

The approach with blocks in gr-HighDataRate_Modem does not require a frame counter that the 2021 Conference design required, just knowledge about the frame ASM and frame length. The details on the approach and blocks are provided in the design document in the "docs" folder.

Also, example flowgraphs for uncoded operations at 15.0 Mbps are provided in the “examples” folder of this github site:

  - Sample Modulator Files in .zip format are available in the folder ("examples/QPSK_Generate_Modulator_Files") also to quickly run the transmit Modulator in Flowgraphs (up to about 40000 frames for about a 10-12 second run at 15 Mbps). (Unzip files before running flowgraph)

  - The original frame stream in baseband real bits before modulation is provided that can be compared to the received stream for verification that no bits or frames had errors or were lost. The first 2 frames are deleted for comparison to the received frame stream that may have the first 0-2 frames missing when running the flowgraph.

  - The provided flowgraphs run with a frame length of 4192 bits that includes the 32 bit CCSDS ASM.  See the Design Document in the "doc" folder for all the details.

  - For simulation, a separate "simulation" .grc file for QPSK is in the "examples" folder and has a "throttle" block available for those that do not have a LimeSDR-Mini in order to try out gr-HighDataRate_Modem without the LimeSDR-Mini with QPSK.

  - For the Full RF Transmit/Receive Loop, the .grc file with the LimeSDR-Mini is used and is in the "examples" folder.


                     CCSDS High Speed FEP/Gateway Flowgraphs/Products
   
JANUARY 2023 Update, High Speed FEP/Gateway blocks and flowgraphs including CCSDS Reed-Solomon & Convolutional Encoding/Decoding: Decode_RS and Encode_RS OOT blocks added for high rate CCSDS Reed-Solomon encoding/decoding with block vector interfaces for high speed operations (CCSDS convolutional coding from In-tree blocks included). Flowgraphs with Reed-Solomon and Convolutional Coding and ZeroMQ data transport are provided at following folder location:

  - Example Flowgraphs located in "examples/High_Speed_FEP-Gateway_CCSDS_Reed-Solomon_CC_ZeroMQ" folder on this site/repository. 

  - FEP/Gateway processing examples with CCSDS Reed-Solomon (Conventional & (255,223)) and CCSDS Convolutional coding and CCSDS scrambling with multicores used as example up to 24.0 Msps with ZeroMQ data transport interfaces. Block Framing, ASMs, Coding, and scrambling in accordance with CCSDS Blue Book, 131.0-B-4, "TM Synchronization and Channel Coding". Each CCSDS frame in frame stream file (file name: "Just_CCSDS_Frame_counter") starts with "7D41" (hexadecimal).
   
  - A few of the blocks are OOT blocks (CCSDS Reed-Solomon Encode/Decode and Frame_Extract and Resolve_Phase) in gr-HighDataRate_Modem module otherwise all blocks are in the standard GNU Radio In-Tree library. 


                     CCSDS High Speed DVB-S2 Flowgraphs/Products

JANUARY 2023 Update, High Speed FEP/Gateway blocks and flowgraphs including CCSDS DVBS2 LDPC & BCH Encoding/Decoding: DVB-S2 Transmit/Encode blocks are In-Tree. However, DVB-S2 Receive/Decode blocks are OOT (Build Receive blocks from github repository fork located at "https://github.com/marcusmueller/gr-dvbs2rx.git". Flowgraphs with DVBS2 LDPC and BCH coding and ZeroMQ data transport interfaces are provided at following folder location:

  - Example Flowgraphs located in "/examples/High_Speed_FEP-Gateway_CCSDS_DVBS2_LDPC_BCH_ZeroMQ" folder on this site/repository. 

  - FEP/Gateway processing example with CCSDS DVB-S2 LDPC/BCH (64800 bit Frame Size) as example up to 20.0 Msps (about 9.941 Mbps after decoding) with ZeroMQ data transport interfaces. Flowgraph uses 4 Parallel Decoder chains with multi-cores "High_Speed_DVBS2_LDPC_BCH_Decoder_FEP_Gateway.grc".  
Before running parallel decoder flowgraph, generate File Source block file for flowgraph with other flowgraph running at slower speed: "PreEncode_PreDeModulate_QPSK_RATE_0.5_LDPC_BCH.grc" to generate File Sink block file "DVB_QPSK_test1.

  - Stream of continuous CCSDS frames are run asynchronously in DVB-S2 code block data fields as stated in "CCSDS SPACE LINK PROTOCOLS OVER ETSI DVB-S2 STANDARD", Blue Book, CCSDS 131.3-B-2.  


                     CCSDS TT&C/Doppler Flowgraphs/Products

JANUARY-March 2023 Updates on CCSDS/TT&C/Doppler: Based on questions received at the 2022 GNU Radio Conference from the audience at the end of my talk, I have now included a CCSDS TT&C Flowgraph at low data rates for Phase Modulation (PM) with a subcarrier and Concatenated Coding (includes processing Doppler removal also via FFTs) that is used extensively by many space agencies:

  - Two "Simulation" Flowgraphs located in "examples/Doppler_And_CCSDS_TTC_Flowgraphs_LowRate" Folder on this site. (March 2023 Update: Added Dual Basis/Conventional Option in Properties/Parameter Settings for Reed Solomon Blocks. Also added option for Normal (255,223) and Shortened (252,220) in Reed Solomon Blocks for Frame Sizes). One flowgraph for (255,223) and another flowgraph for Shortened (252,220).

  - New February 2023: Pluto/RTLSDR Dongle Pair (Actual Full Transmit/Receive RF Loop): Provided a single flowgraph for Transmit and Receive RF loop when using dongles. Transmit with Pluto Dongle and Receive with RTLSDR Dongle. Same as simulation flowgraph above except "Throttle" block replaced by "Pluto Sink" and "RTLSDR Source" blocks.

  - A few of the blocks are OOT blocks like CCSDS Reed-Solomon Encode/Decode in this gr-HighDataRate_Modem module (All blocks have stream interfaces (No message Blocks) for processing efficiency and stability). 

  - Runs at 16 kilosymbols/second with the coding included. 50 kHz subcarrier used. Each CCSDS Frame starts with "7D41" (hexadecimal).

  - With the Doppler FFT functions included, the flowgraph transmit and receive parts could be used operationally in real-time with a transmit/receive dongle for an actual Low Earth Orbit (LEO) spacecraft link that uses typical CCSDS low rate TT&C links at S-band.

 
                               INSTALLATION FROM SOURCE

The installation procedure of gr-HighDataRate_Modem source code is the usual procedure for a GNU Radio out-of-tree (OOT) module. The detailed instructions are as follows for building from source in a system where GNU Radio 3.10 (should work with GNU Radio version 3.9 also) has already been installed with Ubuntu 22.04:


                                DEPENDENCIES

There are some build dependencies for GNU Radio out-of-tree modules that are not required to run GNU Radio, so some distributions might not install them by default when GNU Radio is installed.

VERY IMPORTANT:  A Personal Computer with a CPU containing at least 8 Cores is required to use many of these flowgraphs at full rates.  See the Conference Paper for details on the Parallel Core Approach used to greatly increase the Real-Time Data Rate capability of GNU Radio. 


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

The .py generated file in the GNU Radio Companion should be run from the Ubuntu terminal because the files run at 15.0 Megasamples/second with text printouts on display including the frame count up to about 40000 frames during about a 10-12 second run when using the included provided QPSK Modulator File in the “examples” folder of this github site. The provided QPSK Modulator File is provided for convenience, but a user can also generate their own modulator file with the provided QPSK Modulator .grc flowgraph files in the “examples/QPSK_Generate_Modulator_Files” folder of this site.

    FUTURE WORK   (Expand Capabilities of Real-Time High Rate Modems and High Rate FEPs/Gateways)

1. When a 16-24 core Personal Computer becomes available, incorporate all high data rate blocks including encoding/decoding and Doppler removal/handling into single flowgraph to run in real-time up to 30.0 Msps (and/or two flowgraphs (Transmit/Receive) in real-time with coding or without. Also, use FEP/Gateway connected via ZeroMQ. 
2. Expand CCSDS Reed-Solomon options for interleaving. (March 2023 Update: Completed adding CCSDS Dual Basis and a common (252,220) CCSDS shortened code to Reed Solomon Blocks while keeping block vector in/out interfaces for speed and stability.) 



                                              
