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
grade = turtle.Turtle()  # Cria um objeto "desenhador"

######################################################

#Desenhando a trave da forca

for i in range(1):
    grade.penup()
    grade.setpos(-300,0)
    grade.pendown()
    grade.speed(5)
    grade.pensize(5)
    dist = 150
    ang = 90
    grade.left(ang)
    grade.forward(dist)
    grade.right(ang)
    grade.forward(80)
    grade.right(ang)
    grade.forward(35)
    
    grade.penup()
    grade.setpos(-185,0)
    grade.left(90)
    
    
######################################################
    
# Fazendo os espaços das letras

for i in range(c):
    grade.speed(300)
    grade.color("blue")
    grade.pendown()
    grade.forward(20)
    grade.penup()
    grade.forward(17)
    grade.pendown()
    
    
    
####################################################
    # Fazendo o corpo - Cabeça
cabeca = turtle.Turtle()
cabeca.color("white")
cabeca.pensize(2)
cabeca.penup()
cabeca.setpos(-220,93)
cabeca.pendown()
cabeca.circle(10)

####################################################
    # Fazendo o corpo = Tórax
tor = turtle.Turtle()
tor.color("white")
tor.pensize(2)
tor.penup()
tor.setpos(-220,93)
tor.pd()
tor.right(90)
tor.forward(50)

####################################################
    # Fazendo o corpo = Perda da Direita
pernad = turtle.Turtle()
pernad.color("white")
pernad.pensize(2)
pernad.penup()
pernad.setpos(-220,43)
pernad.pd()
pernad.right(60)
pernad.forward(25)

    
#letra = window.textinput("Enforcando-se", "Escolha uma letra que acha que está na palavra.")

#while len(letra) != 1:
    #letra = window.textinput("Enforcando-se", "Escolha uma letra que acha que está na palavra.")

#if letra in escolhaPC:
    #turtle.write
    





window.exitonclick()