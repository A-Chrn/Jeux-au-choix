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

    def save(self):
        pm.data.save({"money" : self.panel.money}, "save.json")

    def on_enter(self):
        self.panel.argent.text = f"{self.panel.money} €"

        return super().on_enter()
        