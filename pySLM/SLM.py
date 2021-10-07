#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import numpy as np
import sounddevice as sd

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QLabel, QVBoxLayout

class Audio(QThread):
    dbSPL = pyqtSignal(int)
    volNormL = 0
    volNormR = 0
    gain = 1

    def getLevel(self, indata, frames, time, status):
        self.volNormL = int(np.linalg.norm(indata[:,0]))*self.gain
        self.volNormR = int(np.linalg.norm(indata[:,1]))*self.gain
        volNorm = int(np.linalg.norm(indata))*self.gain
        self.dbSPL.emit(volNorm)

    def run(self):
        with sd.InputStream(callback=self.getLevel):
            print("Capture Started")
            while True:
                pass
            print("Capture Stopped")

class SLM(QDialog):

    """Docstring for SLM. """

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simple SLM')

        self.lblVolL = QLabel(self)
        self.lblVolL.setText('Volume L')

        self.txtVolL = QLineEdit(self)

        self.lblVolR = QLabel(self)
        self.lblVolR.setText('Volume R')

        self.txtVolR = QLineEdit(self)

        self.vbVol = QVBoxLayout()
        self.vbVol.addWidget(self.lblVolL)
        self.vbVol.addWidget(self.txtVolL)
        self.vbVol.addWidget(self.lblVolR)
        self.vbVol.addWidget(self.txtVolR)

        self.setLayout(self.vbVol)

        self.show()

        sd.default.device = 2, None
        sd.default.channels = 2, None
        print(sd.query_devices())

        self.spl = Audio()
        self.spl.dbSPL.connect(self.onSplchanged)
        self.spl.start()

    def onSplchanged(self,val):
        splAvg = val
        self.txtVolL.setText(str(self.spl.volNormL))
        self.txtVolR.setText(str(self.spl.volNormR))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wndw = SLM()
    sys.exit(app.exec_())
