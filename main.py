"""Snake Game"""
import turtle
import time
import snake
import food
import constants as con

# pylint: disable=invalid-name
screen = turtle.Screen()
screen.setup(height=con.WINDOW_HEIGHT,width=con.WINDOW_WIDTH)
screen.bgcolor('black')
screen.title('Sssssnake')
screen.tracer(0) #Removes the turtle animation.

my_snake = snake.Snake()
my_food = food.Food()

screen.listen()
screen.onkey(my_snake.up,"Up")
screen.onkey(my_snake.down,"Down")
screen.onkey(my_snake.left,"Left")
screen.onkey(my_snake.right,"Right")


screen.update() #Updates the turtle position at this point only.

game_on = True
while game_on is True:
    screen.update()
    time.sleep(0.1)
    my_snake.move()
    if my_snake.snake_head.distance(my_food) < con.SNAKE_FOOD_DISTANCE:
        my_snake.increase_snake()
        my_food.refresh_food()


screen.mainloop()
