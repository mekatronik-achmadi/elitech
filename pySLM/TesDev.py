#!/usr/bin/python3

import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 48000
RECORD_SECONDS = 2
INPUT_DEVICE_INDEX = 2

p = pyaudio.PyAudio()

print(p.get_device_info_by_index(INPUT_DEVICE_INDEX))
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index=INPUT_DEVICE_INDEX,
                frames_per_buffer=CHUNK)
