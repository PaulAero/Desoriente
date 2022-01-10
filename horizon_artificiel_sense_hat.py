import tkinter as tk
import math as m
from sense_emu import SenseHat

## initilaisation des capteurs
sense = SenseHat()
sense.set_imu_config(True, True, True)

## Root

root = tk.Tk()
root.attributes('-fullscreen', True)
root.bind('<Escape>',lambda e: root.destroy())

## Création du canva

canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), borderwidth=0, highlightthickness=0, bg="black")
canvas.grid()


## Définition classe horizon artificiel

class HorizonArtificiel:

    def _create_circle(self, x, y, r, **kwargs):
        return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
    tk.Canvas.create_circle = _create_circle

    # Partie Horizon
    def horizon(self):
        # Blocs
        self.centre_abscisse=root.winfo_screenwidth()/2
        self.centre_ordonnee=root.winfo_screenheight()/2       
        longueur_rectangle=root.winfo_screenheight()*2/3
        largeur_rectangle=root.winfo_screenheight()*2/3      
        x1=self.centre_abscisse-longueur_rectangle/2
        y1=self.centre_ordonnee+largeur_rectangle/2
        x2=self.centre_abscisse+longueur_rectangle/2
        y2=self.centre_ordonnee-largeur_rectangle/2
        
        #echelle
        ecart_dizaines=(y1-(y1+y2)/2)*2/5
        
        # recuperation de notre orientation
        orientation = sense.get_orientation_degrees()
        
        if orientation['pitch'] < 180:
            tangage = orientation['pitch']*ecart_dizaines/10
        else:
            tangage = (orientation['pitch']-360)*ecart_dizaines/10
        
        if orientation['roll'] < 180:
            roulis = orientation['roll']*0.44*largeur_rectangle*m.cos(m.pi/6)/30
        else:
            roulis = (orientation['roll']-360)*0.44*largeur_rectangle*m.cos(m.pi/6)/10
        
        #canvas.create_polygon((x1,y1), (x1,(y1+y2)/2 - tangage), (x2,(y1+y2)/2 - tangage), (x2, y1), fill="maroon")
        canvas.create_polygon((x1,y1), (x1,(y1+y2)/2 - (tangage-roulis/2)), (x2,(y1+y2)/2 - (tangage+roulis/2)), (x2, y1), fill="maroon")
        #canvas.create_polygon((x1,(y1+y2)/2 - tangage),(x1, y2),(x2,y2), (x2, (y1+y2)/2 - tangage), fill="sky blue")
        canvas.create_polygon((x1,(y1+y2)/2 - (tangage-roulis/2)),(x1, y2),(x2,y2), (x2, (y1+y2)/2 - (tangage+roulis/2)), fill="sky blue")
        
        # Graduations horizontales

        canvas.create_line(x1, (y1+y2)/2, x2,(y1+y2)/2,fill='#DDD',width=4) #CENTRALE

        for i in [-1,1]:#GRADUATION
            canvas.create_line(x1+(x2-x1)/3, (y1+y2)/2+ecart_dizaines*i, x1+(x2-x1)*2/3,(y1+y2)/2+ecart_dizaines*i,fill='#DDD',width=4)
            canvas.create_text(x1+(x2-x1)/4,(y1+y2)/2+ecart_dizaines*i,text='10',fill='#DDD',font='bold')
            canvas.create_text(x2-(x2-x1)/4,(y1+y2)/2+ecart_dizaines*i,text='10',fill='#DDD',font='bold')


        for i in [-1/2,-3/2,1/2,3/2]:#DEMI GRADUATION
            canvas.create_line(x1+(x2-x1)*2/5, (y1+y2)/2+ecart_dizaines*i, x1+(x2-x1)*3/5,(y1+y2)/2+ecart_dizaines*i,fill='#DDD',width=4)


        for i in [-1/4,1/4,-3/4,-5/4,-7/4,3/4,5/4,7/4]: #QUARTS DE GRADUATION
            canvas.create_line(x1+(x2-x1)*5/11, (y1+y2)/2+ecart_dizaines*i, x1+(x2-x1)*6/11,(y1+y2)/2+ecart_dizaines*i,fill='#DDD',width=4)


        # Graduations arc de cercle

        for i in [2,4,5,13]: #GRANDES
            canvas.create_line(self.centre_abscisse-0.44*largeur_rectangle*m.cos(i*m.pi/6),self.centre_ordonnee-0.44*largeur_rectangle*m.sin(i*m.pi/6),self.centre_abscisse-0.49*largeur_rectangle*m.cos(i*m.pi/6),self.centre_ordonnee-0.49*largeur_rectangle*m.sin(i*m.pi/6),fill='#DDD', width=3)


        for i in [7,8,10,11]: #PETITES
            canvas.create_line(self.centre_abscisse-0.44*largeur_rectangle*m.cos(i*m.pi/18),self.centre_ordonnee-0.44*largeur_rectangle*m.sin(i*m.pi/18),self.centre_abscisse-0.46*largeur_rectangle*m.cos(i*m.pi/18),self.centre_ordonnee-0.46*largeur_rectangle*m.sin(i*m.pi/18),fill='#DDD', width=3)



        for i in [3,9]: #MOYENNES
            canvas.create_line(self.centre_abscisse-0.44*largeur_rectangle*m.cos(i*m.pi/12),self.centre_ordonnee-0.44*largeur_rectangle*m.sin(i*m.pi/12),self.centre_abscisse-0.46*largeur_rectangle*m.cos(i*m.pi/12),self.centre_ordonnee-0.46*largeur_rectangle*m.sin(i*m.pi/12),fill='#DDD', width=3)


        # Création triangle du zéro

        canvas.create_polygon(self.centre_abscisse*0.98,y2*1.05,self.centre_abscisse*1.02,y2*1.05,self.centre_abscisse,y2*1.2, fill='#DDD')

    def altimetre(self):
        # Bloc
        longueur_rectangle=root.winfo_screenheight()*2/3
        largeur_rectangle=root.winfo_screenheight()*2/3
        centre_altitude_abscisse=longueur_rectangle+((root.winfo_screenwidth()-longueur_rectangle)/2)*4/3
        centre_altitude_ordonnee=root.winfo_screenheight()/2
        longueur_altitude_rectangle=root.winfo_screenheight()*8/9
        largeur_altitude_rectangle=root.winfo_screenheight()/5
        x1=centre_altitude_abscisse-largeur_altitude_rectangle/2
        y1=centre_altitude_ordonnee+longueur_altitude_rectangle/2
        x2=centre_altitude_abscisse+largeur_altitude_rectangle/2
        y2=centre_altitude_ordonnee-longueur_altitude_rectangle/2

        canvas.create_rectangle(x1,y1,x2,y2, fill="grey")

        # Graduations

        for i in range(1,9):
            canvas.create_line(x1,(y1-y2)*i/8,x1+(x2-x1)/4,(y1-y2)*i/8, fill='#DDD', width=4)

    def anemometre(self):
        # Bloc
        longueur_rectangle=root.winfo_screenheight()*2/3
        largeur_rectangle=root.winfo_screenheight()*2/3
        centre_vitesse_abscisse=((root.winfo_screenwidth()-longueur_rectangle)/2)*2/3
        centre_vitesse_ordonnee=root.winfo_screenheight()/2
        longueur_vitesse_rectangle=root.winfo_screenheight()*8/9
        largeur_vitesse_rectangle=root.winfo_screenheight()/5
        x1=centre_vitesse_abscisse-largeur_vitesse_rectangle/2
        y1=centre_vitesse_ordonnee+longueur_vitesse_rectangle/2
        x2=centre_vitesse_abscisse+largeur_vitesse_rectangle/2
        y2=centre_vitesse_ordonnee-longueur_vitesse_rectangle/2

        canvas.create_rectangle(x1,y1,x2,y2, fill="grey")

        # Graduations
        for i in range(1,13):
            canvas.create_line(x2-(x2-x1)/4,(y1-y2)*i/12,x2,(y1-y2)*i/12, fill='#DDD', width=4)

    def cap_magnetique(self):
        # Bloc

        canvas.create_circle(self.centre_abscisse, root.winfo_screenheight()*6/5,root.winfo_screenheight()/3,fill='grey')

        # Graduations

        for i in range(2,8):#GRANDES
            canvas.create_line(self.centre_abscisse-root.winfo_screenheight()/3*m.cos(i*m.pi/9), root.winfo_screenheight()*6/5-root.winfo_screenheight()/3*m.sin(i*m.pi/9),self.centre_abscisse-0.93*root.winfo_screenheight()/3*m.cos(i*m.pi/9), root.winfo_screenheight()*6/5-0.93*root.winfo_screenheight()/3*m.sin(i*m.pi/9),fill='#DDD', width=3)

        for i in range(5,15,2):#PETITES
            canvas.create_line(self.centre_abscisse-root.winfo_screenheight()/3*m.cos(i*m.pi/18), root.winfo_screenheight()*6/5-root.winfo_screenheight()/3*m.sin(i*m.pi/18),self.centre_abscisse-0.95*root.winfo_screenheight()/3*m.cos(i*m.pi/18), root.winfo_screenheight()*6/5-0.95*root.winfo_screenheight()/3*m.sin(i*m.pi/18),fill='#DDD', width=3)

##

mon_horizon_artificiel=HorizonArtificiel()
mon_horizon_artificiel.horizon()
mon_horizon_artificiel.altimetre()
mon_horizon_artificiel.anemometre()
mon_horizon_artificiel.cap_magnetique()


root.wm_title("Horizon artificiel")
root.mainloop()