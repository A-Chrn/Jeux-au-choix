import pygame
import pygame_manager as pm
from panel import Morpion_Panel

class Morpion(pm.states.State):
    def __init__(self):
        super().__init__("Morpion")

        self.panel = Morpion_Panel()
        self.bind_panel(self.panel)

        
