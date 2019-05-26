#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_1 #mudar para input e outputs corretos
from ev3dev2.sensor.lego import UltrasonicSensor
#importacao da biblioteca de motores
from ev3dev2.motor import LargeMotor, OUTPUT_A,SpeedPercent
from ev3dev2.button import Button
# declaracao dos sensores

ultrasonico = UltrasonicSensor(INPUT_1) #ultrasonico na frente, que verifica a distância ate o boneco


motorgarra = LargeMotor(OUTPUT_A)   #motor da garra

distancia = motorgarra.distance_centimeters()
x = 5 #valor arbitrario de distancia, medida entre o boneco e a garra

if (distancia < x): #pegar o boneco
    motorgarra.on_for_rotations(SpeedPercent(100), 7)
    motorgarra.holding()#comando que faz o motor fazer o hold do boneco

buttons = [] #lista vazia para verificação se algum botao foi pressionado

if (buttons_pressed() != buttons):#soltar o boneco via press de botão
    motorgarra.stop()
    motorgarra.on_for_rotations(SpeedPercent(-100), 7)
    motorgarra.stop()
    

#adicionar caso de parada, combinando esse codigo com o de cores
#if cor = Black, andar mais e verificar se vê preto ou NoColor
#caso preto > Largar o boneco
#caso NoColor ele teria que retornar no caminho, pois seria um dos caminhos via tentativa e erro que eh um beco sem saida