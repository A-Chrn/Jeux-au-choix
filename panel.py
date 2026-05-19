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
        
        self.grille_image = pm.ui.Image(
            x = self.centerx,
            y = self.centery,
            image_path = "grille_morpion.png",
            width = 900,
            height = 900,
            anchor ="center",
            panel = str(self),
            zorder = 1
        )

    
    def draw_back(self, surface):
        surface.fill(self.background)
        return super().draw_back(surface)
    
    def handle_start(self):
        pm.states.activate("choix")

class Clicker_Panel(pm.panels.Panel):
    def __init__(self,):
        super().__init__("CLICKER", rect=pygame.Rect(0, 0, 1920, 1080), centered=True)
        self.background = (67, 67, 70)
        self.money = 0
        self.multiplier = 1
        self.upgrade_price = 50
        pm.audio.add_sound("click", "click.mp3", 0.2, 0, "default")
        if pm.data.exists("save.json") :
            self.money = pm.data.load("save.json")["money"]


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
        
        self.boutton2 = pm.ui.CircleButton(
            x = self.centerx,
            y = self.centery,
            radius = 175,
            filling_color = (39, 139, 245),
            filling_color_hover = (26, 91, 161),
            text = "CLIQUE ICI",
            font_color = (255, 255, 255),
            font_size = 84,
            callback = self.click,
            panel = str(self),

        )

        self.argent_text = pm.ui.Text(
            x = self.width * 0.02,
            y = self.height * 0.08,
            text = "Argent : ",
            font_size = 70,
            font_color = (255, 255, 255),
            panel = str(self),
        )

        self.argent = pm.ui.Text(
            x = self.width * 0.13,
            y = self.height * 0.082,
            text = str(0),
            font_color= (255, 255, 255),
            font_size = 70,
            bold = True,
            panel = str(self),
        )

    def draw_back(self, surface):
        surface.fill(self.background)
        surface.blit(self.argent.surface, self.argent.rect)

        return super().draw_back(surface)
    
    def handle_start(self):
        pm.states.activate("choix")
        pm.data.save({"money" : self.money}, "save.json", )

    def click(self):
        self.money += self.multiplier
        self.argent.text = f"{self.money} €"
        pm.audio.play_sound("click")
    
    def on_enter(self):
        self.multiplicateur = pm.ui.RectButton(
            x = self.width * 0.9,
            y = self.height * 0.1,
            width = 300,
            height = 80,
            anchor = "center",
            filling_color = (39, 139, 245),
            filling_color_hover = (26, 91, 161),
            border_radius = 20,
            font_color = (255, 255, 255),
            callback = self.double_click,
            panel = str(self),
        )

        self.bouton_text = pm.ui.Text(
            x = self.width * 0.9,
            y = self.height * 0.1,
            text = f"x{self.multiplier + 1} / click = {self.upgrade_price} €",
            font_color = (255, 255, 255),
            font_size = 50,
            anchor = "center",
            panel = str(self),
            zorder=1
        )

        self.multiplicateur_text = pm.ui.Text(
            x = self.width // 2,
            y = self.height * 0.1,
            text = f"x{self.multiplier} / click",
            font_color = (255, 255, 255),
            font_size = 70,
            anchor = "center",
            panel = str(self),
            zorder=1
        )

        return super().on_enter()
    
    def double_click(self):
        if self.money >= self.upgrade_price:
            self.money -= self.upgrade_price
            self.multiplier += 1
            self.upgrade_price *= 2
            self.argent.text = f"{self.money} €"
            self.bouton_text.text = f"x{self.multiplier + 1} / click = {self.upgrade_price} €"
            self.multiplicateur_text.text = f"x{self.multiplier} / click"


class Game_Over_Panel(pm.panels.Panel):
    def __init__(self):
        super().__init__("GAME_OVER", rect=pygame.Rect(0, 0, 1920, 1080), centered=True)
        self.background = (67, 67, 70)

        self.title = pm.ui.Text(
            x=self.width * 0.5,
            y=self.height * 0.2,
            anchor="center",
            text="Le gagnant est : ",
            font=pygame.font.SysFont("arial", 84),
            font_size=84,
            font_color=(255, 0, 0),
            panel=str(self)
        )

        self.boutton1 = pm.ui.RectButton(
            x = self.width * 0.5, 
            y = self.height * 0.5, 
            anchor = "center",
            width = 400, 
            height = 120, 
            filling_color = (0, 0, 0), 
            filling_color_hover = (46, 46, 46),
            border_radius = 20,
            text = "REJOUER",
            font_color=(255, 255, 255),
            hover_scale_ratio=1.05,
            hover_scale_duration=0.05,
            callback = self.handle_start, 
            panel = str(self)
            )
        
        self.boutton2 = pm.ui.RectButton(
            x = self.width * 0.5, 
            y = self.height * 0.7, 
            anchor = "center",
            width = 400, 
            height = 120,
            filling_color = (0, 0, 0),
            filling_color_hover = (46, 46, 46),
            border_radius = 20,
            text = "RETOUR AU CHOIX",
            font_color=(255, 255, 255),
            hover_scale_ratio=1.05,
            hover_scale_duration=0.05,
            callback = self.handle_start2,
            panel = str(self)
            )
    
    def draw_back(self, surface):
        surface.fill(self.background)
        return super().draw_back(surface)
    
    def handle_start(self):
        pm.states.activate("Morpion")
    
    def handle_start2(self):
        pm.states.activate("choix")

    def set_winner(self, winner):
        if winner == -1:
            self.title.text = "Egalité !"
        else:
            self.title.text = f"Le gagnant est : Joueur {winner}"