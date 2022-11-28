#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.4.0

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
from gnuradio import filter
from gnuradio import fec
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import gr, pdu
import satellites
import satellites.components.deframers
import time
import threading



from gnuradio import qtgui

class Pluto_TX(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "Pluto_TX")

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
        self.variable_ccsds_encoder_def_0 = variable_ccsds_encoder_def_0 = fec.ccsds_encoder_make(2048,0, fec.CC_STREAMING)
        self.variable_cc_encoder_def_0 = variable_cc_encoder_def_0 = fec.cc_encoder_make(2048,7, 2, [79,-109], 0, fec.CC_STREAMING, False)
        self.samp_rate = samp_rate = 1024000
        self.freq_update = freq_update = 0

        ##################################################
        # Blocks
        ##################################################
        self.doppler_bin = blocks.probe_signal_f()
        def _freq_update_probe():
          while True:

            val = self.doppler_bin.level()
            try:
              try:
                self.doc.add_next_tick_callback(functools.partial(self.set_freq_update,val))
              except AttributeError:
                self.set_freq_update(val)
            except AttributeError:
              pass
            time.sleep(1.0 / (32))
        _freq_update_thread = threading.Thread(target=_freq_update_probe)
        _freq_update_thread.daemon = True
        _freq_update_thread.start()
        self.satellites_encode_rs_ccsds_0 = satellites.encode_rs(False, 1)
        self.satellites_ccsds_concatenated_deframer_0_0 = satellites.components.deframers.ccsds_concatenated_deframer(frame_size = 223, precoding = None, rs_basis = "conventional", rs_interleaving = 1, scrambler = "CCSDS", convolutional = "CCSDS", syncword_threshold = 1, options="")
        self.satellites_ccsds_concatenated_deframer_0 = satellites.components.deframers.ccsds_concatenated_deframer(frame_size = 223, precoding = None, rs_basis = "conventional", rs_interleaving = 1, scrambler = "CCSDS", convolutional = "CCSDS", syncword_threshold = 1, options="")
        self.qtgui_time_sink_x_1_0 = qtgui.time_sink_c(
            1000, #size
            samp_rate, #samp_rate
            'Unfiltered data waveform', #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1_0.set_update_time(0.50)
        self.qtgui_time_sink_x_1_0.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_0.enable_tags(True)
        self.qtgui_time_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0.enable_stem_plot(False)

        self.qtgui_time_sink_x_1_0.disable_legend()

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
                    self.qtgui_time_sink_x_1_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_0_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_c(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1.set_update_time(1.0)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)


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
                    self.qtgui_time_sink_x_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.qtgui_freq_sink_x_0_1 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            (samp_rate/4), #bw
            'Before Doppler Correction', #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1.set_y_axis((-60), (-10))
        self.qtgui_freq_sink_x_0_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_1.enable_grid(False)
        self.qtgui_freq_sink_x_0_1.set_fft_average(0.1)
        self.qtgui_freq_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_1.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_1_win)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            (samp_rate/4), #bw
            "TX", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.5)
        self.qtgui_freq_sink_x_0_0.set_y_axis((-60), (-10))
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            (samp_rate/4), #bw
            'Before PM Demod', #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-60), (-10))
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(0.1)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
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
        self.pdu_tagged_stream_to_pdu_0 = pdu.tagged_stream_to_pdu(gr.types.byte_t, 'packet_len')
        self.pdu_pdu_to_tagged_stream_0_0 = pdu.pdu_to_tagged_stream(gr.types.byte_t, 'packet_len')
        self.pdu_pdu_to_tagged_stream_0 = pdu.pdu_to_tagged_stream(gr.types.byte_t, 'packet_len')
        self.hilbert_fc_0 = filter.hilbert_fc(65, window.WIN_HAMMING, 6.76)
        self.fft_vxx_0 = fft.fft_vcc(1024, True, window.blackmanharris(1024), True, 1)
        self.fec_extended_encoder_0 = fec.extended_encoder(encoder_obj_list=variable_cc_encoder_def_0, threading='capillary', puncpat='11')
        self.digital_symbol_sync_xx_0_0 = digital.symbol_sync_cc(
            digital.TED_GARDNER,
            16.0,
            (2*3.14159/1000),
            0.7,
            1.0,
            0.001,
            1,
            digital.constellation_bpsk().base(),
            digital.IR_PFB_NO_MF,
            128,
            [])
        self.digital_psk_mod_0_0 = digital.psk.psk_mod(
            constellation_points=2,
            mod_code="gray",
            differential=False,
            samples_per_symbol=2,
            excess_bw=0.5,
            verbose=False,
            log=False)
        self.digital_costas_loop_cc_0_0 = digital.costas_loop_cc((2*3.14159/1000), 2, False)
        self.digital_additive_scrambler_bb_0 = digital.additive_scrambler_bb(0xA9, 0xFF, 7, count=0, bits_per_byte=1, reset_tag_key="packet_len")
        self.blocks_vco_c_0 = blocks.vco_c(samp_rate, 6.28, 1)
        self.blocks_unpack_k_bits_bb_0_0_0_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_unpack_k_bits_bb_0_0_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, 8000,True)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 1024)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 223, "packet_len")
        self.blocks_stream_mux_0 = blocks.stream_mux(gr.sizeof_char*1, (32, 2040))
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_rotator_cc_0_0 = blocks.rotator_cc((128000*2*3.14159/1024000/2), False)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_char*1, 32)
        self.blocks_pack_k_bits_bb_1 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_short*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_ff((-1))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_cc(1.0)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(1.0)
        self.blocks_keep_one_in_n_0_0 = blocks.keep_one_in_n(gr.sizeof_gr_complex*1, 4)
        self.blocks_keep_one_in_n_0 = blocks.keep_one_in_n(gr.sizeof_gr_complex*1, 4)
        self.blocks_file_source_0_0_0_0_0_0 = blocks.file_source(gr.sizeof_char*1, '/home/davem/gr-HighDataRate_Modem/examples/Doppler_And_CCSDS_TTC_Flowgraphs_LowRate/Just_CCSDS_Frame_counter', True, 0, 0)
        self.blocks_file_source_0_0_0_0_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_0_0_0_0_0_0.set_processor_affinity([1])
        self.blocks_file_source_0_0_0_0_0 = blocks.file_source(gr.sizeof_char*1, '/home/davem/gr-HighDataRate_Modem/examples/Doppler_And_CCSDS_TTC_Flowgraphs_LowRate/32bitASM_CCSDS_only', True, 0, 0)
        self.blocks_file_source_0_0_0_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_0_0_0_0_0.set_processor_affinity([1])
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/davem/gr-HighDataRate_Modem/examples/Doppler_And_CCSDS_TTC_Flowgraphs_LowRate/CCSDS_TTC_SINK', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_real_0_0_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1024)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_argmax_xx_0 = blocks.argmax_fs(1024)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff((-128000))
        self.analog_sig_source_x_0_2 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 0.002, 50000, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c((samp_rate/4), analog.GR_COS_WAVE, (-64000), 1, 0, 0)
        self.analog_pll_carriertracking_cc_0 = analog.pll_carriertracking_cc((200*2*3.14159/256000), (5000*2*3.14159/256000), (-5000*2*3.14159/256000))
        self.analog_phase_modulator_fc_0 = analog.phase_modulator_fc(1.0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, (1/1.5/1), 0)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 250)
        self.Doppler_Start_blocks_keep_m_in_n_0 = blocks.keep_m_in_n(gr.sizeof_gr_complex, 1024, 32000, 0)
        self.Doppler_Rotate_Correction_x_0_0 = analog.sig_source_c((samp_rate/4), analog.GR_COS_WAVE, (-1*freq_update), 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.pdu_tagged_stream_to_pdu_0, 'pdus'), (self.satellites_encode_rs_ccsds_0, 'in'))
        self.msg_connect((self.satellites_ccsds_concatenated_deframer_0, 'out'), (self.pdu_pdu_to_tagged_stream_0_0, 'pdus'))
        self.msg_connect((self.satellites_ccsds_concatenated_deframer_0_0, 'out'), (self.pdu_pdu_to_tagged_stream_0_0, 'pdus'))
        self.msg_connect((self.satellites_encode_rs_ccsds_0, 'out'), (self.pdu_pdu_to_tagged_stream_0, 'pdus'))
        self.connect((self.Doppler_Rotate_Correction_x_0_0, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.Doppler_Start_blocks_keep_m_in_n_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_phase_modulator_fc_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_pll_carriertracking_cc_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_0_2, 0), (self.blocks_vco_c_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.doppler_bin, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_keep_one_in_n_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_argmax_xx_0, 1), (self.blocks_null_sink_0_0, 0))
        self.connect((self.blocks_argmax_xx_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.hilbert_fc_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_argmax_xx_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_multiply_const_vxx_0_1, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.satellites_ccsds_concatenated_deframer_0, 0))
        self.connect((self.blocks_complex_to_real_0_0_0, 0), (self.analog_phase_modulator_fc_0, 0))
        self.connect((self.blocks_file_source_0_0_0_0_0, 0), (self.blocks_stream_mux_0, 0))
        self.connect((self.blocks_file_source_0_0_0_0_0_0, 0), (self.blocks_unpack_k_bits_bb_0_0_0_0, 0))
        self.connect((self.blocks_keep_one_in_n_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.blocks_keep_one_in_n_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.Doppler_Start_blocks_keep_m_in_n_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_freq_sink_x_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.digital_symbol_sync_xx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.satellites_ccsds_concatenated_deframer_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.qtgui_time_sink_x_1_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.analog_pll_carriertracking_cc_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.digital_psk_mod_0_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_1, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_rotator_cc_0_0, 0), (self.blocks_complex_to_real_0_0_0, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blocks_stream_mux_0, 0), (self.fec_extended_encoder_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.pdu_tagged_stream_to_pdu_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_pack_k_bits_bb_1, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_keep_one_in_n_0_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0_0_0, 0), (self.digital_additive_scrambler_bb_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0_0_0_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_vco_c_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.digital_additive_scrambler_bb_0, 0), (self.blocks_stream_mux_0, 1))
        self.connect((self.digital_costas_loop_cc_0_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0, 0), (self.qtgui_const_sink_x_0_0, 0))
        self.connect((self.digital_psk_mod_0_0, 0), (self.blocks_rotator_cc_0_0, 0))
        self.connect((self.digital_symbol_sync_xx_0_0, 0), (self.digital_costas_loop_cc_0_0, 0))
        self.connect((self.fec_extended_encoder_0, 0), (self.blocks_repeat_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.hilbert_fc_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.pdu_pdu_to_tagged_stream_0, 0), (self.blocks_unpack_k_bits_bb_0_0_0, 0))
        self.connect((self.pdu_pdu_to_tagged_stream_0_0, 0), (self.blocks_file_sink_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Pluto_TX")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_variable_ccsds_encoder_def_0(self):
        return self.variable_ccsds_encoder_def_0

    def set_variable_ccsds_encoder_def_0(self, variable_ccsds_encoder_def_0):
        self.variable_ccsds_encoder_def_0 = variable_ccsds_encoder_def_0

    def get_variable_cc_encoder_def_0(self):
        return self.variable_cc_encoder_def_0

    def set_variable_cc_encoder_def_0(self, variable_cc_encoder_def_0):
        self.variable_cc_encoder_def_0 = variable_cc_encoder_def_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.Doppler_Rotate_Correction_x_0_0.set_sampling_freq((self.samp_rate/4))
        self.analog_sig_source_x_0.set_sampling_freq((self.samp_rate/4))
        self.analog_sig_source_x_0_2.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, (self.samp_rate/4))
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, (self.samp_rate/4))
        self.qtgui_freq_sink_x_0_1.set_frequency_range(0, (self.samp_rate/4))
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_0.set_samp_rate(self.samp_rate)

    def get_freq_update(self):
        return self.freq_update

    def set_freq_update(self, freq_update):
        self.freq_update = freq_update
        self.Doppler_Rotate_Correction_x_0_0.set_frequency((-1*self.freq_update))




def main(top_block_cls=Pluto_TX, options=None):

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
