"""Food"""
import turtle
import random
import constants as cons
import snake

class Food(turtle.Turtle):
    """Food for snakes """
    def __init__(self):
        super().__init__()
        self.shape(cons.FOOD_SHAPE)
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color(cons.FOOD_COLOR)
        self.speed(cons.FOOD_SPEED)
        self.refresh_food()

    def refresh_food(self,sn:snake.Snake =None):
        """Refreshes food after a snake eats"""

        occupied = set()

        if sn is not None:
            occupied = {(seg.xcor(),seg.ycor()) for seg in sn.snake_segments}

        while True:
            new_xcoor = random.randint(cons.MIN_X_COOR,cons.MAX_X_COOR)
            new_ycoor = random.randint(cons.MIN_Y_COOR,cons.MAX_Y_COOR)
            
            if (new_xcoor,new_ycoor) not in occupied:
                self.goto(x=new_xcoor, y= new_ycoor)
                return
