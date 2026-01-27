"""Snake"""
import turtle
import constants as con

class Snake:
    """Defines snake"""

    def __init__(self):
        self.initial_snake_length = 3
        self.snake_segments:list[turtle.Turtle] = []
        self.create_snake()
        self.snake_head = self.snake_segments[0]
        self.snake_length = len(self.snake_segments)

    def create_snake(self):
        """Creates the snake with 3 segments"""
        for i in range(1,self.initial_snake_length+1):
            self.create_each_segment(-20*i,0)

    def create_each_segment(self,xcor,ycor):
        """Create each snake segment"""
        snake_segment = turtle.Turtle()
        snake_segment.shape('square')
        snake_segment.color('white')
        snake_segment.penup()
        snake_segment.goto(x=xcor,y=ycor)
        self.snake_segments.append(snake_segment)
  
    def increase_snake(self):
        """Increse snake length after food"""
        last_snake_segment = self.snake_segments[self.snake_length-1]
        self.create_each_segment(last_snake_segment.xcor()-20*self.snake_length,last_snake_segment.ycor())
        self.snake_length = len(self.snake_segments)
        self.move()

    def move(self):
        """Moves the snake"""
        for segment_num in range(self.snake_length-1,0,-1):
            new_x = self.snake_segments[segment_num-1].xcor()
            new_y = self.snake_segments[segment_num-1].ycor()
            self.snake_segments[segment_num].goto(x=new_x,y=new_y)
        self.snake_segments[0].forward(con.SNAKE_PACE)

    def up(self):
        """Moves snake up"""
        if self.snake_head.heading() != con.UP_DIRECTION:
            self.snake_head.setheading(con.UP_DIRECTION)

    def down(self):
        """Moves snake down"""
        if self.snake_head.heading() != con.DOWN_DIRECTION:
            self.snake_head.setheading(con.DOWN_DIRECTION)

    def left(self):
        """Moves snake left"""
        if self.snake_head.heading() != con.LEFT_DIRECTION:
            self.snake_head.setheading(con.LEFT_DIRECTION)

    def right(self):
        """Moves snake right"""
        if self.snake_head.heading() != con.RIGHT_DIRECTION:
            self.snake_head.setheading(con.RIGHT_DIRECTION)
