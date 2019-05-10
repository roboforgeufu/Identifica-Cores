#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import ColorSensor
# declaração do sensor
sensordecor=ColorSensor(INPUT_1)
while True:
    #entrada no loop de leitura
    print(sensordecor.color_name)
    #parada
    a = str(input("De novo? "))
    if (a == 'N'):
        break
