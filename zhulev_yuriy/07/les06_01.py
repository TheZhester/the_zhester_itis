# coding: utf-8

# Python. Быстрый старт.
# Занятие 6.

# Домашнее задание: свободная форма - потренироваться в рисовании с использованием turtle


import turtle
#import tkSimpleDialog   # для 2.x Python
import random
import math


''' Строка в тройных кавычках - многострочная строка.
    Может использоваться в качестве многострочного комментария.
'''

def gotoxy(x, y):
    ''' Функция перевода курсора без рисования линии
    '''
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

    
def draw_circle(r, color):
    ''' Функция рисования круга заданного радиуса и цвета
    '''
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()    
    
# Скорость, равная нулю - максимальная    
turtle.speed(0)

gotoxy(0,0)
turtle.circle(80)
gotoxy(0,160)
draw_circle(5, "red")

phi = 360 / 7
r = 50 

for i in range(0,7):
    phi_rad = phi * i * math.pi / 180.0
    gotoxy(math.sin(phi_rad)*r, math.cos(phi_rad)*r + 60)
    turtle.circle(22)

    
gotoxy(math.sin(phi_rad)*r, math.cos(phi_rad)*r + 60)    
draw_circle(22, "brown")


answer = ''
while answer != 'N':
    answer = turtle.textinput("Нарисовать окружность", "Y/N")
    #tkSimpleDialog.askstring("Нарисовать окружность", "Y/N")       # Для 2.x Python
    
    if answer == 'Y':
        turtle.penup()
        turtle.goto(random.randrange(-300,300), random.randrange(-200,200))
        turtle.pendown()
        turtle.fillcolor(random.random(),random.random(),random.random())
        turtle.begin_fill()
        turtle.circle(random.randrange(1,100))
        turtle.end_fill()
    else:
        pass