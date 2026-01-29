"""Snake"""
import turtle
import constants as cons

class Snake:
    """Defines snake"""

    def __init__(self):
        self.initial_snake_length = cons.SNAKE_INITIAL_LENGTH
        self.snake_segments:list[turtle.Turtle] = []
        self.create_snake()
        self.snake_head = self.snake_segments[0]
        self.snake_length = len(self.snake_segments)

    def create_snake(self):
        """Creates the snake with initial no. of segments"""
        for i in range(1,self.initial_snake_length+1):
            self.create_each_segment(-20*i,0)

    def create_each_segment(self,xcor,ycor):
        """Create each snake segment"""
        snake_segment = turtle.Turtle()
        snake_segment.shape('square')
        snake_segment.color(cons.SNAKE_COLOR)
        snake_segment.penup()
        snake_segment.goto(x=xcor,y=ycor)
        self.snake_segments.append(snake_segment)

    def increase_snake(self):
        """Increse snake length after food"""
        last_snake_segment = self.snake_segments[self.snake_length-1]
        self.create_each_segment(last_snake_segment.xcor()-20*self.snake_length,
                                 last_snake_segment.ycor()
                                )
        self.snake_length = len(self.snake_segments)
        self.move()

    def move(self):
        """Moves the snake"""
        for segment_num in range(self.snake_length-1,0,-1):
            new_x = self.snake_segments[segment_num-1].xcor()
            new_y = self.snake_segments[segment_num-1].ycor()
            self.snake_segments[segment_num].goto(x=new_x,y=new_y)
        self.snake_head.forward(cons.SNAKE_PACE)
        self.fix_snake_position()

    def up(self):
        """Moves snake up"""
        if self.snake_head.heading() != cons.DOWN_DIRECTION:
            self.snake_head.setheading(cons.UP_DIRECTION)

    def down(self):
        """Moves snake down"""
        if self.snake_head.heading() != cons.UP_DIRECTION:
            self.snake_head.setheading(cons.DOWN_DIRECTION)

    def left(self):
        """Moves snake left"""
        if self.snake_head.heading() != cons.RIGHT_DIRECTION:
            self.snake_head.setheading(cons.LEFT_DIRECTION)

    def right(self):
        """Moves snake right"""
        if self.snake_head.heading() != cons.LEFT_DIRECTION:
            self.snake_head.setheading(cons.RIGHT_DIRECTION)

    def fix_snake_position(self):
        """Fixes snake position"""
        if self.snake_head.xcor() > cons.MAX_X_COOR:
            self.snake_head.goto(cons.MIN_X_COOR,self.snake_head.ycor())

        if self.snake_head.xcor() < cons.MIN_X_COOR:
            self.snake_head.goto(cons.MAX_X_COOR,self.snake_head.ycor())

        if self.snake_head.ycor() > cons.MAX_Y_COOR:
            self.snake_head.goto(self.snake_head.xcor(),cons.MIN_Y_COOR)

        if self.snake_head.ycor() < cons.MIN_Y_COOR:
            self.snake_head.goto(self.snake_head.xcor(),cons.MAX_Y_COOR)
    
    def snake_hits_itself(self):
        for segment in self.snake_segments[1:]:
            if segment.distance(self.snake_head) < cons.SNAKE_PACE/2:
                return True
        return False