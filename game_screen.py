from guess_area import Guessbox
from game_board import Gameboard

class GameScreen():
    
    def __init__(self,settings,screen):
        self.game_board = Gameboard(settings,screen)
        self.guess_box = Guessbox(settings,screen, self.game_board)

        self.active = False
        
        
    def update(self):
        self.guess_box.update()
        self.game_board.update()