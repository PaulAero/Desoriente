


## Définition classe horizon artificiel

class HorizonArtificiel:

    def __init__(self):

        import tkinter as tk
        import math as m
        self.root2 = tk.Tk()
        self.root2.attributes('-fullscreen', True)
        self.root2.bind('<Escape>',lambda e: self.root2.destroy())
        self.canvas2 = tk.Canvas(self.root2, width=self.root2.winfo_screenwidth(), height=self.root2.winfo_screenheight(), borderwidth=0, highlightthickness=0, bg="black")
        self.canvas2.grid()

    def _create_circle(self, x, y, r, **kwargs):
        return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)


    import tkinter as tk
    tk.Canvas.create_circle = _create_circle

    # Partie Horizon
    def horizon(self):

        import math as m

        # Blocs

        self.centre_abscisse=self.root2.winfo_screenwidth()/2
        self.centre_ordonnee=self.root2.winfo_screenheight()/2
        longueur_rectangle=self.root2.winfo_screenheight()*2/3
        largeur_rectangle=self.root2.winfo_screenheight()*2/3
        x1=self.centre_abscisse-longueur_rectangle/2
        y1=self.centre_ordonnee+largeur_rectangle/2
        x2=self.centre_abscisse+longueur_rectangle/2
        y2=self.centre_ordonnee-largeur_rectangle/2

        self.canvas2.create_rectangle(x1,y1,x2,(y1+y2)/2, fill="maroon")
        self.canvas2.create_rectangle(x1,(y1+y2)/2,x2,y2, fill="sky blue")

        # Graduations horizontales

        self.canvas2.create_line(x1, (y1+y2)/2, x2,(y1+y2)/2,fill='#DDD',width=4) #CENTRALE

        ecart_dizaines=(y1-(y1+y2)/2)*2/5

        for i in [-1,1]:#GRADUATION
            self.canvas2.create_line(x1+(x2-x1)/3, (y1+y2)/2+ecart_dizaines*i, x1+(x2-x1)*2/3,(y1+y2)/2+ecart_dizaines*i,fill='#DDD',width=4)
            self.canvas2.create_text(x1+(x2-x1)/4,(y1+y2)/2+ecart_dizaines*i,text='10',fill='#DDD',font='bold')
            self.canvas2.create_text(x2-(x2-x1)/4,(y1+y2)/2+ecart_dizaines*i,text='10',fill='#DDD',font='bold')


        for i in [-1/2,-3/2,1/2,3/2]:#DEMI GRADUATION
            self.canvas2.create_line(x1+(x2-x1)*2/5, (y1+y2)/2+ecart_dizaines*i, x1+(x2-x1)*3/5,(y1+y2)/2+ecart_dizaines*i,fill='#DDD',width=4)


        for i in [-1/4,1/4,-3/4,-5/4,-7/4,3/4,5/4,7/4]: #QUARTS DE GRADUATION
            self.canvas2.create_line(x1+(x2-x1)*5/11, (y1+y2)/2+ecart_dizaines*i, x1+(x2-x1)*6/11,(y1+y2)/2+ecart_dizaines*i,fill='#DDD',width=4)


        # Graduations arc de cercle

        for i in [2,4,5,13]: #GRANDES
            self.canvas2.create_line(self.centre_abscisse-0.44*largeur_rectangle*m.cos(i*m.pi/6),self.centre_ordonnee-0.44*largeur_rectangle*m.sin(i*m.pi/6),self.centre_abscisse-0.49*largeur_rectangle*m.cos(i*m.pi/6),self.centre_ordonnee-0.49*largeur_rectangle*m.sin(i*m.pi/6),fill='#DDD', width=3)


        for i in [7,8,10,11]: #PETITES
            self.canvas2.create_line(self.centre_abscisse-0.44*largeur_rectangle*m.cos(i*m.pi/18),self.centre_ordonnee-0.44*largeur_rectangle*m.sin(i*m.pi/18),self.centre_abscisse-0.46*largeur_rectangle*m.cos(i*m.pi/18),self.centre_ordonnee-0.46*largeur_rectangle*m.sin(i*m.pi/18),fill='#DDD', width=3)



        for i in [3,9]: #MOYENNES
            self.canvas2.create_line(self.centre_abscisse-0.44*largeur_rectangle*m.cos(i*m.pi/12),self.centre_ordonnee-0.44*largeur_rectangle*m.sin(i*m.pi/12),self.centre_abscisse-0.46*largeur_rectangle*m.cos(i*m.pi/12),self.centre_ordonnee-0.46*largeur_rectangle*m.sin(i*m.pi/12),fill='#DDD', width=3)


        # Création triangle du zéro

        self.canvas2.create_polygon(self.centre_abscisse*0.98,y2*1.05,self.centre_abscisse*1.02,y2*1.05,self.centre_abscisse,y2*1.2, fill='#DDD')


    def creation_affichage_num_alti(self,largeur_case,longueur_case,centre_abscisse,centre_ordonnee,x1,valeur_alti):
        self.canvas2.create_rectangle(centre_abscisse-largeur_case/2,centre_ordonnee-longueur_case/2,centre_abscisse+largeur_case/2,centre_ordonnee+longueur_case/2, fill="grey",width=4)
        self.canvas2.create_polygon(centre_abscisse-largeur_case/2,(centre_ordonnee-longueur_case/2)*1.02,centre_abscisse-largeur_case/2,(centre_ordonnee+longueur_case/2)*0.98,(centre_abscisse-largeur_case/2)*0.99,centre_ordonnee, fill='black')
        self.canvas2.create_line((centre_abscisse-largeur_case/2)*0.99,centre_ordonnee,x1,centre_ordonnee, fill='black', width=2, dash=(10,20))
        ecartement=largeur_case/6
        unite=valeur_alti%10
        dizaine=(valeur_alti//10)%10
        centaine=(valeur_alti//100)%10
        millier=(valeur_alti//1000)%10
        dizaine_millier=(valeur_alti//10000)%10
        self.canvas2.create_text(centre_abscisse+largeur_case/2-ecartement,centre_ordonnee,text=str(unite),fill='#DDD',font='bold')
        self.canvas2.create_text(centre_abscisse+largeur_case/2-ecartement*2,centre_ordonnee,text=str(dizaine),fill='#DDD',font='bold')
        self.canvas2.create_text(centre_abscisse+largeur_case/2-ecartement*3,centre_ordonnee,text=str(centaine),fill='#DDD',font='bold')
        self.canvas2.create_text(centre_abscisse+largeur_case/2-ecartement*4,centre_ordonnee,text=str(millier),fill='#DDD',font='bold')
        self.canvas2.create_text(centre_abscisse+largeur_case/2-ecartement*5,centre_ordonnee,text=str(dizaine_millier),fill='#DDD',font='bold')


    def altimetre(self):

        import tkinter as tk

        valeur_altitude=12345
        # Bloc
        longueur_rectangle=self.root2.winfo_screenheight()*2/3
        largeur_rectangle=self.root2.winfo_screenheight()*2/3
        centre_altitude_abscisse=longueur_rectangle+((self.root2.winfo_screenwidth()-longueur_rectangle)/2)*4/3
        centre_altitude_ordonnee=self.root2.winfo_screenheight()/2
        longueur_altitude_rectangle=self.root2.winfo_screenheight()*8/9
        largeur_altitude_rectangle=self.root2.winfo_screenheight()/5
        x1=centre_altitude_abscisse-largeur_altitude_rectangle/2
        y1=centre_altitude_ordonnee+longueur_altitude_rectangle/2
        x2=centre_altitude_abscisse+largeur_altitude_rectangle/2
        y2=centre_altitude_ordonnee-longueur_altitude_rectangle/2

        self.canvas2.create_rectangle(x1,y1,x2,y2, fill="grey")
        self.creation_affichage_num_alti((x2-x1)/2,(x2-x1)/4,x2-(x2-x1)/4,self.root2.winfo_screenheight()/2,x1,valeur_altitude)
        # # Valeur réelle centrée
        #
        # canvas.create_line(x1,y2+(y1-y2)/2,x1+(x2-x1),y2+(y1-y2)/2, fill='#DDD', width=4)

        # Graduations

        dizaine_unite=valeur_altitude%10+10*((valeur_altitude//10)%10)
        valeur_basse=(valeur_altitude-dizaine_unite)-300
        delta_centaine_du_dessus=(valeur_altitude//100+1)*100-valeur_altitude
        for i in range(8,0,-1):
            gradient=(y1-y2)/800
            position_y=y2+(y1-y2)*i/8-delta_centaine_du_dessus*gradient
            self.canvas2.create_line(x1,position_y,x1+(x2-x1)/6,position_y, fill='#DDD', width=4)
            self.canvas2.create_text(x1+(x2-x1)*1.7 /6,position_y,text=str(int(valeur_basse)),fill='#DDD',font='bold')
            valeur_basse+=100

        # # Graduations
        #
        # for i in range(1,9):
        #     canvas.create_line(x1,(y1-y2)*i/8,x1+(x2-x1)/4,(y1-y2)*i/8, fill='#DDD', width=4)
        #     canvas.create_text(arrivee_x,arrivee_y*1.015,text=str(i-9),fill='#DDD',font='bold')


    def creation_affichage_num_anemo(self,largeur_case,longueur_case,centre_abscisse,centre_ordonnee,x2,valeur_anemo):
        self.canvas2.create_rectangle(centre_abscisse-largeur_case/2,centre_ordonnee-longueur_case/2,centre_abscisse+largeur_case/2,centre_ordonnee+longueur_case/2, fill="grey",width=4)
        self.canvas2.create_polygon(centre_abscisse+largeur_case/2,(centre_ordonnee-longueur_case/2)*1.02,centre_abscisse+largeur_case/2,(centre_ordonnee+longueur_case/2)*0.98,(centre_abscisse+largeur_case/2)*1.04,centre_ordonnee, fill='black')
        # Valeur réelle centrée

        self.canvas2.create_line((centre_abscisse+largeur_case/2)*1.04,centre_ordonnee,x2,centre_ordonnee, fill='black', width=2, dash=(10,20))

        # Chiffres
        ecartement=largeur_case/6
        unite=valeur_anemo%10
        dizaine=(valeur_anemo//10)%10
        centaine=(valeur_anemo//100)%10
        millier=(valeur_anemo//1000)%10
        dizaine_millier=(valeur_anemo//10000)%10
        self.canvas2.create_text(centre_abscisse+largeur_case/2-ecartement,centre_ordonnee,text=str(unite),fill='#DDD',font='bold')
        self.canvas2.create_text(centre_abscisse+largeur_case/2-ecartement*2,centre_ordonnee,text=str(dizaine),fill='#DDD',font='bold')
        self.canvas2.create_text(centre_abscisse+largeur_case/2-ecartement*3,centre_ordonnee,text=str(centaine),fill='#DDD',font='bold')
        self.canvas2.create_text(centre_abscisse+largeur_case/2-ecartement*4,centre_ordonnee,text=str(millier),fill='#DDD',font='bold')
        self.canvas2.create_text(centre_abscisse+largeur_case/2-ecartement*5,centre_ordonnee,text=str(dizaine_millier),fill='#DDD',font='bold')

    def anemometre(self):

        valeur_vitesse=1120
        # Bloc
        longueur_rectangle=self.root2.winfo_screenheight()*2/3
        largeur_rectangle=self.root2.winfo_screenheight()*2/3
        centre_vitesse_abscisse=((self.root2.winfo_screenwidth()-longueur_rectangle)/2)*2/3
        centre_vitesse_ordonnee=self.root2.winfo_screenheight()/2
        longueur_vitesse_rectangle=self.root2.winfo_screenheight()*8/9
        largeur_vitesse_rectangle=self.root2.winfo_screenheight()/5
        x1=centre_vitesse_abscisse-largeur_vitesse_rectangle/2
        y1=centre_vitesse_ordonnee+longueur_vitesse_rectangle/2
        x2=centre_vitesse_abscisse+largeur_vitesse_rectangle/2
        y2=centre_vitesse_ordonnee-longueur_vitesse_rectangle/2

        self.canvas2.create_rectangle(x1,y1,x2,y2, fill="grey")
        self.creation_affichage_num_anemo((x2-x1)/2,(x2-x1)/4,x1+(x2-x1)/4,self.root2.winfo_screenheight()/2,x2,valeur_vitesse)



        # Graduations

        unite=valeur_vitesse%10
        valeur_trait=(valeur_vitesse-unite)-50
        delta_dizaine_du_dessus=(valeur_vitesse//10+1)*10-valeur_vitesse
        for i in range(12,0,-1):
            gradient=(y1-y2)/120
            position_y=y2+(y1-y2)*i/12-delta_dizaine_du_dessus*gradient
            self.canvas2.create_line(x2-(x2-x1)/6,position_y,x2,position_y, fill='#DDD', width=4)
            self.canvas2.create_text((x2-(x2-x1)/6)*0.95,position_y,text=str(int(valeur_trait)),fill='#DDD',font='bold')
            valeur_trait+=10


        # # Graduations
        # for i in range(1,13):
        #     canvas.create_line(x2-(x2-x1)/4,(y1-y2)*i/12,x2,(y1-y2)*i/12, fill='#DDD', width=4)


##CAP MOUVEMENT LE 7/01

    def cap_magnetique(self):

        import math as m

        valeur_cap=31
        affichage_cap=valeur_cap/10


        # Bloc

        self.canvas2.create_circle(self.centre_abscisse, self.root2.winfo_screenheight()*6/5,self.root2.winfo_screenheight()/3,fill='grey')

        # Création triangle d'indication

        self.canvas2.create_polygon(self.centre_abscisse-self.root2.winfo_screenwidth()*1/100,self.root2.winfo_screenheight()*6/5-self.root2.winfo_screenheight()/3-self.root2.winfo_screenwidth()*1/100,self.centre_abscisse+self.root2.winfo_screenwidth()*1/100,self.root2.winfo_screenheight()*6/5-self.root2.winfo_screenheight()/3-self.root2.winfo_screenwidth()*1/100,self.centre_abscisse,self.root2.winfo_screenheight()*6/5-self.root2.winfo_screenheight()/3, fill='#DDD')

# #         # Graduations
# #
# #         for i in range(9,45):#GRANDES
# #             i+=affichage_cap
# #             depart_x=self.centre_abscisse-root.winfo_screenheight()/3*m.cos(i*m.pi/18)
# #             depart_y=root.winfo_screenheight()*6/5-root.winfo_screenheight()/3*m.sin(i*m.pi/18)
# #             arrivee_x=self.centre_abscisse-0.93*root.winfo_screenheight()/3*m.cos(i*m.pi/18)
# #             arrivee_y= root.winfo_screenheight()*6/5-0.93*root.winfo_screenheight()/3*m.sin(i*m.pi/18)
# #             canvas.create_line(depart_x,depart_y ,arrivee_x,arrivee_y,fill='#DDD', width=3)
# #             canvas.create_text(arrivee_x,arrivee_y*1.015,text=str(i-9),fill='#DDD',font='bold')

        # Graduations

        # Valeur réelle centrée

        x0=self.centre_abscisse
        depart_y0=self.root2.winfo_screenheight()*6/5-self.root2.winfo_screenheight()/3
        arrivee_y0= self.root2.winfo_screenheight()*6/5
        self.canvas2.create_line(x0,depart_y0 ,x0,arrivee_y0,fill='#DDD', width=3)
        self.canvas2.create_text(x0,self.root2.winfo_screenheight()-(self.root2.winfo_screenheight()-depart_y0)/3,text=str(valeur_cap),fill='red',font='Times 20 bold')


        for i in range(9,45):#GRANDES
            depart_x=self.centre_abscisse-self.root2.winfo_screenheight()/3*m.cos(i*m.pi/18-valeur_cap*m.pi/180)
            depart_y=self.root2.winfo_screenheight()*6/5-self.root2.winfo_screenheight()/3*m.sin(i*m.pi/18-valeur_cap*m.pi/180)
            arrivee_x=self.centre_abscisse-0.93*self.root2.winfo_screenheight()/3*m.cos(i*m.pi/18-valeur_cap*m.pi/180)
            arrivee_y= self.root2.winfo_screenheight()*6/5-0.93*self.root2.winfo_screenheight()/3*m.sin(i*m.pi/18-valeur_cap*m.pi/180)
            self.canvas2.create_line(depart_x,depart_y ,arrivee_x,arrivee_y,fill='#DDD', width=3)
            self.canvas2.create_text(arrivee_x,arrivee_y*1.015,text=str(i-9),fill='#DDD',font='bold')


        for i in range(1,72,2):#PETITES
            depart_x=self.centre_abscisse-self.root2.winfo_screenheight()/3*m.cos(i*m.pi/36-valeur_cap*m.pi/180)
            depart_y= self.root2.winfo_screenheight()*6/5-self.root2.winfo_screenheight()/3*m.sin(i*m.pi/36-valeur_cap*m.pi/180)
            arrivee_x=self.centre_abscisse-0.95*self.root2.winfo_screenheight()/3*m.cos(i*m.pi/36-valeur_cap*m.pi/180)
            arrivee_y=self.root2.winfo_screenheight()*6/5-0.95*self.root2.winfo_screenheight()/3*m.sin(i*m.pi/36-valeur_cap*m.pi/180)
            self.canvas2.create_line(depart_x,depart_y,arrivee_x, arrivee_y,fill='#DDD', width=3)

    def horizon_artificiel(self):
        self.horizon()
        self.altimetre()
        self.anemometre()
        self.cap_magnetique()
        self.bouton_horizon()
        self.root2.wm_title("Horizon artificiel")
        self.root2.mainloop()



##                                           Creation du bouton vers le variometre

    def dessiner_vario(self):
        import sys
        sys.path.append("D:\FAC\L3\Projet\dev_1")
        import Variometre_classe
        from Variometre_classe import Variometre
        monVario=Variometre()
        monVario.tracer_le_variometre()

    def bouton_horizon (self):
        import tkinter as tk
        hauteur_bouton=self.root2.winfo_screenheight()//150
        largeur_bouton=self.root2.winfo_screenheight()//50
        bouton = tk.Button (self.root2,text = "Vers le Variomètre",fg="white",bg="red",height = hauteur_bouton, width = largeur_bouton,command=lambda:self.dessiner_vario())
        ordonnee_bouton=(self.root2.winfo_screenheight()//2)-(self.root2.winfo_screenheight()//30)
        bouton.place(x=self.root2.winfo_screenwidth()-((self.root2.winfo_screenwidth()//10)+largeur_bouton), y=ordonnee_bouton)



##

mon_horizon_artificiel=HorizonArtificiel()
mon_horizon_artificiel.horizon_artificiel()

