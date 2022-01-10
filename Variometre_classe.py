# import tkinter as tk
# import math as m
# # from math import *
# import sys
# sys.path.append("D:\FAC\L3\Projet")
# import new_interface_statique_horizon_artificiel_deux
# from new_interface_statique_horizon_artificiel_deux import HorizonArtificiel

# root = tk.Tk()
# root.attributes('-fullscreen', True)
# root.bind('<Escape>',lambda e: root.destroy())
#
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
# canvas = tk.Canvas(root, width=screen_width, height=screen_height, borderwidth=0, highlightthickness=0, bg="floral white")
# canvas.grid()






## Définition classe VARIOMETRE


class Variometre :




##                                                     Constructeur

    def __init__(self):
        import tkinter as tk
        import math as m
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.bind('<Escape>',lambda e: self.root.destroy())
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.canvas = tk.Canvas(self.root, width=self.screen_width, height=self.screen_height, borderwidth=0, highlightthickness=0, bg="floral white")
        self.canvas.grid()





##                                        Création du cercle au centre de l'écran
    def _create_circle(self, x, y, r, **kwargs):
        return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)

    import tkinter as tk
    tk.Canvas.create_circle = _create_circle

    def creation_du_cercle_principal(self):
        self.rayon_cercle=self.screen_height/3
        self.canvas.create_circle(self.screen_width/2, self.screen_height/2, self.screen_height/3, fill="black", outline='royal blue', width=4)




    ##                               Création des  graduations avec rotation de lignes

    def rotation_ligne(self,canvas, x0, y0, longueur, angle, couleur):
        import math as m
        angle = m.radians(angle) # math.radians permet de convertir en radian
        xf = int(x0+longueur*m.cos(angle)) #valeur de l'abscisse finale
        yf = int(y0+longueur*m.sin(angle)) #valeur de l'ordonnée finale
        canvas.create_line(x0, y0, xf, yf, width=2, fill='white') # faire une ligne

    def petites_graduations(self):
        self.rayon_cercle=self.screen_height/3
        for i in range(120,240,5):
            self.rotation_ligne(self.canvas, self.screen_width/2, self.screen_height/2, self.rayon_cercle, i, "#ff0000")
        self.canvas.create_circle(self.screen_width/2, self.screen_height/2, 9*self.rayon_cercle/10, fill="black", outline='black', width=4)


    def grandes_graduations(self):
        for i in range(0,360,30):
            self.rotation_ligne(self.canvas, self.screen_width/2, self.screen_height/2, self.rayon_cercle, i, "#ff0000")
        self.canvas.create_circle(self.screen_width/2, self.screen_height/2, 2*self.rayon_cercle/3, fill="black", outline='black', width=4)





    ##                                         Texte au centre du variomètre

    def textes_centre(self):
        C=(self.screen_width/2, self.screen_height/2)
        self.canvas.create_text(C,text ="Vertical\n Speed", fill ="white", font="Arial 14 bold")
        C=(self.screen_width/2, self.screen_height/2)
        self.canvas.create_text(C,text ="\n\n\n\n\n\n FT/min \n x1000", fill ="white", font="Arial 9 bold")





    ##                                      Chiffres au niveau des graduations

    def chiffres(self):
        import math as m
        #Chiffre 3
        abscisse_trois=(self.screen_width/2)+2*self.rayon_cercle/3
        trois=(abscisse_trois-self.screen_width/120,self.screen_height/2)
        self.canvas.create_text(trois,text ="3", fill ="white", font="Arial 13 bold")
        #Chiffre 0
        self.abscisse_zero=(self.screen_width/2)-2*self.rayon_cercle/3
        zero=(self.abscisse_zero+self.screen_width/120,self.screen_height/2)
        self.canvas.create_text(zero,text ="0", fill ="white", font="Arial 13 bold")
        #Chiffres 2
        abscisse_deux_sup=(self.screen_width/2)+m.cos(m.pi/3)*(2*self.rayon_cercle/3)
        ordonnee_deux_sup=(self.screen_height/2)-m.sin(m.pi/3)*(2*self.rayon_cercle/3)
        deux_sup=(abscisse_deux_sup-self.screen_height/120,ordonnee_deux_sup+self.screen_height/120)
        self.canvas.create_text(deux_sup,text ="2", fill ="white", font="Arial 13 bold")
        abscisse_deux_inf=(self.screen_width/2)+m.cos(m.pi/3)*(2*self.rayon_cercle/3)
        ordonnee_deux_inf=(self.screen_height/2)+m.sin(m.pi/3)*(2*self.rayon_cercle/3)
        deux_inf=(abscisse_deux_inf-self.screen_height/120,ordonnee_deux_inf-self.screen_height/120)
        self.canvas.create_text(deux_inf,text ="2", fill ="white", font="Arial 13 bold")
        #Chiffres 1
        abscisse_un_sup=(self.screen_width/2)-m.cos(m.pi/3)*(2*self.rayon_cercle/3)
        ordonnee_un_sup=(self.screen_height/2)-m.sin(m.pi/3)*(2*self.rayon_cercle/3)
        un_sup=(abscisse_un_sup,ordonnee_un_sup+self.screen_height/120)
        self.canvas.create_text(un_sup,text ="1", fill ="white", font="Arial 13 bold")
        abscisse_un_inf=(self.screen_width/2)-m.cos(m.pi/3)*(2*self.rayon_cercle/3)
        ordonnee_un_inf=(self.screen_height/2)+m.sin(m.pi/3)*(2*self.rayon_cercle/3)
        un_inf=(abscisse_un_inf+self.screen_height/120,ordonnee_un_inf)
        self.canvas.create_text(un_inf,text ="1", fill ="white", font="Arial 13 bold")
        #Chiffres 0.5
        abscisse_demi_sup=(self.screen_width/2)-m.cos(m.pi/6)*(2*self.rayon_cercle/3)
        ordonnee_demi_sup=(self.screen_height/2)-m.sin(m.pi/6)*(2*self.rayon_cercle/3)
        demi_sup=(abscisse_demi_sup+self.screen_height/110,ordonnee_demi_sup+self.screen_height/100)
        self.canvas.create_text(demi_sup,text ="0.5", fill ="white", font="Arial 10 bold")
        abscisse_demi_inf=(self.screen_width/2)-m.cos(m.pi/6)*(2*self.rayon_cercle/3)
        ordonnee_demi_inf=(self.screen_height/2)+m.sin(m.pi/6)*(2*self.rayon_cercle/3)
        demi_inf=(abscisse_demi_inf+self.screen_height/70,ordonnee_demi_inf+self.screen_height/100)
        self.canvas.create_text(demi_inf,text ="0.5", fill ="white", font="Arial 10 bold")


    def fleches(self):
        #Création flèche inf
        self.canvas.create_line ((self.abscisse_zero+self.screen_width/120, self.screen_height/2+ self.screen_height/40), (self.abscisse_zero+self.screen_width/300, self.screen_height/2+ self.screen_height/20), (self.abscisse_zero+self.screen_width/50, self.screen_height/2+ self.screen_height/12),
                                fill="grey", width=3, smooth=True,
                                arrow="last", arrowshape=(17,17,5))
        #Création flèche sup
        self.canvas.create_line ((self.abscisse_zero+self.screen_width/120, self.screen_height/2- self.screen_height/40), (self.abscisse_zero+self.screen_width/300, self.screen_height/2- self.screen_height/20), (self.abscisse_zero+self.screen_width/50, self.screen_height/2- self.screen_height/12),
                                fill="grey", width=3, smooth=True,
                                arrow="last", arrowshape=(17,17,5))
        #texte inf
        inf=(self.abscisse_zero,self.screen_height/2+ self.screen_height/25)
        self.canvas.create_text(inf,text ="DN", fill ="white", font="Arial 6 bold")
        #texte sup
        sup=(self.abscisse_zero,self.screen_height/2-self.screen_height/25)
        self.canvas.create_text(sup,text ="UP", fill ="white", font="Arial 6 bold")

    def tracer_vario_statique(self):
        self.creation_du_cercle_principal()
        self.petites_graduations()
        self.grandes_graduations()
        self.textes_centre()
        self.chiffres()
        self.fleches()



    ##                                                   Aiguille

    def rotation_ligne_aiguille(self,canvas, x0, y0, longueur, angle):
        import math as m
        angle = m.radians(angle) # math.radians permet de convertir en radian
        xf = int(x0+longueur*m.cos(angle)) #valeur de l'abscisse finale
        yf = int(y0+longueur*m.sin(angle)) #valeur de l'ordonnée finale
        canvas.create_line(x0, y0, xf, yf, width=2, fill='red') # faire une ligne

    def aiguille(self):
        vitesse=1000
        position_texte_limite=(self.screen_width/2,self.screen_height/12)
        position_texte_vitesse=(self.screen_width/2,self.screen_height/9)

        if 0<vitesse and vitesse<3000 :
            angle_vario=(vitesse*60)/(1000)
            angle_python=180+angle_vario
            self.rotation_ligne_aiguille(self.canvas, self.screen_width/2, self.screen_height/2, 3*self.rayon_cercle/6, angle_python)
            self.canvas.create_text(position_texte_vitesse,text ="Votre vitesse actuelle est de : " + str(vitesse) + "ft/min ", fill ="red", font="Courier 20")

        elif vitesse < 0 :
            angle_vario=(abs(vitesse)*60)/(1000)
            angle_python=180-angle_vario
            self.rotation_ligne_aiguille(self.canvas, self.screen_width/2, self.screen_height/2, 3*self.rayon_cercle/6, angle_python)
            self.canvas.create_text(position_texte_vitesse,text ="Votre vitesse actuelle est de : " + str(vitesse) + "ft/min ", fill ="red", font="Courier 20")

        else:
            self.canvas.create_text(position_texte_limite,text ="Limite de vitesse atteinte", fill ="orange red", font="Courier 20 bold ")
            self.rotation_ligne_aiguille(self.canvas, self.screen_width/2, self.screen_height/2, 3*self.rayon_cercle/6, 0)
            self.canvas.create_text(position_texte_vitesse,text ="Votre vitesse actuelle est de : " + str(vitesse) + "ft/min ", fill ="red", font="Courier 20")





##                                        Création du bouton vers l'horizon artificiel

    def dessiner_horizon(self):
        import sys
        sys.path.append("D:\FAC\L3\Projet\dev_1")
        import horizon_artificiel
        from horizon_artificiel import HorizonArtificiel
        mon_horizon_artificiel=HorizonArtificiel()
        mon_horizon_artificiel.horizon_artificiel()


    def bouton_vario (self):
        import tkinter as tk
        hauteur_bouton=self.screen_height//150
        largeur_bouton=self.screen_height//50
        bouton = tk.Button (self.root,text = "Vers Horizon Artificiel",fg="white",bg="grey",height = hauteur_bouton, width = largeur_bouton,command=lambda:self.dessiner_horizon())
        ordonnee_bouton=(self.screen_height//2)-(self.screen_height//30)
        bouton.place(x=self.screen_width//20, y=ordonnee_bouton)


    def tracer_le_variometre(self):
        self.tracer_vario_statique()
        self.aiguille()
        self.bouton_vario()
        self.root.mainloop()




monVario=Variometre()
monVario.tracer_le_variometre()


# monVario.tracer_vario_statique()
# monVario.aiguille()
# monVario.bouton()
# root.mainloop()