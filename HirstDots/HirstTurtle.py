from turtle import Turtle,Screen
from ExtraindoCoresColorgram import lista_cor
import random
hirst=Turtle()
tela=Screen()
tela.colormode(255)
# hirst.pencolor(random.choice(lista_cor))
hirst.penup()
hirst.hideturtle()
hirst.setheading(225)
hirst.forward(300)
hirst.setheading(0)

hirst.speed("fastest")

n_dots=101

for count_dots in range(1,n_dots):
    hirst.dot(20,random.choice(lista_cor))
    hirst.penup()
    hirst.forward(50)
    if count_dots%10==0:
        hirst.left(90)
        hirst.forward(40)
        hirst.left(90)
        hirst.forward(500)
        hirst.setheading(0)

tela.exitonclick()