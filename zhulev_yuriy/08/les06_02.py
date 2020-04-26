# coding: utf-8

# Python. Быстрый старт.
# Занятие 7.

# Домашнее задание: 
#     рисование барабана пистолета сделать функцией, которая принимает координаты базовой точки для рисования барабана;
#     анимацию вращения барабана также сделать функцией.


import turtle
#import tkSimpleDialog   # 2.x Python
import random
import math

PHI = 360 / 7
R = 50 

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

def draw_pistol(base_x, base_y):
    gotoxy(base_x, base_y)
    turtle.circle(80)
    gotoxy(base_x, base_y + 160)
    draw_circle(5, "red")
    for i in range(0,7): 
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(base_x  +math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 60)
        draw_circle(22, "white")

def rotate_pistol(base_x, base_y, start):
    for i in range(start, random.randrange(7,100)):        #random.randrange(7,100)
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(base_x + math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 60)
        draw_circle(22, "brown")
        draw_circle(22, "white")

    gotoxy(base_x + math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 60)    
    draw_circle(22, "brown")
    
    return i % 7
turtle.speed(0)
draw_pistol(100, 100)


answer = ''
start = 0
while answer != 'N':
    answer = turtle.textinput("Играть?", "Y/N")
    #tkSimpleDialog.askstring("Нарисовать окружность", "Y/N")       # for 2.x Python
    
    if answer == 'Y':
        start = rotate_pistol(100, 100, start)    
     
        if start == 0:
            gotoxy(-150, 250)
            turtle.write("Вы проиграли!", font=("Arial", 18, "normal"))   
    else:
        pass