import pygame
import pygame_manager as pm
from panel import Choix_Panel

class Choix(pm.states.State):
    def __init__(self):
        super().__init__("choix")

        self.panel = Choix_Panel()
        self.bind_panel(self.panel)