#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import numpy as np
from time import sleep
import sounddevice as sd

from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QProgressBar

class Audio(QThread):
    dbSPL = pyqtSignal(int)
    volL = 0
    volR = 0
    ofsetL = 117
    ofsetR = 115

    def rms(self,inarray,offset):
        return round(20*np.log10(np.sqrt(np.mean(np.square(inarray))))+offset,2)

    def getLevel(self, indata, frames, time, status):
        sleep(0.1)
        self.volL = self.rms(indata[:,0],self.ofsetL)
        self.volR = self.rms(indata[:,1],self.ofsetR)
        volNorm = int(np.linalg.norm(indata))
        self.dbSPL.emit(volNorm)

    def run(self):
        with sd.InputStream(callback=self.getLevel):
            print("Capture Started")
            while True:
                pass

class SLM(QDialog):

    """Docstring for SLM. """

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simple SLM')
        self.setFixedSize(480,160)

        self.lblVolL = QLabel(self)
        self.lblVolL.setText('Volume L')

        self.lblVolL0 = QLabel(self)
        self.lblVolL0.setText('0 dB')
        self.lblVolLU = QLabel(self)
        self.lblVolLU.setText('140 dB')

        self.barVolL = QProgressBar(self)
        self.barVolL.setTextVisible(False)
        self.barVolL.setFixedSize(250,25)
        self.barVolL.setMaximum(140)

        self.txtVolL = QLineEdit(self)
        self.txtVolL.setReadOnly(True)
        self.txtVolL.setFixedWidth(50)

        self.vbVolL = QHBoxLayout()
        self.vbVolL.addWidget(self.lblVolL)
        self.vbVolL.addWidget(self.txtVolL)
        self.vbVolL.addWidget(self.lblVolL0)
        self.vbVolL.addWidget(self.barVolL)
        self.vbVolL.addWidget(self.lblVolLU)
        
        self.lblVolR = QLabel(self)
        self.lblVolR.setText('Volume R')

        self.lblVolR0 = QLabel(self)
        self.lblVolR0.setText('0 dB')
        self.lblVolRU = QLabel(self)
        self.lblVolRU.setText('140 dB')

        self.barVolR = QProgressBar(self)
        self.barVolR.setTextVisible(False)
        self.barVolR.setFixedSize(250,25)
        self.barVolR.setMaximum(140)

        self.txtVolR = QLineEdit(self)
        self.txtVolR.setReadOnly(True)
        self.txtVolR.setFixedWidth(50)

        self.vbVolR = QHBoxLayout()
        self.vbVolR.addWidget(self.lblVolR)
        self.vbVolR.addWidget(self.txtVolR)
        self.vbVolR.addWidget(self.lblVolR0)
        self.vbVolR.addWidget(self.barVolR)
        self.vbVolR.addWidget(self.lblVolRU)

        self.hbVol = QVBoxLayout()
        self.hbVol.addLayout(self.vbVolL)
        self.hbVol.addLayout(self.vbVolR)

        self.setLayout(self.hbVol)

        self.show()

        sd.default.device = 2, None
        sd.default.channels = 2, None
        sd.default.samplerate = 48000
        print(sd.query_devices())

        self.spl = Audio()
        self.spl.dbSPL.connect(self.onSplchanged)
        self.spl.start()

    def onSplchanged(self,val):
        splAvg = val
        self.txtVolL.setText(str(self.spl.volL))
        self.txtVolR.setText(str(self.spl.volR))
        self.barVolL.setValue(int(self.spl.volL))
        self.barVolR.setValue(int(self.spl.volR))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wndw = SLM()
    sys.exit(app.exec_())
