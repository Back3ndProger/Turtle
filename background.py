import turtle
from turtle import *
from town import draw_building


# создаем экран и черепашку
screen = turtle.Screen()

# устанавливаем цвет фона и скорость черепашки
screen.bgcolor("skyblue")
speed(0)

# делаем черепашку невидимой
hideturtle()

# функция для рисования солнца
def draw_sun():
    penup()
    goto(-250, 150)
    pendown()
    begin_fill()
    fillcolor("yellow")
    circle(50)
    end_fill()
    hideturtle()
draw_sun()

# рисуем небо и солнце
penup()
goto(-300, 200)
pendown()
begin_fill()
fillcolor("white")
end_fill()

import turtle

# создаем экран и черепашку
screen = turtle.Screen()
grass = turtle.Turtle()

# устанавливаем цвет фона и скорость черепашки
screen.bgcolor("skyblue")
grass.speed(0)

# делаем черепашку невидимой
grass.hideturtle()

# функция для рисования травы
def draw_grass():
    grass.penup()
    grass.goto(-300, -200)
    grass.pendown()
    grass.begin_fill()
    grass.fillcolor("green")
    for i in range(2):
        grass.forward(15000)
        grass.right(90)
        grass.forward(15000)
        grass.right(90)
        grass.forward(15000)
    grass.end_fill()
    grass.hideturtle()

# рисуем небо, солнце и траву
grass.penup()
grass.goto(-300, 200)
grass.pendown()
grass.begin_fill()
grass.fillcolor("white")
grass.end_fill()
draw_sun()
draw_grass()
# закрываем окно по клику
screen.exitonclick()

