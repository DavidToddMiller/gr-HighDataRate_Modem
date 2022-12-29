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
from gnuradio import fec
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import iio
import HighDataRate_Modem



from gnuradio import qtgui

class TX_Doppler_Dongle_RS_CC(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "TX_Doppler_Dongle_RS_CC")

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
        self.variable_cc_encoder_def_0 = variable_cc_encoder_def_0 = fec.cc_encoder_make(2048,7, 2, [79,-109], 0, fec.CC_STREAMING, False)
        self.samp_rate = samp_rate = 1024000
        self.constel = constel = digital.constellation_calcdist(digital.psk_2()[0], digital.psk_2()[1],
        4, 1, digital.constellation.AMPLITUDE_NORMALIZATION).base()
        self.constel.gen_soft_dec_lut(8)

        ##################################################
        # Blocks
        ##################################################
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
        self.qtgui_freq_sink_x_0_0.set_y_axis((-100), 0)
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
        self.iio_pluto_sink_0 = iio.fmcomms2_sink_fc32('' if '' else iio.get_pluto_uri(), [True, True], 32768, False)
        self.iio_pluto_sink_0.set_len_tag_key('')
        self.iio_pluto_sink_0.set_bandwidth(20000000)
        self.iio_pluto_sink_0.set_frequency(720000000)
        self.iio_pluto_sink_0.set_samplerate(samp_rate)
        self.iio_pluto_sink_0.set_attenuation(0, 10.0)
        self.iio_pluto_sink_0.set_filter_params('Auto', '', 0, 0)
        self.fec_extended_encoder_0 = fec.extended_encoder(encoder_obj_list=variable_cc_encoder_def_0, threading='capillary', puncpat='11')
        self.digital_constellation_modulator_0_0 = digital.generic_mod(
            constellation=constel,
            differential=False,
            samples_per_symbol=16,
            pre_diff_code=True,
            excess_bw=0.5,
            verbose=False,
            log=False,
            truncate=False)
        self.blocks_vector_to_stream_0_1 = blocks.vector_to_stream(gr.sizeof_char*1, 255)
        self.blocks_vco_c_0 = blocks.vco_c(samp_rate, 6.28, 1)
        self.blocks_unpack_k_bits_bb_0_0_0_0_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_stream_to_vector_2_0 = blocks.stream_to_vector(gr.sizeof_char*1, 223)
        self.blocks_stream_to_tagged_stream_0_0_1 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 2040, "packet_len")
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 223, "packet_len")
        self.blocks_stream_mux_0 = blocks.stream_mux(gr.sizeof_char*1, (32, 2040))
        self.blocks_rotator_cc_0_0 = blocks.rotator_cc((128000*2*3.14159/1024000/2), False)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_gr_complex*1, 4)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_keep_one_in_n_0 = blocks.keep_one_in_n(gr.sizeof_gr_complex*1, 4)
        self.blocks_file_source_0_0_0_0_0_0 = blocks.file_source(gr.sizeof_char*1, '/home/davem/Documents/CCSDS_TTC_Flowgraphs/Just_CCSDS_Frame_counter', True, 0, 0)
        self.blocks_file_source_0_0_0_0_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_0_0_0_0_0_0.set_processor_affinity([1])
        self.blocks_file_source_0_0_0_0_0 = blocks.file_source(gr.sizeof_char*1, '/home/davem/Documents/CCSDS_TTC_Flowgraphs/32bitASM_CCSDS_only', True, 0, 0)
        self.blocks_file_source_0_0_0_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_0_0_0_0_0.set_processor_affinity([1])
        self.blocks_complex_to_real_0_0_0 = blocks.complex_to_real(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_0_2 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 0.002, 50000, 0, 0)
        self.analog_phase_modulator_fc_0 = analog.phase_modulator_fc(1.0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, (1/1.5/100), 0)
        self.HighDataRate_Modem_Encode_RS_0 = HighDataRate_Modem.Encode_RS(1, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.HighDataRate_Modem_Encode_RS_0, 0), (self.blocks_vector_to_stream_0_1, 0))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_phase_modulator_fc_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0_2, 0), (self.blocks_vco_c_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_keep_one_in_n_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.iio_pluto_sink_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_complex_to_real_0_0_0, 0), (self.analog_phase_modulator_fc_0, 0))
        self.connect((self.blocks_file_source_0_0_0_0_0, 0), (self.blocks_stream_mux_0, 0))
        self.connect((self.blocks_file_source_0_0_0_0_0_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_keep_one_in_n_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.digital_constellation_modulator_0_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_rotator_cc_0_0, 0))
        self.connect((self.blocks_rotator_cc_0_0, 0), (self.blocks_complex_to_real_0_0_0, 0))
        self.connect((self.blocks_stream_mux_0, 0), (self.fec_extended_encoder_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_stream_to_vector_2_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0_0_1, 0), (self.blocks_stream_mux_0, 1))
        self.connect((self.blocks_stream_to_vector_2_0, 0), (self.HighDataRate_Modem_Encode_RS_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0_0_0_0_0, 0), (self.blocks_stream_to_tagged_stream_0_0_1, 0))
        self.connect((self.blocks_vco_c_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_vector_to_stream_0_1, 0), (self.blocks_unpack_k_bits_bb_0_0_0_0_0, 0))
        self.connect((self.digital_constellation_modulator_0_0, 0), (self.blocks_repeat_0, 0))
        self.connect((self.fec_extended_encoder_0, 0), (self.blocks_pack_k_bits_bb_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "TX_Doppler_Dongle_RS_CC")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_variable_cc_encoder_def_0(self):
        return self.variable_cc_encoder_def_0

    def set_variable_cc_encoder_def_0(self, variable_cc_encoder_def_0):
        self.variable_cc_encoder_def_0 = variable_cc_encoder_def_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0_2.set_sampling_freq(self.samp_rate)
        self.iio_pluto_sink_0.set_samplerate(self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, (self.samp_rate/4))
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)

    def get_constel(self):
        return self.constel

    def set_constel(self, constel):
        self.constel = constel




def main(top_block_cls=TX_Doppler_Dongle_RS_CC, options=None):

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
