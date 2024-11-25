from machine import Pin, PWM
import time

class LED:
    def __init__(self, pin=2, freq=10, duration=500):
        self.pin = Pin(pin, mode=Pin.OUT)
        self.freq = freq
        self.duration = duration

    def flicker(self):
        pwm = PWM(self.pin, freq=self.freq)
        time.sleep_ms(self.duration)
        pwm.deinit()

