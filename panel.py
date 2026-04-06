import pygame
import pygame_manager as pm

class MENU_Panel(pm.panels.Panel):
    def __init__(self):
        super().__init__("MENU", rect=pygame.Rect(0, 0, 1920, 1080), centered=True)
        self.background = (180, 197, 253)
        
        self.boutton1 = pm.ui.RectButton(
            x = self.centerx, 
            y = self.centery, 
            anchor = "center",
            width = 400, 
            height = 120, 
            filling_color = (0, 0, 0), 
            filling_color_hover = (46, 46, 46),
            border_radius = 20,
            text = "JOUER",
            font_color=(255, 255, 255),
            hover_scale_ratio=1.05,
            hover_scale_duration=0.05,
            callback = self.handle_start, 
            panel = str(self)
            )
            
    def draw_back(self, surface):
        surface.fill(self.background)
        return super().draw_back(surface)
    
    def handle_start(self):
        pm.states.activate("choix")

class Choix_Panel(pm.panels.Panel):
    def __init__(self):
        super().__init__("CHOIX", rect=pygame.Rect(0, 0, 1920, 1080), centered=True)
        self.background = (180, 197, 253)

        self.title = pm.ui.Text(
            x=self.width * 0.5,
            y=self.height * 0.2,
            anchor="center",
            text="CLIQUE SUR LE JEU DE TON CHOIX",
            font=pygame.font.SysFont("arial", 84),
            font_size=84,
            font_color=(0, 255, 255),
            gradient=True,
            gradient_color=(255, 0, 255),
            gradient_direction="diagonal",
            gradient_fluctuation=True,
            panel=str(self)
        )

        self.boutton1 = pm.ui.RectButton(
            x = self.width * 0.3, 
            y = self.centery, 
            anchor = "center",
            width = 400, 
            height = 120, 
            filling_color = (0, 0, 0), 
            filling_color_hover = (46, 46, 46),
            hover_scale_ratio=1.05,
            hover_scale_duration=0.05,
            border_radius = 20,
            text = "MORPION",
            font_color=(255, 255, 255),
            callback = self.handle_start1, 
            panel = str(self)
            )
        
        self.boutton2 = pm.ui.RectButton(
            x = self.width * 0.7, 
            y = self.centery, 
            anchor = "center",
            width = 400, 
            height = 120, 
            filling_color = (0, 0, 0), 
            filling_color_hover = (46, 46, 46),
            hover_scale_ratio=1.05,
            hover_scale_duration=0.05,
            border_radius = 20,
            text = "JEUX CLICKER",
            font_color=(255, 255, 255),
            callback = self.handle_start2, 
            panel = str(self)
            )
        
        self.boutton3 = pm.ui.RectButton(
            x = self.width * 0.05, 
            y = self.height * 0.95, 
            anchor = "center",
            width = 140, 
            height = 80,
            filling=False,
            filling_color=(255, 255, 255, 50),
            border_radius = 20,
            text = "RETOUR",
            font_color=(255, 255, 255),
            callback = self.handle_start3, 
            panel = str(self)
            )
    def draw_back(self, surface):
        surface.fill(self.background)
        return super().draw_back(surface)
    
    def handle_start1(self):
        pm.states.activate("Morpion")

    def handle_start2(self):
        pm.states.activate("Clicker")

    def handle_start3(self):
        pm.states.activate("MENU")

class Morpion_Panel(pm.panels.Panel):
    def __init__(self):
        super().__init__("MORPION", rect=pygame.Rect(0, 0, 1920, 1080), centered=True)
        self.background = (67, 67, 70)
        self.boutton1 = pm.ui.RectButton(
            x = self.width * 0.05, 
            y = self.height * 0.95, 
            anchor = "center",
            width = 140, 
            height = 80,
            filling=False,
            filling_color=(255, 255, 255, 50),
            border_radius = 20,
            text = "RETOUR",
            font_color=(255, 255, 255),
            callback = self.handle_start, 
            panel = str(self)
            )
    
    def draw_back(self, surface):
        surface.fill(self.background)
        return super().draw_back(surface)
    
    def handle_start(self):
        pm.states.activate("choix")

class Clicker_Panel(pm.panels.Panel):
    def __init__(self):
        super().__init__("CLICKER", rect=pygame.Rect(0, 0, 1920, 1080), centered=True)
        self.background = (67, 67, 70)

        self.boutton1 = pm.ui.RectButton(
            x = self.width * 0.05, 
            y = self.height * 0.95, 
            anchor = "center",
            width = 140, 
            height = 80,
            filling=False,
            filling_color=(255, 255, 255, 50),
            border_radius = 20,
            text = "RETOUR",
            font_color=(255, 255, 255),
            callback = self.handle_start, 
            panel = str(self)
            )
        
        self.boutton2 = pm.ui.RectButton(
            x = self.centerx,
            y = self.centery,
            anchor = "center"
        )
    
    def draw_back(self, surface):
        surface.fill(self.background)
        return super().draw_back(surface)
    
    def handle_start(self):
        pm.states.activate("choix")