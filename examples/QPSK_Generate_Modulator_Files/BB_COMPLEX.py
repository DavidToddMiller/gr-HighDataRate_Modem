#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: BB_COMPLEX
# GNU Radio version: 3.10.1.1

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

from gnuradio import blocks
import pmt
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation



from gnuradio import qtgui

class BB_COMPLEX(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "BB_COMPLEX", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("BB_COMPLEX")
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

        self.settings = Qt.QSettings("GNU Radio", "BB_COMPLEX")

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
        self.samp_rate = samp_rate = 5000000

        ##################################################
        # Blocks
        ##################################################
        self.blocks_throttle_0_0_0_1 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_repeat_0_0_1 = blocks.repeat(gr.sizeof_float*1, 2)
        self.blocks_repeat_0_0 = blocks.repeat(gr.sizeof_float*1, 2)
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_ff(2)
        self.blocks_keep_m_in_n_0_0_0 = blocks.keep_m_in_n(gr.sizeof_float, 1, 2, 1)
        self.blocks_keep_m_in_n_0_0 = blocks.keep_m_in_n(gr.sizeof_float, 1, 2, 0)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0_0_0_0_1 = blocks.file_source(gr.sizeof_char*1, '/home/davem/gr-HighDataRate_Modem/examples/QPSK_Generate_Modulator_Files/BBFileModQPSK__CCSDS_32ASM', False, 0, 0)
        self.blocks_file_source_0_0_0_0_1.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_0_0_0_0_1.set_processor_affinity([0])
        self.blocks_file_sink_0_0_0_0_0_1 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/davem/gr-HighDataRate_Modem/examples/QPSK_Generate_Modulator_Files/4192BBFileModQPSK_inCOMPLEX_with32ASM', False)
        self.blocks_file_sink_0_0_0_0_0_1.set_unbuffered(False)
        self.blocks_file_sink_0_0_0_0_0_1.set_processor_affinity([7])
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blocks_add_const_vxx_0_0 = blocks.add_const_ff(-1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.blocks_keep_m_in_n_0_0, 0))
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.blocks_keep_m_in_n_0_0_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_multiply_const_vxx_1_0, 0))
        self.connect((self.blocks_file_source_0_0_0_0_1, 0), (self.blocks_throttle_0_0_0_1, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_file_sink_0_0_0_0_0_1, 0))
        self.connect((self.blocks_keep_m_in_n_0_0, 0), (self.blocks_repeat_0_0, 0))
        self.connect((self.blocks_keep_m_in_n_0_0_0, 0), (self.blocks_repeat_0_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_add_const_vxx_0_0, 0))
        self.connect((self.blocks_repeat_0_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_repeat_0_0_1, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_throttle_0_0_0_1, 0), (self.blocks_char_to_float_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "BB_COMPLEX")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0_0_0_1.set_sample_rate(self.samp_rate)




def main(top_block_cls=BB_COMPLEX, options=None):

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
