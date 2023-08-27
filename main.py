from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("TURTLE CROSSING PROJECT")
screen.tracer(0)

player = Player()
car = CarManager()
car.car_list.append(car)
scoreboard = Scoreboard()
scoreboard.display_level()

screen.listen()
screen.onkeypress(key="Up", fun=player.move_up)

once = 0
loop = 1

game_is_on = True

while game_is_on:
    if game_is_on:
        if player.finish_line():
            car.inc_speed()
            scoreboard.inc_level()
        car.move()

        if loop % 6 == 0:
            if len(car.car_list) < 50:
                car_new = CarManager()
                car.car_list.append(car_new)

        car.repeat()

        if car.xcor() <= 0 or once >= 1:
            once += 1
            screen.update()
            time.sleep(0.1)
            for car_num in range(len(car.car_list)):
                if player.distance(car.car_list[car_num]) <= 20:
                    game_is_on = False
                    scoreboard.game_over()

        loop += 1

screen.exitonclick()
