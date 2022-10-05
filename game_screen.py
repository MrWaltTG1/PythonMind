from guess_area import Guessbox

class GameScreen():
    
    def __init__(self,settings,screen):
        self.guess_box = Guessbox(settings,screen, 0)
        
    def update(self):
        self.guess_box.blitme()
        self.guess_box.update()