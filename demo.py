#!/usr/bin/env python3
from ev3dev2.sensor import Sensor
from ev3dev2.sound import Sound

def getIrValue():
    ir = Sensor(address="i2c-legoev33:i2c8")
    return ir.value()

Sound().speak(getIrValue().__str__())

