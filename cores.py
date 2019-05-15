#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import ColorSensor
# declaração do sensor
sensordecor=ColorSensor(INPUT_1)
#declaração de uma lista vazia para receber as cores já lidas
cores = []
while True:
    #entrada no loop de leitura
    cor = sensordecor.color_name
    #adição da cor vista a lista caso ela não seja repetida
    if cor not in cores:
        cores.append(cor)
        #se cor nova,adicionar tomada de decisão para direção por tentativa e erro
    else :
        #if cor == 'White':
        #continuar função caminho
        print("Cor já vista")
        #repetir a decisão descoberta na primeira etapa
    print('A cor atual é ',cor)
    #printar a lista de cores obtida
    for i in len(cores):
        print(cores[i])
    #parada
    a = str(input("De novo? "))
    if (a == 'N'):
        break
