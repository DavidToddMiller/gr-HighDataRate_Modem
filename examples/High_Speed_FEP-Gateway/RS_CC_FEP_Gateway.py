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
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
import pmt
from gnuradio import ccsds_rs
from gnuradio import fec
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import zeromq
import HighDataRate_Modem



from gnuradio import qtgui

class RS_CC_FEP_Gateway(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "RS_CC_FEP_Gateway")

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
        self.variable_cc_decoder_def_0 = variable_cc_decoder_def_0 = fec.cc_decoder.make(2048,7, 2, [79,-109], 0, (-1), fec.CC_STREAMING, False)
        self.samp_rate = samp_rate = 24000000

        ##################################################
        # Blocks
        ##################################################
        self.zeromq_push_sink_0 = zeromq.push_sink(gr.sizeof_char, 1, 'tcp://127.0.0.1:5555', 100, False, (-1))
        self.zeromq_push_sink_0.set_processor_affinity([0])
        self.zeromq_pull_source_0 = zeromq.pull_source(gr.sizeof_char, 1, 'tcp://127.0.0.1:5555', 100, False, (-1))
        self.zeromq_pull_source_0.set_processor_affinity([0])
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
            128, #size
            samp_rate, #samp_rate
            'My Decode Block Output', #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(1.0)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-1, 2)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0.enable_stem_plot(False)


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


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_win)
        self.qtgui_time_sink_x_0_0_0.set_processor_affinity([0])
        self.fec_extended_decoder_0 = fec.extended_decoder(decoder_obj_list=variable_cc_decoder_def_0, threading='capillary', ann=None, puncpat='11', integration_period=10000)
        self.fec_extended_decoder_0.set_processor_affinity([3])
        self.ccsds_rs_decode_rs_test_0_0_1 = ccsds_rs.decode_rs_test(1, 1)
        self.ccsds_rs_decode_rs_test_0_0_1.set_processor_affinity([5])
        self.ccsds_rs_decode_rs_test_0_0_0_0 = ccsds_rs.decode_rs_test(1, 1)
        self.ccsds_rs_decode_rs_test_0_0_0_0.set_processor_affinity([7])
        self.ccsds_rs_decode_rs_test_0_0_0 = ccsds_rs.decode_rs_test(1, 1)
        self.ccsds_rs_decode_rs_test_0_0_0.set_processor_affinity([6])
        self.ccsds_rs_decode_rs_test_0_0 = ccsds_rs.decode_rs_test(1, 1)
        self.ccsds_rs_decode_rs_test_0_0.set_processor_affinity([4])
        self.blocks_vector_to_stream_0_1_0_2_0 = blocks.vector_to_stream(gr.sizeof_char*1, 223)
        self.blocks_vector_to_stream_0_1_0_2_0.set_processor_affinity([7])
        self.blocks_vector_to_stream_0_1_0_2 = blocks.vector_to_stream(gr.sizeof_char*1, 223)
        self.blocks_vector_to_stream_0_1_0_2.set_processor_affinity([6])
        self.blocks_vector_to_stream_0_1_0_1 = blocks.vector_to_stream(gr.sizeof_char*1, 223)
        self.blocks_vector_to_stream_0_1_0_1.set_processor_affinity([5])
        self.blocks_vector_to_stream_0_1_0_0 = blocks.vector_to_stream(gr.sizeof_char*1, 223)
        self.blocks_vector_to_stream_0_1_0_0.set_processor_affinity([4])
        self.blocks_unpack_k_bits_bb_0_0_0_0_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_unpack_k_bits_bb_0_0_0_0_0.set_processor_affinity([0])
        self.blocks_throttle_0_0_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_throttle_0_0_0.set_processor_affinity([0])
        self.blocks_tag_gate_0 = blocks.tag_gate(gr.sizeof_char * 1, False)
        self.blocks_tag_gate_0.set_single_key("")
        self.blocks_stream_to_vector_2_0_0_2_0 = blocks.stream_to_vector(gr.sizeof_char*1, 255)
        self.blocks_stream_to_vector_2_0_0_2_0.set_processor_affinity([7])
        self.blocks_stream_to_vector_2_0_0_2 = blocks.stream_to_vector(gr.sizeof_char*1, 255)
        self.blocks_stream_to_vector_2_0_0_2.set_processor_affinity([6])
        self.blocks_stream_to_vector_2_0_0_1 = blocks.stream_to_vector(gr.sizeof_char*1, 255)
        self.blocks_stream_to_vector_2_0_0_1.set_processor_affinity([5])
        self.blocks_stream_to_vector_2_0_0_0 = blocks.stream_to_vector(gr.sizeof_char*1, 255)
        self.blocks_stream_to_vector_2_0_0_0.set_processor_affinity([4])
        self.blocks_stream_mux_0 = blocks.stream_mux(gr.sizeof_char*1, (223, 223, 223, 223))
        self.blocks_stream_mux_0.set_processor_affinity([0])
        self.blocks_stream_demux_0_0 = blocks.stream_demux(gr.sizeof_char*1, (32,2040))
        self.blocks_stream_demux_0_0.set_processor_affinity([2])
        self.blocks_stream_demux_0 = blocks.stream_demux(gr.sizeof_char*1, (255,255,255,255))
        self.blocks_stream_demux_0.set_processor_affinity([2])
        self.blocks_pack_k_bits_bb_0_0 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0_0.set_processor_affinity([2])
        self.blocks_null_sink_1 = blocks.null_sink(gr.sizeof_char*1)
        self.blocks_null_sink_1.set_processor_affinity([1])
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(2)
        self.blocks_multiply_const_vxx_0.set_processor_affinity([1])
        self.blocks_file_source_0_0_0_0_0_0 = blocks.file_source(gr.sizeof_char*1, '/home/davem/gr-HighDataRate_Modem/examples/High_Speed_FEP-Gateway/Pre_RS_CC_encoded', True, 0, 0)
        self.blocks_file_source_0_0_0_0_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_0_0_0_0_0_0.set_processor_affinity([0])
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/davem/gr-HighDataRate_Modem/examples/High_Speed_FEP-Gateway/CCSDS_HighSpeed_RS_SINK', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_file_sink_0.set_processor_affinity([0])
        self.blocks_char_to_float_0_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_0_0.set_processor_affinity([0])
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff((-1))
        self.blocks_add_const_vxx_0.set_processor_affinity([1])
        self.HighDataRate_Modem_Tag_FrameASM_0 = HighDataRate_Modem.Tag_FrameASM()
        self.HighDataRate_Modem_Tag_FrameASM_0.set_processor_affinity([2])
        self.HighDataRate_Modem_Resolve_Phase_0 = HighDataRate_Modem.Resolve_Phase(2072, 60000)
        self.HighDataRate_Modem_Resolve_Phase_0.set_processor_affinity([2])
        self.HighDataRate_Modem_Frame_Extract_0 = HighDataRate_Modem.Frame_Extract(2072, 15000)
        self.HighDataRate_Modem_Frame_Extract_0.set_processor_affinity([2])


        ##################################################
        # Connections
        ##################################################
        self.connect((self.HighDataRate_Modem_Frame_Extract_0, 0), (self.HighDataRate_Modem_Resolve_Phase_0, 0))
        self.connect((self.HighDataRate_Modem_Resolve_Phase_0, 0), (self.blocks_stream_demux_0_0, 0))
        self.connect((self.HighDataRate_Modem_Tag_FrameASM_0, 0), (self.HighDataRate_Modem_Frame_Extract_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.fec_extended_decoder_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_char_to_float_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.blocks_file_source_0_0_0_0_0_0, 0), (self.blocks_unpack_k_bits_bb_0_0_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0_0, 0), (self.blocks_stream_demux_0, 0))
        self.connect((self.blocks_stream_demux_0, 0), (self.blocks_stream_to_vector_2_0_0_0, 0))
        self.connect((self.blocks_stream_demux_0, 1), (self.blocks_stream_to_vector_2_0_0_1, 0))
        self.connect((self.blocks_stream_demux_0, 2), (self.blocks_stream_to_vector_2_0_0_2, 0))
        self.connect((self.blocks_stream_demux_0, 3), (self.blocks_stream_to_vector_2_0_0_2_0, 0))
        self.connect((self.blocks_stream_demux_0_0, 0), (self.blocks_null_sink_1, 0))
        self.connect((self.blocks_stream_demux_0_0, 1), (self.blocks_pack_k_bits_bb_0_0, 0))
        self.connect((self.blocks_stream_mux_0, 0), (self.blocks_char_to_float_0_0_0, 0))
        self.connect((self.blocks_stream_mux_0, 0), (self.zeromq_push_sink_0, 0))
        self.connect((self.blocks_stream_to_vector_2_0_0_0, 0), (self.ccsds_rs_decode_rs_test_0_0, 0))
        self.connect((self.blocks_stream_to_vector_2_0_0_1, 0), (self.ccsds_rs_decode_rs_test_0_0_1, 0))
        self.connect((self.blocks_stream_to_vector_2_0_0_2, 0), (self.ccsds_rs_decode_rs_test_0_0_0, 0))
        self.connect((self.blocks_stream_to_vector_2_0_0_2_0, 0), (self.ccsds_rs_decode_rs_test_0_0_0_0, 0))
        self.connect((self.blocks_tag_gate_0, 0), (self.HighDataRate_Modem_Tag_FrameASM_0, 0))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0_0_0_0_0, 0), (self.blocks_throttle_0_0_0, 0))
        self.connect((self.blocks_vector_to_stream_0_1_0_0, 0), (self.blocks_stream_mux_0, 0))
        self.connect((self.blocks_vector_to_stream_0_1_0_1, 0), (self.blocks_stream_mux_0, 1))
        self.connect((self.blocks_vector_to_stream_0_1_0_2, 0), (self.blocks_stream_mux_0, 2))
        self.connect((self.blocks_vector_to_stream_0_1_0_2_0, 0), (self.blocks_stream_mux_0, 3))
        self.connect((self.ccsds_rs_decode_rs_test_0_0, 0), (self.blocks_vector_to_stream_0_1_0_0, 0))
        self.connect((self.ccsds_rs_decode_rs_test_0_0_0, 0), (self.blocks_vector_to_stream_0_1_0_2, 0))
        self.connect((self.ccsds_rs_decode_rs_test_0_0_0_0, 0), (self.blocks_vector_to_stream_0_1_0_2_0, 0))
        self.connect((self.ccsds_rs_decode_rs_test_0_0_1, 0), (self.blocks_vector_to_stream_0_1_0_1, 0))
        self.connect((self.fec_extended_decoder_0, 0), (self.blocks_tag_gate_0, 0))
        self.connect((self.zeromq_pull_source_0, 0), (self.blocks_file_sink_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "RS_CC_FEP_Gateway")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_variable_cc_decoder_def_0(self):
        return self.variable_cc_decoder_def_0

    def set_variable_cc_decoder_def_0(self, variable_cc_decoder_def_0):
        self.variable_cc_decoder_def_0 = variable_cc_decoder_def_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0_0_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.samp_rate)




def main(top_block_cls=RS_CC_FEP_Gateway, options=None):

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
