## Définition classe VARIOMETRE
class Variometre :
##                                                     Constructeur
    def __init__(self):
        import tkinter as tk
        import math as m
        from sense_hat import SenseHat
        
        ## initilaisation des capteurs
        self.sense = SenseHat()
        self.sense.clear()
        
        #Root
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.bind('<Escape>',lambda e: self.root.destroy())
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.canvas = tk.Canvas(self.root, width=self.screen_width, height=self.screen_height, borderwidth=0, highlightthickness=0, bg="black")
        self.canvas.grid()
        self.logo=tk.PhotoImage(file="logo_mini_vario.gif",master=self.root)
        self.canvas.create_image(self.screen_width-self.screen_width/15,self.screen_height-self.screen_height/9,image=self.logo,anchor=tk.CENTER)
##                                        Création du cercle au centre de l'écran
    def _create_circle(self, x, y, r, **kwargs):
        return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
    import tkinter as tk
    tk.Canvas.create_circle = _create_circle
    def creation_du_cercle_principal(self):
        self.rayon_cercle=self.screen_height/3
        self.canvas.create_circle(self.screen_width/2, self.screen_height/2, self.screen_height/3, fill="ivory2", outline='white', width=5)
    ##                               Création des  graduations avec rotation de lignes
    def rotation_ligne(self,canvas, x0, y0, longueur, angle, couleur):
        import math as m
        angle = m.radians(angle) # math.radians permet de convertir en radian
        xf = int(x0+longueur*m.cos(angle)) #valeur de l'abscisse finale
        yf = int(y0+longueur*m.sin(angle)) #valeur de l'ordonnée finale
        canvas.create_line(x0, y0, xf, yf, width=2, fill='black') # faire une ligne
    def petites_graduations(self):
        self.rayon_cercle=self.screen_height/3
        for i in range(120,240,6):
            self.rotation_ligne(self.canvas, self.screen_width/2, self.screen_height/2, self.rayon_cercle, i, "#ff0000")
        self.canvas.create_circle(self.screen_width/2, self.screen_height/2, 9*self.rayon_cercle/10, fill="ivory2", outline='ivory2', width=4)
    def grandes_graduations(self):
        for i in range(0,360,30):
            self.rotation_ligne(self.canvas, self.screen_width/2, self.screen_height/2, self.rayon_cercle, i, "#ff0000")
        self.canvas.create_circle(self.screen_width/2, self.screen_height/2, 2*self.rayon_cercle/3, fill="ivory2", outline='ivory2', width=4)
    ##                                         Texte au centre du variomètre
    def textes_centre(self):
        import tkinter.font as font
        taille_police=self.root.winfo_screenheight()//40
        taille_police_bas=self.root.winfo_screenheight()//60
        font_centre = font.Font(family='Arial',       size=taille_police, weight="bold")
        font_centre_bas = font.Font(family='Arial',       size=taille_police_bas, weight="bold")
        C=(self.screen_width/2, self.screen_height/2)
        self.canvas.create_text(C,text ="Vertical\n Speed", fill ="black", font=font_centre)
        C=(self.screen_width/2, self.screen_height/2)
        self.canvas.create_text(C,text ="\n\n\n\n\n\n FT/min \n x1000", fill ="black", font=font_centre_bas)
    ##                                      Chiffres au niveau des graduations
    def chiffres(self):
        import math as m
        import tkinter.font as font
        taille_police=self.root.winfo_screenheight()//40
        taille_police_demi=self.root.winfo_screenheight()//50
        font_graduations = font.Font(family='Arial',       size=taille_police, weight="bold")
        font_graduations_demi = font.Font(family='Arial',       size=taille_police_demi, weight="bold")
        #Chiffre 3
        abscisse_trois=(self.screen_width/2)+2*self.rayon_cercle/3
        trois=(abscisse_trois-self.screen_width/120,self.screen_height/2)
        self.canvas.create_text(trois,text ="3", fill ="black", font=font_graduations)
        #Chiffre 0
        self.abscisse_zero=(self.screen_width/2)-2*self.rayon_cercle/3
        zero=(self.abscisse_zero+self.screen_width/120,self.screen_height/2)
        self.canvas.create_text(zero,text ="0", fill ="black", font=font_graduations)
        #Chiffres 2
        abscisse_deux_sup=(self.screen_width/2)+m.cos(m.pi/3)*(2*self.rayon_cercle/3)
        ordonnee_deux_sup=(self.screen_height/2)-m.sin(m.pi/3)*(2*self.rayon_cercle/3)
        deux_sup=(abscisse_deux_sup-self.screen_height/120,ordonnee_deux_sup+self.screen_height/120)
        self.canvas.create_text(deux_sup,text ="2", fill ="black", font=font_graduations)
        abscisse_deux_inf=(self.screen_width/2)+m.cos(m.pi/3)*(2*self.rayon_cercle/3)
        ordonnee_deux_inf=(self.screen_height/2)+m.sin(m.pi/3)*(2*self.rayon_cercle/3)
        deux_inf=(abscisse_deux_inf-self.screen_height/120,ordonnee_deux_inf-self.screen_height/120)
        self.canvas.create_text(deux_inf,text ="2", fill ="black", font=font_graduations)
        #Chiffres 1
        abscisse_un_sup=(self.screen_width/2)-m.cos(m.pi/3)*(2*self.rayon_cercle/3)
        ordonnee_un_sup=(self.screen_height/2)-m.sin(m.pi/3)*(2*self.rayon_cercle/3)
        un_sup=(abscisse_un_sup,ordonnee_un_sup+self.screen_height/120)
        self.canvas.create_text(un_sup,text ="1", fill ="black", font=font_graduations)
        abscisse_un_inf=(self.screen_width/2)-m.cos(m.pi/3)*(2*self.rayon_cercle/3)
        ordonnee_un_inf=(self.screen_height/2)+m.sin(m.pi/3)*(2*self.rayon_cercle/3)
        un_inf=(abscisse_un_inf+self.screen_height/120,ordonnee_un_inf)
        self.canvas.create_text(un_inf,text ="1", fill ="black", font=font_graduations)
        #Chiffres 0.5
        abscisse_demi_sup=(self.screen_width/2)-m.cos(m.pi/6)*(2*self.rayon_cercle/3)
        ordonnee_demi_sup=(self.screen_height/2)-m.sin(m.pi/6)*(2*self.rayon_cercle/3)
        demi_sup=(abscisse_demi_sup+self.screen_height/110,ordonnee_demi_sup+self.screen_height/100)
        self.canvas.create_text(demi_sup,text ="0.5", fill ="black", font=font_graduations_demi)
        abscisse_demi_inf=(self.screen_width/2)-m.cos(m.pi/6)*(2*self.rayon_cercle/3)
        ordonnee_demi_inf=(self.screen_height/2)+m.sin(m.pi/6)*(2*self.rayon_cercle/3)
        demi_inf=(abscisse_demi_inf+self.screen_height/70,ordonnee_demi_inf+self.screen_height/100)
        self.canvas.create_text(demi_inf,text ="0.5", fill ="black", font=font_graduations_demi)
    def fleches(self):
        #Création flèche inf
        import tkinter.font as font
        taille_up_down=self.root.winfo_screenheight()//65
        font_up_down = font.Font(family='Arial',size=taille_up_down, weight="bold")
        self.canvas.create_line ((self.abscisse_zero+self.screen_width/120, self.screen_height/2+ self.screen_height/40), (self.abscisse_zero+self.screen_width/300, self.screen_height/2+ self.screen_height/20), (self.abscisse_zero+self.screen_width/50, self.screen_height/2+ self.screen_height/12),
                                fill="grey", width=3, smooth=True,
                                arrow="last", arrowshape=(15,15,5))
        #Création flèche sup
        self.canvas.create_line ((self.abscisse_zero+self.screen_width/120, self.screen_height/2- self.screen_height/40), (self.abscisse_zero+self.screen_width/300, self.screen_height/2- self.screen_height/20), (self.abscisse_zero+self.screen_width/50, self.screen_height/2- self.screen_height/12),
                                fill="grey", width=3, smooth=True,
                                arrow="last", arrowshape=(15,15,5))
        #texte inf
        inf=(self.abscisse_zero-9,self.screen_height/2+ self.screen_height/25)
        self.canvas.create_text(inf,text ="DN", fill ="midnight blue", font=font_up_down)
        #texte sup
        sup=(self.abscisse_zero-9,self.screen_height/2-self.screen_height/25)
        self.canvas.create_text(sup,text ="UP", fill ="midnight blue", font=font_up_down)
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
    
    def recuperation_vitesse(self):
        import time
        
        delta_temps=1 #en secondes, temps entre deux mesures de pression
        pression_1=self.sense.get_pressure()
        #time.sleep(delta_temps)
        pression_2=self.sense.get_pressure()
        delta_pression=pression_2-pression_1 #positif si 2>1 cad si on descend
        delta_altitude=delta_pression*(-28) #unités hPa et ft
        vitesse_verticale=delta_altitude*60/delta_temps #en ft/min
        return(vitesse_verticale)
        
            
    def aiguille(self):
        import tkinter.font as font
        
        taille_sup_haut=self.root.winfo_screenheight()//30
        taille_sup_bas=self.root.winfo_screenheight()//40
        font_sup_haut = font.Font(family='Arial',       size=taille_sup_haut, weight="bold")
        font_sup_bas = font.Font(family='Arial',       size=taille_sup_bas, weight="normal")
        vitesse=self.recuperation_vitesse()
        position_texte_limite=(self.screen_width/2,self.screen_height/12)
        position_texte_vitesse=(self.screen_width/2,self.screen_height/9)
        if 0<= vitesse and vitesse<3000 :
            angle_vario=(vitesse*60)/(1000)
            angle_python=180+angle_vario
            self.rotation_ligne_aiguille(self.canvas, self.screen_width/2, self.screen_height/2, 3*self.rayon_cercle/6, angle_python)
            vitesse = round(abs(vitesse),2)
            self.texte=self.canvas.create_text(position_texte_vitesse,text ="Your current speed is : " + str(vitesse) + " ft/min ", fill ="ivory2", font=font_sup_bas)
            
        elif vitesse < 0 and vitesse>-3000:
            angle_vario=(abs(vitesse)*60)/(1000)
            angle_python=180-angle_vario
            vitesse = round(vitesse,2)
            self.rotation_ligne_aiguille(self.canvas, self.screen_width/2, self.screen_height/2, 3*self.rayon_cercle/6, angle_python)
            self.texte=self.canvas.create_text(position_texte_vitesse,text ="Your current speed is : " + str(vitesse) + " ft/min ", fill ="ivory2", font=font_sup_bas)
            
        else:
            self.canvas.create_text(position_texte_limite,text ="Speed ​​limit reached \n", fill ="orange red", font=font_sup_haut)
            vitesse = round(vitesse,2)
            self.rotation_ligne_aiguille(self.canvas, self.screen_width/2, self.screen_height/2, 3*self.rayon_cercle/6, 0)
            self.self.canvas.create_text(position_texte_vitesse,text ="Your current speed is : " + str(vitesse) + "ft/min ", fill ="red", font=font_sup_bas)
          
