"""Food"""
import turtle
import random
import constants as con

class Food(turtle.Turtle):
    """Food for snakes """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("purple")
        self.speed(0)
        self.refresh_food()

    def refresh_food(self):
        """Refreshes food after a snake eats"""
        self.goto(x=random.randint(con.MIN_X_COOR,con.MAX_X_COOR),
                  y=random.randint(con.MIN_Y_COOR,con.MAX_Y_COOR)
                )
