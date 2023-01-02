#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.5.0

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
import sip
from gnuradio import blocks
import pmt
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import HighDataRate_Modem



from gnuradio import qtgui

class QPSK_15Mbps_TRIchain(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "QPSK_15Mbps_TRIchain")

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
        self.samp_rate = samp_rate = 15000000
        self.freq = freq = 80000000

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            256, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(1.5)
        self.qtgui_const_sink_x_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


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
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.qtgui_const_sink_x_0.set_processor_affinity([7])
        self.digital_symbol_sync_xx_0_0_0 = digital.symbol_sync_cc(
            digital.TED_GARDNER,
            2.00000,
            (6.28/50),
            1.0,
            1.0,
            1.5,
            1,
            digital.constellation_bpsk().base(),
            digital.IR_PFB_NO_MF,
            128,
            firdes.root_raised_cosine(32,64,1.0,1.0,704))
        self.digital_symbol_sync_xx_0_0_0.set_processor_affinity([6])
        self.digital_symbol_sync_xx_0_0 = digital.symbol_sync_cc(
            digital.TED_GARDNER,
            2.00000,
            (6.28/50),
            1.0,
            1.0,
            1.5,
            1,
            digital.constellation_bpsk().base(),
            digital.IR_PFB_NO_MF,
            128,
            firdes.root_raised_cosine(32,64,1.0,1.0,704))
        self.digital_symbol_sync_xx_0_0.set_processor_affinity([5])
        self.digital_symbol_sync_xx_0 = digital.symbol_sync_cc(
            digital.TED_GARDNER,
            2.000000,
            (6.28/50),
            1.0,
            1.0,
            1.5,
            1,
            digital.constellation_bpsk().base(),
            digital.IR_PFB_NO_MF,
            128,
            firdes.root_raised_cosine(32,64,1.0,1.0,704))
        self.digital_symbol_sync_xx_0.set_processor_affinity([4])
        self.digital_costas_loop_cc_0_0_0 = digital.costas_loop_cc((3.14159/40), 4, False)
        self.digital_costas_loop_cc_0_0_0.set_processor_affinity([6])
        self.digital_costas_loop_cc_0_0 = digital.costas_loop_cc((3.14159/40), 4, False)
        self.digital_costas_loop_cc_0_0.set_processor_affinity([5])
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc((3.14159/40), 4, False)
        self.digital_costas_loop_cc_0.set_processor_affinity([4])
        self.digital_binary_slicer_fb_0_0_0_0 = digital.binary_slicer_fb()
        self.digital_binary_slicer_fb_0_0_0_0.set_processor_affinity([7])
        self.digital_binary_slicer_fb_0_0_0 = digital.binary_slicer_fb()
        self.digital_binary_slicer_fb_0_0_0.set_processor_affinity([7])
        self.digital_binary_slicer_fb_0_0 = digital.binary_slicer_fb()
        self.digital_binary_slicer_fb_0_0.set_processor_affinity([7])
        self.blocks_throttle_0_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0_0_0.set_processor_affinity([1])
        self.blocks_stream_mux_2 = blocks.stream_mux(gr.sizeof_char*1, (82510,82510,82510))
        self.blocks_stream_mux_2.set_processor_affinity([7])
        self.blocks_stream_mux_0_1 = blocks.stream_mux(gr.sizeof_gr_complex*1, (1524, 82000))
        self.blocks_stream_mux_0_1.set_processor_affinity([2])
        self.blocks_stream_mux_0_1.set_min_output_buffer(85048)
        self.blocks_stream_mux_0_0 = blocks.stream_mux(gr.sizeof_gr_complex*1, (1524, 82000))
        self.blocks_stream_mux_0_0.set_processor_affinity([2])
        self.blocks_stream_mux_0_0.set_min_output_buffer(85048)
        self.blocks_stream_mux_0 = blocks.stream_mux(gr.sizeof_gr_complex*1, (1524, 82000))
        self.blocks_stream_mux_0.set_processor_affinity([2])
        self.blocks_stream_mux_0.set_min_output_buffer(85048)
        self.blocks_skiphead_0_0 = blocks.skiphead(gr.sizeof_gr_complex*1, 140000)
        self.blocks_skiphead_0_0.set_processor_affinity([2])
        self.blocks_skiphead_0_0.set_min_output_buffer((140000*2))
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_gr_complex*1, 70000)
        self.blocks_skiphead_0.set_processor_affinity([2])
        self.blocks_skiphead_0.set_min_output_buffer((140000*2))
        self.blocks_keep_m_in_n_0_1 = blocks.keep_m_in_n(gr.sizeof_char, 74270, 82510, 8240)
        self.blocks_keep_m_in_n_0_1.set_processor_affinity([3])
        self.blocks_keep_m_in_n_0_0_0 = blocks.keep_m_in_n(gr.sizeof_gr_complex, 82000, 210000, 0)
        self.blocks_keep_m_in_n_0_0_0.set_processor_affinity([2])
        self.blocks_keep_m_in_n_0_0_0.set_min_output_buffer((82000*2))
        self.blocks_keep_m_in_n_0_0 = blocks.keep_m_in_n(gr.sizeof_gr_complex, 82000, 210000, 0)
        self.blocks_keep_m_in_n_0_0.set_processor_affinity([2])
        self.blocks_keep_m_in_n_0_0.set_min_output_buffer((82000*2))
        self.blocks_keep_m_in_n_0 = blocks.keep_m_in_n(gr.sizeof_gr_complex, 82000, 210000, 0)
        self.blocks_keep_m_in_n_0.set_processor_affinity([2])
        self.blocks_keep_m_in_n_0.set_min_output_buffer((82000*2))
        self.blocks_interleave_0_0_0 = blocks.interleave(gr.sizeof_float*1, 1)
        self.blocks_interleave_0_0_0.set_processor_affinity([4])
        self.blocks_interleave_0_0 = blocks.interleave(gr.sizeof_float*1, 1)
        self.blocks_interleave_0_0.set_processor_affinity([4])
        self.blocks_interleave_0 = blocks.interleave(gr.sizeof_float*1, 1)
        self.blocks_interleave_0.set_processor_affinity([4])
        self.blocks_file_source_0_0_0_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/davem/gr-HighDataRate_Modem/examples/3048QPSK_PREamble_COMPLEX', True, 0, 0)
        self.blocks_file_source_0_0_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_0_0_0_0.set_processor_affinity([2])
        self.blocks_file_source_0_0_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/davem/gr-HighDataRate_Modem/examples/QPSK_Generate_Modulator_Files/4192BBFileModQPSK_inCOMPLEX_with32ASM', False, 0, 0)
        self.blocks_file_source_0_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_0_0_0.set_processor_affinity([1])
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, '/home/davem/gr-HighDataRate_Modem/examples/FINAL_OUTPUT_FRAMES_ONLY', False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0_0.set_processor_affinity([3])
        self.blocks_complex_to_float_0_0_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0_0_0.set_processor_affinity([4])
        self.blocks_complex_to_float_0_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0_0.set_processor_affinity([4])
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0.set_processor_affinity([4])
        self.HighDataRate_Modem_Tag_FrameASM_0 = HighDataRate_Modem.Tag_FrameASM()
        self.HighDataRate_Modem_Tag_FrameASM_0.set_processor_affinity([3])
        self.HighDataRate_Modem_TAG_CHUNKpreamble_0_1 = HighDataRate_Modem.TAG_CHUNKpreamble()
        self.HighDataRate_Modem_TAG_CHUNKpreamble_0_1.set_processor_affinity([7])
        self.HighDataRate_Modem_TAG_CHUNKpreamble_0_0 = HighDataRate_Modem.TAG_CHUNKpreamble()
        self.HighDataRate_Modem_TAG_CHUNKpreamble_0_0.set_processor_affinity([7])
        self.HighDataRate_Modem_TAG_CHUNKpreamble_0 = HighDataRate_Modem.TAG_CHUNKpreamble()
        self.HighDataRate_Modem_TAG_CHUNKpreamble_0.set_processor_affinity([7])
        self.HighDataRate_Modem_Resolve_Phase_1 = HighDataRate_Modem.Resolve_Phase(4192, 120000)
        self.HighDataRate_Modem_Resolve_Phase_1.set_processor_affinity([3])
        self.HighDataRate_Modem_Frame_Extract_0 = HighDataRate_Modem.Frame_Extract(4192, 30000)
        self.HighDataRate_Modem_Frame_Extract_0.set_processor_affinity([3])
        self.HighDataRate_Modem_Chunk_ExtractQPSK_0_1 = HighDataRate_Modem.Chunk_ExtractQPSK()
        self.HighDataRate_Modem_Chunk_ExtractQPSK_0_1.set_processor_affinity([7])
        self.HighDataRate_Modem_Chunk_ExtractQPSK_0_0 = HighDataRate_Modem.Chunk_ExtractQPSK()
        self.HighDataRate_Modem_Chunk_ExtractQPSK_0_0.set_processor_affinity([7])
        self.HighDataRate_Modem_Chunk_ExtractQPSK_0 = HighDataRate_Modem.Chunk_ExtractQPSK()
        self.HighDataRate_Modem_Chunk_ExtractQPSK_0.set_processor_affinity([7])


        ##################################################
        # Connections
        ##################################################
        self.connect((self.HighDataRate_Modem_Chunk_ExtractQPSK_0, 0), (self.blocks_stream_mux_2, 0))
        self.connect((self.HighDataRate_Modem_Chunk_ExtractQPSK_0_0, 0), (self.blocks_stream_mux_2, 1))
        self.connect((self.HighDataRate_Modem_Chunk_ExtractQPSK_0_1, 0), (self.blocks_stream_mux_2, 2))
        self.connect((self.HighDataRate_Modem_Frame_Extract_0, 0), (self.HighDataRate_Modem_Resolve_Phase_1, 0))
        self.connect((self.HighDataRate_Modem_Resolve_Phase_1, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.HighDataRate_Modem_TAG_CHUNKpreamble_0, 0), (self.HighDataRate_Modem_Chunk_ExtractQPSK_0, 0))
        self.connect((self.HighDataRate_Modem_TAG_CHUNKpreamble_0_0, 0), (self.HighDataRate_Modem_Chunk_ExtractQPSK_0_0, 0))
        self.connect((self.HighDataRate_Modem_TAG_CHUNKpreamble_0_1, 0), (self.HighDataRate_Modem_Chunk_ExtractQPSK_0_1, 0))
        self.connect((self.HighDataRate_Modem_Tag_FrameASM_0, 0), (self.HighDataRate_Modem_Frame_Extract_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_interleave_0, 1))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_interleave_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.blocks_interleave_0_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 1), (self.blocks_interleave_0_0, 1))
        self.connect((self.blocks_complex_to_float_0_0_0, 1), (self.blocks_interleave_0_0_0, 1))
        self.connect((self.blocks_complex_to_float_0_0_0, 0), (self.blocks_interleave_0_0_0, 0))
        self.connect((self.blocks_file_source_0_0_0, 0), (self.blocks_throttle_0_0_0, 0))
        self.connect((self.blocks_file_source_0_0_0_0, 0), (self.blocks_stream_mux_0, 0))
        self.connect((self.blocks_file_source_0_0_0_0, 0), (self.blocks_stream_mux_0_0, 0))
        self.connect((self.blocks_file_source_0_0_0_0, 0), (self.blocks_stream_mux_0_1, 0))
        self.connect((self.blocks_interleave_0, 0), (self.digital_binary_slicer_fb_0_0, 0))
        self.connect((self.blocks_interleave_0_0, 0), (self.digital_binary_slicer_fb_0_0_0, 0))
        self.connect((self.blocks_interleave_0_0_0, 0), (self.digital_binary_slicer_fb_0_0_0_0, 0))
        self.connect((self.blocks_keep_m_in_n_0, 0), (self.blocks_stream_mux_0_0, 1))
        self.connect((self.blocks_keep_m_in_n_0_0, 0), (self.blocks_stream_mux_0, 1))
        self.connect((self.blocks_keep_m_in_n_0_0_0, 0), (self.blocks_stream_mux_0_1, 1))
        self.connect((self.blocks_keep_m_in_n_0_1, 0), (self.HighDataRate_Modem_Tag_FrameASM_0, 0))
        self.connect((self.blocks_skiphead_0, 0), (self.blocks_keep_m_in_n_0_0, 0))
        self.connect((self.blocks_skiphead_0_0, 0), (self.blocks_keep_m_in_n_0_0_0, 0))
        self.connect((self.blocks_stream_mux_0, 0), (self.digital_symbol_sync_xx_0_0, 0))
        self.connect((self.blocks_stream_mux_0_0, 0), (self.digital_symbol_sync_xx_0, 0))
        self.connect((self.blocks_stream_mux_0_1, 0), (self.digital_symbol_sync_xx_0_0_0, 0))
        self.connect((self.blocks_stream_mux_2, 0), (self.blocks_keep_m_in_n_0_1, 0))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.blocks_keep_m_in_n_0, 0))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.blocks_skiphead_0_0, 0))
        self.connect((self.digital_binary_slicer_fb_0_0, 0), (self.HighDataRate_Modem_TAG_CHUNKpreamble_0, 0))
        self.connect((self.digital_binary_slicer_fb_0_0_0, 0), (self.HighDataRate_Modem_TAG_CHUNKpreamble_0_0, 0))
        self.connect((self.digital_binary_slicer_fb_0_0_0_0, 0), (self.HighDataRate_Modem_TAG_CHUNKpreamble_0_1, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0, 0), (self.blocks_complex_to_float_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0_0, 0), (self.blocks_complex_to_float_0_0_0, 0))
        self.connect((self.digital_symbol_sync_xx_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.digital_symbol_sync_xx_0_0, 0), (self.digital_costas_loop_cc_0_0, 0))
        self.connect((self.digital_symbol_sync_xx_0_0_0, 0), (self.digital_costas_loop_cc_0_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "QPSK_15Mbps_TRIchain")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0_0_0.set_sample_rate(self.samp_rate)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq




def main(top_block_cls=QPSK_15Mbps_TRIchain, options=None):

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
