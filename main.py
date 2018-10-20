#!/usr/bin/env python3
from ev3dev2.sensor import Sensor, INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.motor import MoveTank, SpeedPercent, OUTPUT_A, OUTPUT_B, OUTPUT_D, OUTPUT_C, Motor

# Definition of variable

off = TouchSensor(INPUT_2)
tank = MoveTank(OUTPUT_A, OUTPUT_B)
roller = Motor(OUTPUT_C)

power = 40
section = 30
max = 100
min = -100
roller.on(-100)


def getIrValue():
    ir = Sensor(address="i2c-legoev33:i2c8")
    return ir.value()


def getConvertedIrValue():
    return (getIrValue() - 5) * section


def controlSpeed(motor):
    if motor < min:
        return min
    if motor > max:
        return max
    return motor


def controlTheBall():
    roller.on_for_seconds(100, 30)


def followTheBall():
    tank.on(SpeedPercent(controlSpeed(power - getConvertedIrValue()).__str__()), SpeedPercent(controlSpeed(power + getConvertedIrValue()).__str__()))



# Main
while off.is_released:
    followTheBall()
    if off.is_pressed:
        tank.off()
        roller.off()




