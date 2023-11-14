import random
import turtle
import time
t = turtle
t.bgcolor('black')
t.pencolor('blue')
turtle.shape("turtle")
t.title('Тебе повезет')
t.speed(1000000000000000000000000000000000000000)
b = 0
a = 1
c = 30000
h = 0
while True:
    c -= 500
    print('Ваш счёт', c, '$!')
    if c < 500:
        print('у вас ноль рублей на балансе!')
        break
    time.sleep(4)
    t.penup()
    t.pendown()
    t.clear()
    a = int(t.textinput('Введите число', ''))
    b = int(random.randint(1, 10))
    if a == b:
        c = c + 10000
        print('Ваш счёт', c, '$!')
        print('вы выграли')
        turtle.exitonclick()
        break

    print(a, b)
    t.goto(0, 0)
    t.pendown()
    t.clear()
    if b == 1:
        t.right(-45)
        t.fd(180)
        t.right(135)
        t.fd(300)
        t.left(90)
    if b == 2:
        t.left(90)
        for i in range(180):
            t.fd(1)
            t.left(-1)
        t.left(-45)
        t.fd(180)
        t.left(135)
        t.fd(130)
    if b == 3:
        for i in range(180):
            t.fd(1)
            t.left(-1)
        t.left(180)
        for i in range(180):
            t.fd(1)
            t.left(-1)
        t.left(180)
    if b == 4:
        for i in range(3):
            t.right(90)
            t.forward(180)
        t.penup()
        t.goto(0, 0)
        t.right(180)
        t.pendown()
        t.fd(360)
        t.lt(90)
    if b == 5:
        t.penup()
        t.fd(180)

        t.pendown()
        t.fd(-180)
        t.right(90)
        t.fd(180)
        t.left(90)
        t.fd(110)
        for i in range(220):
            t.right(1.1)
            t.fd(2)
        t.penup()
        for i in range(220):
            t.right(-1.1)
            t.fd(-2)
        t.fd(-110)
        t.left(-90)
        t.fd(-180)
        t.right(-90)
        t.fd(180)
    if b == 6:
        t.left(180+45+20)
        t.fd(180)
        for i in range(360):
            t.left(1)
            t.fd(1)
        t.penup()
        for i in range(360):
            t.left(-1)
            t.fd(1)
        t.fd(-180)
        t.left(-180+-45+-20)
    if b == 7:
        t.fd(180)
        t.right(120)
        t.fd(300)
        t.penup()
        t.goto(0, 0)
        t.right(-120)
    if b == 8:
        for i in range(360):
            t.left(-1)
            t.fd(1)
        for i in range(360):
            t.left(1)
            t.fd(1)
    if b == 9:
        for i in range(360):
            t.left(-1)
            t.fd(1)
        for i in range(120):
            t.left(-1)
            t.fd(1)
        t.fd(220)
        t.left(360)
        t.left(120)
    if b == 10:
        t.right(-45)
        t.fd(90)
        t.right(135)
        t.fd(180)
        t.left(90)
        t.penup()
        t.fd(130)
        t.pendown()
        for i in range(90):
            t.left(1)
            t.fd(1)
        t.fd(90)
        for i in range(180):
            t.left(1)
            t.fd(1)
        t.fd(90)
        for i in range(90):
            t.left(1)
            t.fd(1)
    v = a

    h = b

    if v == h:
        many = c + 10000
        print('Ваш счёт', c, '$!')
        print('Вы выйграли')
        turtle.exitonclick()
        break
