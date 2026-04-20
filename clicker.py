import pygame
import pygame_manager as pm
from panel import Clicker_Panel

class Clicker(pm.states.State):
    def __init__(self):
        super().__init__("Clicker")

        self.panel = Clicker_Panel()
        self.bind_panel(self.panel)

    def update(self):
        ...

    def on_enter(self):
        self.argent = 0
        self.panel.argent.text = str(self.argent)

        return super().on_enter()
        