from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

class Food(Turtle):  # Custom Food class will inherit all attributes and methods from Turtle superclass

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(random.choice(COLORS))
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)