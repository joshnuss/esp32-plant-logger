from temperature import TempSensor
from moisture import MoistureSensor
from logger import Logger
from led import LED
from machine import Pin, Timer, SoftI2C, RTC, SDCard
import os
import time
import micropython
import date

LOG_FREQUENCY_MS = 30000

sd = SDCard(slot=2, freq=5000000)
os.mount(sd, '/sd')

rtc = RTC()
i2c = SoftI2C(scl=Pin(14), sda=Pin(13))
temp = TempSensor(0x38, i2c)
moisture = MoistureSensor(pin=Pin(36))
led = LED()
logger = Logger(path='/sd/temp.csv')

def measure(_name):
    temp_values = temp.values
    datetime = rtc.datetime()

    logger.log([
        date.format(datetime),
        f"{temp_values['t']}°C",
        f"{temp_values['rh']}%",
        str(moisture.value)
    ])

    led.pulse()

def callback(_timer):
    micropython.schedule(measure, 'measure')

timer = Timer(0)
timer.init(period=LOG_FREQUENCY_MS, mode=Timer.PERIODIC, callback=callback)

led.pulse()

while True:
    time.sleep(1000)
