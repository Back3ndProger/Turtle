import turtle

def draw_building():
    # Переместить черепашку в заданную позицию
    turtle.penup()
    turtle.goto(-100, -200)
    turtle.pendown()

    # Нарисовать прямоугольник заданной ширины и высоты
    turtle.fillcolor("grey")  # Задать цвет заливки
    turtle.begin_fill()

    for i in range(2):
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(300)
        turtle.left(90)
    turtle.end_fill()


    # Нарисовать окна на здании
    window_size = min(200, 300) / 8  # Размер окна зависит от размера здания
    window_spacing = window_size * 2  # Расстояние между окнами
    num_windows_x = int((200 - window_spacing) / window_spacing)
    num_windows_y = int((300 - window_spacing) / window_spacing)

    # Начать рисование окон с левого нижнего угла здания
    start_x = 0 - 200 / 2 + window_spacing / 2
    start_y = -50 - 300 / 2 + window_spacing / 2

    for i in range(num_windows_x):
        for j in range(num_windows_y):
            # Переместиться к следующему окну
            window_x = start_x + i * window_spacing
            window_y = start_y + j * window_spacing
            turtle.penup()
            turtle.goto(window_x, window_y)
            turtle.pendown()

            # Нарисовать окно
            turtle.fillcolor("white")
            turtle.begin_fill()
            for k in range(4):
                turtle.forward(window_size)
                turtle.left(90)
            turtle.end_fill()

draw_building()