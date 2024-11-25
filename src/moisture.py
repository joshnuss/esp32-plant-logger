from machine import Pin, ADC

class MoistureSensor:
    def __init__(self, pin):
        pin.init(mode=Pin.IN)
        self.adc = ADC(pin)

    @property
    def measurement(self):
        return self.adc.read_u16()

