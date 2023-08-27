from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.left(180)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(320, random.randint(-250, 250))
        self.car_list = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.car_list:
            car.forward(self.move_speed)

    def repeat(self):
        for car in self.car_list:
            if car.xcor() <= -320:
                car.goto(320, random.randint(-250, 250))

    def inc_speed(self):
        self.move_speed += MOVE_INCREMENT
