from dht20 import DHT20
from moisture import MoistureSensor
from machine import Pin, Timer, SoftI2C, RTC, SDCard, PWM
import os
import time
import micropython

rtc = RTC()
i2c = SoftI2C(scl=Pin(14), sda=Pin(13))
temp = DHT20(0x38, i2c)
moisture = MoistureSensor(pin=Pin(36))
led = Pin(2, mode=Pin.OUT)
sd = SDCard(slot=2, freq=5000000)
os.mount(sd, '/sd')

def flicker():
    pwm = PWM(led, freq=10)
    time.sleep_ms(500)
    pwm.deinit()

def format_date(date):
    return f"{date[0]:04}-{date[1]:02}-{date[2]:02} {date[4]:02}:{date[5]:02}:{date[6]:02}"

def measure(_name):
    temp_values = temp.measurements
    moisture_value = moisture.measurement
    date = rtc.datetime()

    file = open('/sd/temp.csv', 'a')
    file.write(f"{format_date(date)},{temp_values['t']}°C,{temp_values['rh']}%,{moisture_value}\n")
    file.close()

    flicker()

def callback(_timer):
    micropython.schedule(measure, 'measure')

timer = Timer(0)
timer.init(period=30000, mode=Timer.PERIODIC, callback=callback)

flicker()

while True:
    time.sleep(1000)