##                                        Création du bouton vers l'horizon artificiel
    def dessiner_horizon(self):
        self.root.destroy()
        
        import horizon_artificiel
        from horizon_artificiel import HorizonArtificiel
        mon_horizon_artificiel=HorizonArtificiel()
        mon_horizon_artificiel.horizon_artificiel()
        
        
    def bouton_vario (self):
        import tkinter as tk
        import tkinter.font as font
        hauteur_bouton=4
        largeur_bouton=len('To Artificial Horizon')
        taille_police=self.root.winfo_screenheight()//50
        f = font.Font(family='Arial', size=taille_police, weight="bold")
        self.bouton_horizon = tk.Button (self.root,text = "To Artificial Horizon",font=f,fg="white",bg="grey",height = hauteur_bouton, width = largeur_bouton,command=lambda:self.dessiner_horizon())
        ordonnee_bouton=self.root.winfo_screenheight()/2-(hauteur_bouton+1)*taille_police
        self.bouton_horizon.place(x=(self.root.winfo_screenwidth()//50), y=ordonnee_bouton)
        self.bouton_click=True
        
        
    def ouvrir_carte_gps(self):

        self.root.destroy()
        import gps_interface
        from gps_interface import Track
        maTrace=Track()
        maTrace.create_my_track()




    def bouton_carte(self):
        import tkinter as tk
        import tkinter.font as font
        
        height_button=4
        width_button=len('To Track')
        font_size=self.root.winfo_screenheight()//50
        f = font.Font(family='Arial', size=font_size, weight="bold")
        button = tk.Button (self.root,text = "To Track",font= f,fg="white",bg="grey",height = height_button, width = width_button,command=lambda:self.ouvrir_carte_gps())
        button_vario_coordinate_y=self.root.winfo_screenheight()/2-(height_button+1)*font_size
        button.place(x=self.root.winfo_screenwidth()-((self.root.winfo_screenwidth()//10)+width_button), y=button_vario_coordinate_y)
        self.bouton_click=True


    def tracer_le_variometre(self):
        
        self.bouton_vario()
        self.bouton_carte()
        self.bouton_click=False
        while self.bouton_click==False:
            self.tracer_vario_statique()
            self.aiguille()
            self.root.update()
            self.canvas.delete(self.texte)
        self.root.mainloop()
            
        
vario=Variometre()
vario.tracer_le_variometre()