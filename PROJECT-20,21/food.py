from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        rand_x_cor = random.randint(-280, 280)
        rand_y_cor = random.randint(-280, 280)
        self.goto(rand_x_cor, rand_y_cor)
