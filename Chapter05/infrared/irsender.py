import time
import json
import os

import pigpio # http://abyz.co.uk/rpi/pigpio/python.html

# Class for sending infrared signals
# Based on pigpio irrp

class IRSender:

    # Class settings
    GLITCH     = 100                                    # glitch us
    PRE_MS     = 200                                    # preamble ms
    POST_MS    = 15                                     # postamble ms
    FREQ       = 38.0                                   # frequency kHz
    SHORT      = 10                                     # short code length
    GAP_MS     = 100                                    # key gap ms
    NO_CONFIRM = False                                  # No confirm needed
    TOLERANCE  = 15                                     # tolerance percentage

    POST_US    = POST_MS * 1000
    PRE_US     = PRE_MS  * 1000
    GAP_S      = GAP_MS  / 1000.0
    CONFIRM    = not NO_CONFIRM
    TOLER_MIN =  (100 - TOLERANCE) / 100.0
    TOLER_MAX =  (100 + TOLERANCE) / 100.0

    def __init__(self, filename, gpio=17):
        self.last_tick = 0
        self.in_code = False
        self.code = []
        self.fetching_code = False
        self.filename = filename
        self.gpio = gpio

        self.pi = pigpio.pi() # Connect to pigpiod

        try:
            f = open(self.filename, "r")
        except:
            print("Can't open: {}".format(self.filename))
            return

        self.records = json.load(f)
        f.close()

        self.pi.set_mode(self.gpio, pigpio.OUTPUT) # IR TX connected to this GPIO.
        self.pi.wave_add_new()

    def connected(self):
        return self.pi.connected

    def carrier(self, gpio, frequency, micros):
        """
        Generate carrier square wave.
        """
        wf = []
        cycle = 1000.0 / frequency
        cycles = int(round(micros/cycle))
        on = int(round(cycle / 2.0))
        sofar = 0
        for c in range(cycles):
            target = int(round((c+1)*cycle))
            sofar += on
            off = target - sofar
            sofar += off
            wf.append(pigpio.pulse(1<<gpio, 0, on))
            wf.append(pigpio.pulse(0, 1<<gpio, off))
        return wf

    def send_code (self, code_ref):
        emit_time = time.time()

        if code_ref in self.records:
            self.code = self.records[code_ref]
            # Create wave
            marks_wid = {}
            spaces_wid = {}
            wave = [0]*len(self.code)
            for i in range(0, len(self.code)):
                ci = self.code[i]
                if i & 1: # Space
                    if ci not in spaces_wid:
                        self.pi.wave_add_generic([pigpio.pulse(0, 0, ci)])
                        spaces_wid[ci] = self.pi.wave_create()
                    wave[i] = spaces_wid[ci]
                else: # Mark
                    if ci not in marks_wid:
                        wf = self.carrier(self.gpio, IRSender.FREQ, ci)
                        self.pi.wave_add_generic(wf)
                        marks_wid[ci] = self.pi.wave_create()
                    wave[i] = marks_wid[ci]

            delay = emit_time - time.time()

            if delay > 0.0:
                time.sleep(delay)
            self.pi.wave_chain(wave)

            while self.pi.wave_tx_busy():
                time.sleep(0.002)

            emit_time = time.time() + IRSender.GAP_S

            for i in marks_wid:
                self.pi.wave_delete(marks_wid[i])

            marks_wid = {}

            for i in spaces_wid:
                self.pi.wave_delete(spaces_wid[i])

            spaces_wid = {}
        else:
            print("Id {} not found".format(this_code))


    def close(self):
        self.pi.stop() # Disconnect from Pi.
