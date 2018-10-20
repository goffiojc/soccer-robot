from ev3dev2.sensor import Sensor, INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.motor import MoveTank, SpeedPercent, OUTPUT_A, OUTPUT_B, OUTPUT_D, MediumMotor


motor = MediumMotor(OUTPUT_D)
motor.on_for_seconds(100, 5)

