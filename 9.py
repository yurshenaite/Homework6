# Напишите программу, которая строит два прямоугольника. Каждый прямоугольник задается координатами верхней левой
# и правой нижней вершин. Программа должна выводить сообщение об относительном расположении этих прямоугольников,
# рассматривая следующие случаи :
# 1. Прямоугольники лежат вне друг друга, не касаясь;
# 2. Прямоугольники имеют касание
# 3. Прямоугольники имеют пересечение
# 4. Один прямоугольник лежит внутри другого, не касаясь"

import turtle

print('Число 1 означает параметры для первого прямоугольника, 2 - для второго.')

#Вводятся параметры для первого прямоугольника
vlx_1 = float(input('1.Введите координаты x верхней левой вершины: '))
vly_1 = float(input('1.Введите координаты у верхней левой вершины: '))
npx_1 = float(input('1.Введите координаты x нижней правой вершины: '))
npy_1 = float(input('1.Введите координаты y нижней правой вершины: '))
length_1 = float(input('1.Введите длину стороны первого прямоугольника: '))

#Вводятся параметры для второго прямоугольника
vlx_2 = float(input('2.Введите координаты x верхней левой вершины: '))
vly_2 = float(input('2.Введите координаты у верхней левой вершины: '))
npx_2 = float(input('2.Введите координаты x нижней правой вершины: '))
npy_2 = float(input('2.Введите координаты y нижней правой вершины: '))
length_2 = float(input('2.Введите длину стороны второго прямоугольника: '))

turtle.penup()
turtle.goto(vlx_1, vly_1)
turtle.pendown()
turtle.pencolor('black')
turtle.forward(length_1)
turtle.right(90)
turtle.goto(npx_1, npy_1)
turtle.right(90)
turtle.forward(length_1)
turtle.right(90)
turtle.goto(vlx_1, vly_1)
turtle.penup()

turtle.penup()
turtle.goto(vlx_2, vly_2)
turtle.pendown()
turtle.pencolor('black')
turtle.forward(length_2)
turtle.right(90)
turtle.goto(npx_2, npy_2)
turtle.right(90)
turtle.forward(length_2)
turtle.right(90)
turtle.goto(vlx_2, vly_2)
turtle.penup()

def check_rectangles(vlx_1, vly_1, npx_1, npy_1, length_1, vlx_2, vly_2, npx_2, npy_2, length_2):
    if npx_1 < vlx_2 or npx_2 < vlx_1 or npy_1 > vly_2 or npy_2 > vly_1:
        turtle.goto(-100, -100)
        turtle.pendown()
        turtle.pencolor('red')
        turtle.write("Прямоугольники не пересекаются и не касаются.")
    elif npx_1 == vlx_2 or npx_2 == vlx_1 or npy_1 == vly_2 or npy_2 == vly_1:
        turtle.goto(-100, -150)
        turtle.pendown()
        turtle.pencolor('red')
        turtle.write("Прямоугольники касаются.")
    elif (vlx_1 < vlx_2 and vly_1 > vly_2 and npx_1 > npx_2 and npy_1 < npy_2) or (
            vlx_2 < vlx_1 and vly_2 > vly_1 and npx_2 > npx_1 and npy_2 < npy_1):
        turtle.goto(-100, -150)
        turtle.pendown()
        turtle.pencolor('red')
        turtle.write("Один прямоугольник лежит внутри другого, не касаясь.")
    else:
        turtle.goto(-100, -150)
        turtle.pendown()
        turtle.pencolor('red')
        turtle.write("Прямоугольники пересекаются.")

check_rectangles(vlx_1, vly_1, npx_1, npy_1, length_1, vlx_2, vly_2, npx_2, npy_2, length_2)

turtle.done()