"""Snake Game """
import turtle
import snake
import food
import constants as cons
import tkinter.messagebox as msg
import scoreboard as sc

class SnakeGame:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(height=cons.WINDOW_HEIGHT, width=cons.WINDOW_WIDTH)
        self.screen.bgcolor('black')
        self.screen.tracer(0)
        
        self.my_snake = snake.Snake()
        self.my_food = food.Food()
        self.current_score = 0
        self.game_on = True
        
        # Load highscore
        self.highscore, self.highscore_player_name = sc.load_highscore()
        self.update_title()
        
        # Get player name
        self.current_player = self.screen.textinput(
            "Welcome to Snake", 
            "Enter your name please."
        ) or "Anonymous"
        
        # Setup controls
        self.setup_controls()
        
    def setup_controls(self):
        """Setup keyboard controls"""
        self.screen.listen()
        self.screen.onkey(self.my_snake.up, "Up")
        self.screen.onkey(self.my_snake.down, "Down")
        self.screen.onkey(self.my_snake.left, "Left")
        self.screen.onkey(self.my_snake.right, "Right")
    
    def update_title(self):
        """Update screen title"""
        if self.highscore > 0:
            self.screen.title(
                f"Score: {self.current_score} | "
                f"High Score: {self.highscore} by {self.highscore_player_name}"
            )
        else:
            self.screen.title(f"Score: {self.current_score} | No high score set")
    
    def check_food_collision(self):
        """Check if snake eats food"""
        if self.my_snake.snake_head.distance(self.my_food) < cons.SNAKE_FOOD_DISTANCE:
            self.current_score += 1
            self.my_snake.increase_snake()
            self.my_food.refresh_food(self.my_snake)
            self.update_title()
    
    def game_over(self):
        """Handle game over"""
        self.game_on = False
        
        # Check for new highscore
        if self.current_score > self.highscore:
            if self.highscore > 0:
                points_ahead = self.current_score - self.highscore
                msg.showinfo(
                    "NEW HIGH SCORE!", 
                    f"CONGRATULATIONS! You beat {self.highscore_player_name}'s "
                    f"score by {points_ahead} point(s)!"
                )
            else:
                msg.showinfo(
                    "NEW HIGH SCORE!", 
                    f"CONGRATULATIONS! You set the first high score: {self.current_score}!"
                )
            sc.save_highscore(self.current_score, self.current_player)
        else:
            msg.showerror("GAME OVER", f"You lost! Final score: {self.current_score}")
        
        self.screen.bye()
    
    def game_loop(self):
        """Main game loop"""
        if not self.game_on:
            return
        
        self.my_snake.move()
        self.screen.update()
        
        if self.my_snake.snake_hits_itself():
            self.game_over()
            return
        
        self.check_food_collision()
        
        # Schedule next frame
        self.screen.ontimer(self.game_loop, 100)
    
    def run(self):
        """Start the game"""
        self.game_loop()
        self.screen.mainloop()


if __name__ == "__main__":
    game = SnakeGame()
    game.run()