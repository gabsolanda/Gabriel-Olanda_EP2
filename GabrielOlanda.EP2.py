# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:10:52 2015

@author: Gabriel Olanda
"""
from random import choice

import turtle               # Iniciando e importando a biblioteca Turtle
window = turtle.Screen()    # Criando uma janela para a função Turtle
window.bgcolor("silver")
window.title("Forca dos Engenheiros")

arquivo = open('entrada.txt', encoding="utf-8")
lista = arquivo.readlines()

def LISTA(p):
    list[p].strip()
    
Llimpa = []

for e in lista:
    t = e.strip()
    Llimpa.append(t)
    
escolhaPC = choice(Llimpa)
c = len(escolhaPC)
print(escolhaPC)
turtle = turtle.Turtle()  # Cria um objeto "desenhador"

#Desenhando a trave da forca

for i in range(1):
    turtle.penup()
    turtle.setpos(-300,0)
    turtle.pendown()
    turtle.speed(5)
    turtle.pensize(5)
    dist = 150
    ang = 90
    turtle.left(ang)
    turtle.forward(dist)
    turtle.right(ang)
    turtle.forward(80)
    turtle.right(ang)
    turtle.forward(35)
    
    turtle.penup()
    turtle.setpos(-185,0)
    turtle.left(90)
    
# Fazendo os espaços das letras

for i in range(c):
    turtle.speed(1)
    turtle.color("blue")
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    turtle.forward(17)
    turtle.pendown()
    
    
    
    
window.exitonclick()