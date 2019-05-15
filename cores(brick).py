#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import ColorSensor
# declaracao do sensor
sensordecor=ColorSensor(INPUT_1)
while True:
    #entrada no loop de leitura
    #imprime na tela o codigo da cor seguido de seu nome
    print(sensordecor.color, "---", sensordecor.color_name)
    #sai do loop se nao ver nenhuma cor
    if sensordecor.color == 0:
        break
