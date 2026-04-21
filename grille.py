import pygame
import pygame_manager as pm

class Grille :
    def __init__(self, x, y, taille_case, panel):
        self.x = x
        self.y = y
        self.case = taille_case
        self.panel = panel
        self.tab = [[0 for _ in range(3)] for _ in range(3)]
        self.symboles = {
            "croix" : 1,
            "cercle" : 2
        }
        self.objets = []
        self.tour = self.symboles["croix"]
    
    def placer(self, x, y):
        if self.tab[x][y] != 0 :
            return
        self.tab[x][y] = self.tour
        self.generer(self.tour, x, y)
        self.tour = int(((self.tour * 2 - 3) * -1 + 3) / 2)
        resultat = self.verif_end(self.symboles.values())
        if resultat == 0 :
            return 
        elif resultat == -1 :
            print(" Aucun gagnant ")
        else : 
            print(" Le gagnant est : ", resultat)

    def verif_lignes(self, symbole):
        for ligne in self.tab:
            if all(case == symbole for case in ligne):
                return True
        return False

    def verif_collonnes(self, symbole):
        for collonne in range(3):
            if all(self.tab[ligne][collonne] == symbole for ligne in range(3)):
                return True
        return False

    def verif_diags(self, symbole):
        if all(self.tab[i][i] == symbole for i in range(3)):
            return True
        if all(self.tab[i][2 - i] == symbole for i in range(3)):
            return True
        return False

    def verif_gagnant(self, symbole):
        return self.verif_lignes(symbole) or self.verif_collonnes(symbole) or self.verif_diags(symbole)

    def verif_end(self, symboles):
        for symbole in symboles:
            if self.verif_gagnant(symbole):
                return symbole
        if all(case != 0 for ligne in self.tab for case in ligne):
            return -1
        return 0

    def generer(self, symbole, x, y):
        type_objet = Croix if symbole == self.symboles["croix"] else Cercle
        objet = type_objet(self.x + (x + 0.5) * self.case, self.y + (y + 0.5) * self.case, self.panel)
        self.objets.append(objet)

    def nettoyer(self):
        for objet in self.objets :
            objet.destroy()
        self.tab = [[0 for _ in range(3)] for _ in range(3)]

class BaseEntity :
    def __init__(self, x, y, panel):
        self.x = x
        self.y = y
        self.panel = panel
        self.image = None

    def destroy(self):
        if self.image is not None :
            self.image.kill()

class Croix(BaseEntity) :
    def __init__(self, x, y, panel):
        super().__init__(x, y, panel) 
        
        self.image = pm.ui.Image(
            x = self.x,
            y = self.y,
            image_path = "croix.png",
            width = 200,
            height = 200,
            anchor = "center",
            panel = str(panel),
            zorder = 1
        )

class Cercle(BaseEntity) :
    def __init__(self, x, y, panel):
        super().__init__(x, y, panel)
        
        self.image = pm.ui.Image(
            x = self.x,
            y = self.y,
            image_path = "cercle.png",
            width = 200,
            height = 200,
            anchor = "center",
            panel = str(panel),
            zorder = 1
        )