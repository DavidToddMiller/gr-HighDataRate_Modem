#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.5.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
import pmt
from gnuradio import digital
from gnuradio import fec
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import HighDataRate_Modem



from gnuradio import qtgui

class RS_CC_TX_RCV(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "RS_CC_TX_RCV")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.variable_cc_encoder_def_0 = variable_cc_encoder_def_0 = fec.cc_encoder_make(2072,7, 2, [79,-109], 0, fec.CC_STREAMING, False)
        self.variable_cc_decoder_def_0 = variable_cc_decoder_def_0 = fec.cc_decoder.make(2072,7, 2, [79,-109], 0, (-1), fec.CC_STREAMING, False)
        self.samp_rate = samp_rate = 2000000
        self.constel = constel = digital.constellation_calcdist(digital.psk_2()[0], digital.psk_2()[1],
        4, 1, digital.constellation.AMPLITUDE_NORMALIZATION).base()
        self.constel.gen_soft_dec_lut(8)

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_time_sink_x_1_0_0 = qtgui.time_sink_c(
            128, #size
            samp_rate, #samp_rate
            'RF NOISE', #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1_0_0.set_update_time(1.0)
        self.qtgui_time_sink_x_1_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_0_0.enable_tags(True)
        self.qtgui_time_sink_x_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_1_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_0_0_win)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
            1024, #size
            'BPSK constellation', #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.50)
        self.qtgui_const_sink_x_0_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0.enable_axis_labels(True)

        self.qtgui_const_sink_x_0_0.disable_legend()

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.fec_extended_encoder_0 = fec.extended_encoder(encoder_obj_list=variable_cc_encoder_def_0, threading='capillary', puncpat='11')
        self.fec_extended_decoder_0 = fec.extended_decoder(decoder_obj_list=variable_cc_decoder_def_0, threading='capillary', ann=None, puncpat='11', integration_period=10000)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(2, (3.14159/100.0), firdes.root_raised_cosine(32,64,1.0,0.5,1704), 32, 0, 1.5, 1)
        self.digital_costas_loop_cc_0_0 = digital.costas_loop_cc((2*3.14159/1000), 2, False)
        self.digital_constellation_modulator_0_0 = digital.generic_mod(
            constellation=constel,
            differential=False,
            samples_per_symbol=2,
            pre_diff_code=True,
            excess_bw=0.5,
            verbose=False,
            log=False,
            truncate=False)
        self.blocks_vector_to_stream_0_1 = blocks.vector_to_stream(gr.sizeof_char*1, 255)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_char*1, 223)
        self.blocks_unpack_k_bits_bb_0_0_0_0_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_tag_gate_0 = blocks.tag_gate(gr.sizeof_char * 1, False)
        self.blocks_tag_gate_0.set_single_key("")
        self.blocks_stream_to_vector_2_0_0 = blocks.stream_to_vector(gr.sizeof_char*1, 255)
        self.blocks_stream_to_vector_2_0_0.set_processor_affinity([3])
        self.blocks_stream_to_vector_2_0 = blocks.stream_to_vector(gr.sizeof_char*1, 223)
        self.blocks_stream_to_tagged_stream_0_0_1 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 2040, "packet_len")
        self.blocks_stream_to_tagged_stream_0_0_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 223, "packet_len")
        self.blocks_stream_mux_0 = blocks.stream_mux(gr.sizeof_char*1, (32, 2040))
        self.blocks_stream_demux_0 = blocks.stream_demux(gr.sizeof_char*1, (32,2040))
        self.blocks_pack_k_bits_bb_0_0 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_null_sink_1 = blocks.null_sink(gr.sizeof_char*1)
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_cc(0.8)
        self.blocks_file_source_0_0_0_0_0_0 = blocks.file_source(gr.sizeof_char*1, '/home/davem/Github_Test/gr-HighDataRate_Modem/examples/High_Speed_FEP-Gateway_CCSDS_Reed-Solomon_CC_ZeroMQ/Just_CCSDS_Frame_counter', True, 0, 0)
        self.blocks_file_source_0_0_0_0_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_0_0_0_0_0_0.set_processor_affinity([1])
        self.blocks_file_source_0_0_0_0_0 = blocks.file_source(gr.sizeof_char*1, '/home/davem/Github_Test/gr-HighDataRate_Modem/examples/High_Speed_FEP-Gateway_CCSDS_Reed-Solomon_CC_ZeroMQ/32bitASM_CCSDS_only', True, 0, 0)
        self.blocks_file_source_0_0_0_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_0_0_0_0_0.set_processor_affinity([1])
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/davem/Github_Test/gr-HighDataRate_Modem/examples/High_Speed_FEP-Gateway_CCSDS_Reed-Solomon_CC_ZeroMQ/CCSDS_TTC_SINK', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, (1/0.75/10), 0)
        self.HighDataRate_Modem_Tag_FrameASM_xx_0 = HighDataRate_Modem.Tag_FrameASM_bb(1, 32, 1)
        self.HighDataRate_Modem_Resolve_Phase_0 = HighDataRate_Modem.Resolve_Phase(1, 2072, 120000, 1)
        self.HighDataRate_Modem_Frame_Extract_xx_0 = HighDataRate_Modem.Frame_Extract_bb(2072, 15000, 32)
        self.HighDataRate_Modem_Encode_RS_0 = HighDataRate_Modem.Encode_RS(False, 0, 1)
        self.HighDataRate_Modem_Decode_RS_0 = HighDataRate_Modem.Decode_RS(False, 0, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.HighDataRate_Modem_Decode_RS_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.HighDataRate_Modem_Encode_RS_0, 0), (self.blocks_vector_to_stream_0_1, 0))
        self.connect((self.HighDataRate_Modem_Frame_Extract_xx_0, 0), (self.HighDataRate_Modem_Resolve_Phase_0, 0))
        self.connect((self.HighDataRate_Modem_Resolve_Phase_0, 0), (self.blocks_stream_demux_0, 0))
        self.connect((self.HighDataRate_Modem_Tag_FrameASM_xx_0, 0), (self.HighDataRate_Modem_Frame_Extract_xx_0, 0))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_noise_source_x_0, 0), (self.qtgui_time_sink_x_1_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.fec_extended_decoder_0, 0))
        self.connect((self.blocks_file_source_0_0_0_0_0, 0), (self.blocks_stream_mux_0, 0))
        self.connect((self.blocks_file_source_0_0_0_0_0_0, 0), (self.blocks_stream_to_tagged_stream_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.digital_constellation_modulator_0_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0_0, 0), (self.blocks_stream_to_vector_2_0_0, 0))
        self.connect((self.blocks_stream_demux_0, 0), (self.blocks_null_sink_1, 0))
        self.connect((self.blocks_stream_demux_0, 1), (self.blocks_pack_k_bits_bb_0_0, 0))
        self.connect((self.blocks_stream_mux_0, 0), (self.fec_extended_encoder_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0_0_0, 0), (self.blocks_stream_to_vector_2_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0_0_1, 0), (self.blocks_stream_mux_0, 1))
        self.connect((self.blocks_stream_to_vector_2_0, 0), (self.HighDataRate_Modem_Encode_RS_0, 0))
        self.connect((self.blocks_stream_to_vector_2_0_0, 0), (self.HighDataRate_Modem_Decode_RS_0, 0))
        self.connect((self.blocks_tag_gate_0, 0), (self.HighDataRate_Modem_Tag_FrameASM_xx_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_multiply_const_vxx_2, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0_0_0_0_0, 0), (self.blocks_stream_to_tagged_stream_0_0_1, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_vector_to_stream_0_1, 0), (self.blocks_unpack_k_bits_bb_0_0_0_0_0, 0))
        self.connect((self.digital_constellation_modulator_0_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0, 0), (self.qtgui_const_sink_x_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_costas_loop_cc_0_0, 0))
        self.connect((self.fec_extended_decoder_0, 0), (self.blocks_tag_gate_0, 0))
        self.connect((self.fec_extended_encoder_0, 0), (self.blocks_pack_k_bits_bb_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "RS_CC_TX_RCV")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_variable_cc_encoder_def_0(self):
        return self.variable_cc_encoder_def_0

    def set_variable_cc_encoder_def_0(self, variable_cc_encoder_def_0):
        self.variable_cc_encoder_def_0 = variable_cc_encoder_def_0

    def get_variable_cc_decoder_def_0(self):
        return self.variable_cc_decoder_def_0

    def set_variable_cc_decoder_def_0(self, variable_cc_decoder_def_0):
        self.variable_cc_decoder_def_0 = variable_cc_decoder_def_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_0_0.set_samp_rate(self.samp_rate)

    def get_constel(self):
        return self.constel

    def set_constel(self, constel):
        self.constel = constel




def main(top_block_cls=RS_CC_TX_RCV, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
