# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:10:52 2015

@author: Gabriel Olanda

"""
jogada = 1
while jogada == 1:
    from random import choice
    import time
    
    
    import turtle               # Iniciando e importando a biblioteca Turtle
    window = turtle.Screen()    # Criando uma janela para a função Turtle
    window.bgcolor("silver")
    window.title("Forca dos Engenheiros")
    window.screensize(1000,1000)
    arquivo = open('entrada.txt', encoding="utf-8")
    lista = arquivo.readlines()
    
    def LISTA(p):
        list[p].strip()
        
    Llimpa = []
    
    for e in lista:
        t = e.strip()
        if t !='':
            Llimpa.append(t)
        
        
    escolhaPCx = choice(Llimpa)
    escolhaPC = escolhaPCx.upper()
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
        grade.setpos(-180,0)
        grade.left(90)
        
        
    ######################################################
        
    # Fazendo os espaços das letras
    
    for i in range(c):
        if escolhaPC[i] == " ":
            grade.penup()
            grade.forward(40)
            grade.pendown()
        else:    
            grade.speed(500)
            grade.color("blue")
            grade.pendown()
            grade.forward(30)
            grade.penup()
            grade.forward(10)
            grade.pendown()
        
        
    ####################################################
    """    # Fazendo o corpo - Cabeça
    cabeca = turtle.Turtle()
    cabeca.color("white")
    cabeca.pensize(2)
    cabeca.penup()
    cabeca.setpos(-220,93)
    cabeca.pendown()
    cabeca.circle(10)
    """
    
    ####################################################
    """ 
       # Fazendo o corpo = Tórax
    tor = turtle.Turtle()
    tor.color("white")
    tor.pensize(2)
    tor.penup()
    tor.setpos(-220,93)
    tor.pd()
    tor.right(90)
    tor.forward(50)
    """
    
    ####################################################
    """   
       # Fazendo o corpo = Perna da Direita
    pernad = turtle.Turtle()
    pernad.color("white")
    pernad.pensize(2)
    pernad.penup()
    pernad.setpos(-220,43)
    pernad.pd()
    pernad.right(45)
    pernad.forward(25)
    """
    
    ####################################################
    """
        # Fazendo o corpo = Perna da Esquerda
    pernae = turtle.Turtle()
    pernae.color("white")
    pernae.pensize(2)
    pernae.penup()
    pernae.setpos(-220,43)
    pernae.pd()
    pernae.right(135)
    pernae.forward(25)
    """
    
    ####################################################
    """
        # Fazendo o corpo = Braço da Direita
    bracod = turtle.Turtle()
    bracod.color("white")
    bracod.pensize(2)
    bracod.penup()
    bracod.setpos(-220,75)
    bracod.pd()
    bracod.right(45)
    bracod.forward(25)
    """
    ####################################################
    """
        # Fazendo o corpo = Braço da Esquerda
    bracoe = turtle.Turtle()
    bracoe.color("white")
    bracoe.pensize(2)
    bracoe.penup()
    bracoe.setpos(-220,75)
    bracoe.pd()
    bracoe.right(135)
    bracoe.forward(25)
    """

    bracod = turtle.Turtle()
    pernae = turtle.Turtle()
    cabeca = turtle.Turtle() 
    tor = turtle.Turtle()   
    pernad = turtle.Turtle()
    bracoe = turtle.Turtle()
    ####################################################
    def boneco_enforcado(npartes):
    
        if npartes == 1:
                
                cabeca.color("white")
                cabeca.pensize(2)
                cabeca.penup()
                cabeca.setpos(-220,93)
                cabeca.pendown()
                cabeca.circle(10)
               
                        
            
        if npartes == 2:
                # Fazendo o corpo = Tórax
                
                tor.color("white")
                tor.pensize(2)
                tor.penup()
                tor.setpos(-220,93)
                tor.pd()
                tor.right(90)
                tor.forward(50)
                
            
        if npartes == 3:
                    # Fazendo o corpo = Perna da Direita
                
                pernad.color("white")
                pernad.pensize(2)
                pernad.penup()
                pernad.setpos(-220,43)
                pernad.pd()
                pernad.right(45)
                pernad.forward(25)
               
                
        if npartes == 4:
                    # Fazendo o corpo = Perna da Esquerda
                
                pernae.color("white")
                pernae.pensize(2)
                pernae.penup()
                pernae.setpos(-220,43)
                pernae.pd()
                pernae.right(135)
                pernae.forward(25)
               
                
        if npartes == 5:
                    # Fazendo o corpo = Braço da Direita
                
                bracod.color("white")
                bracod.pensize(2)
                bracod.penup()
                bracod.setpos(-220,75)
                bracod.pd()
                bracod.right(45)
                bracod.forward(25)
                
                
        if npartes == 6:
                    # Fazendo o corpo = Braço da Esquerda
                
                bracoe.color("white")
                bracoe.pensize(2)
                bracoe.penup()
                bracoe.setpos(-220,75)
                bracoe.pd()
                bracoe.right(135)
                bracoe.forward(25)
                
                bracoe.penup()
                bracoe.setpos(-100,100)
                bracoe.pd()
                bracoe.color("red")
                bracoe.right(135)
                bracoe.right(90)
                bracoe.write("Wasted", font = ("Arial",35))
                time.sleep(3)
                global jogada
                jogada = 2
                window.clear()
                grade.clear()
                cabeca.clear()
                tor.clear()
                pernad.clear()
                pernae.clear()
                bracoe.clear()
                bracod.clear()
                letras.clear()
                vit.clear()
                jogada = 1
                boneco_enforcado()
    ####################################################
    
    letras = turtle.Turtle()
    letras.pu()
    letras.setpos(-185,0)
    letras.pd()
    
    win = escolhaPC.count(" ")
    
    npartes = 0
    #letras.write("The forca mininu", True, align="center")
    while win < len(escolhaPC):
        a = window.textinput("Enforcando-se", "Escolha uma letra que acha que está na palavra.")
        letra = a.upper()
        while len(letra) != 1:
            letra = window.textinput("Enforcando-se", "Escolha uma letra que acha que está na palavra.")
        
      
            
        if letra in escolhaPC:
            i = escolhaPC.index(letra)
            print(i)
            letras.pu()
            letras.setpos(-175+40*i ,0)
            letras.write(letra, font=("Arial",20))
            letras.pd()
            #win+=1
            lista2 = []
            for i in range(c):
                if escolhaPC[i] == letra:
                    lista2.append(i)
                    win += 1
            for pos in lista2:
                letras.pu()
                letras.hideturtle()
                letras.setpos(-175+40*(pos) ,0)
                letras.write(letra, font=("Arial",20))
                    
       
        
        else:
            npartes+=1        
            boneco_enforcado(npartes)
               
        if win == len(escolhaPC):
            vit = turtle.Turtle()
            vit.penup()
            vit.setpos(-100,100)
            vit.pd()
            vit.color("red")
            vit.right(135)
            vit.right(90)
            vit.write("Vitória", font = ("Arial",35))
            time.sleep(3)
            jogada = 2
            
            
            jogada = 1
    
    
    
    window.exitonclick()