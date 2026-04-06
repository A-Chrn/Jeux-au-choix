import pygame
import pygame_manager as pm
from menu import Menu
from Choix import Choix
from morpion import Morpion
from clicker import Clicker

class Main():
    def __init__(self):
        pm.init()
        self.menu = Menu()
        self.choix = Choix()
        self.morpion = Morpion()
        self.clicker = Clicker()

        pm.states.activate("MENU")
        pm.screen.set_vsync(True)

    def update(self):
        pm.screen.clear((70, 70, 85))
        pm.states.update()

main = Main()
pm.run(main.update)