import pygame
import pygame_manager as pm
from panel import Morpion_Panel
from grille import Grille

class Morpion(pm.states.State):
    def __init__(self):
        super().__init__("Morpion")
        
        self.panel = Morpion_Panel()
        self.bind_panel(self.panel)

        self.x = self.panel.grille_image.x - self.panel.grille_image.width / 2
        self.y = self.panel.grille_image.y - self.panel.grille_image.height / 2
        self.taille = self.panel.grille_image.width / 3
        
        self.grille = Grille(self.x, self.y, self.taille, self.panel)
        self.boutons = []

    def generate(self, x, y, taille):
        for i in range(3):
            l = []
            for j in range(3):
                bouton = pm.ui.RectButton(
                    x = x + taille * j,
                    y = y + taille * i,
                    width = taille,
                    height = taille,
                    anchor = "topleft",
                    filling = False,
                    filling_hover = False,
                    callback = self.place,
                    panel = str(self.panel),
                    id = (j, i),
                    callback_give_id = True,
                    zorder = 10
                )
                l.append(bouton)
            self.boutons.append(l)

    def place(self, id):
        x, y = id
        self.grille.placer(x, y)

    def on_enter(self):
        self.generate(self.x, self.y, self.taille)
        return super().on_enter()

    def on_exit(self):
        for i in range(len(self.boutons)):
            for j in range(len(self.boutons[i])):
                self.boutons[i][j].kill()
        return super().on_exit()
        
