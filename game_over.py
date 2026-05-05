import pygame
import pygame_manager as pm
from panel import Game_Over_Panel

class Game_Over(pm.states.State):
    def __init__(self):
        super().__init__("Game_Over")

        self.panel = Game_Over_Panel()
        self.bind_panel(self.panel)

    
