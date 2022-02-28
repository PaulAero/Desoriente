from tkinter import *
import tkinter.font as tkFont
from sense_hat import SenseHat
from PIL import ImageTk, Image
import os


#initialisation de la fenetre
fen = Tk()
fen.title("Test de l'ensemble des capteurs")
fen.attributes('-fullscreen', True)
#fen.attributes('-zoomed', True)
fen.bind('<Escape>',lambda e: fen.destroy())
fen['bg'] = '#ffffff'

#parametre de la fenetre
largeur = fen.winfo_screenwidth()
longueur = fen.winfo_screenheight()

#logo
img = ImageTk.PhotoImage(Image.open("logo_check.gif"))
logo = Label(fen, image = img, bg='white')
logo.place(x = largeur//10,y = (longueur//6.5), anchor=CENTER)

#initilaisation des capteurs
sense = SenseHat()
sense.set_imu_config(True, True, True)

#font
arial_font_titre = tkFont.Font(family='Arial', size = 20, weight="normal")
arial_font = tkFont.Font(family='Arial', size = 12, weight="normal")


#presentation des resultats des differents capteurs
presentation = Label(fen, bg = '#ffffff', font = arial_font_titre,text = "Values returned by the sensors")
presentation.place(x = largeur//2,y = (longueur//8), anchor=CENTER)
#la pression
pressure = sense.get_pressure()
#pression = Label(fen, bg = '#ffffff',font = arial_font,text = "Pressure: %s Millibars" % pressure)
pression = Label(fen, bg = '#ffffff',font = arial_font,text = "Pressure: %.2f Millibars" % pressure)
pression.place(x = largeur//2, y = (longueur//8+longueur//20), anchor=CENTER)
#compass
north = sense.get_compass()
compass = Label(fen, bg = '#ffffff', font = arial_font, text = "North: %.2f °" % north)
compass.place(x = largeur//2, y = ((longueur//8)+2*longueur//20), anchor=CENTER)
#accelerometre
accel = sense.get_accelerometer_raw()
accelero = Label(fen, bg = '#ffffff',font = arial_font, text = "Accelerometer in Gs x: {x: .2f}, y: {y: .2f}, z: {z: .2f}".format(**accel))
accelero.place(x = largeur//2, y = ((longueur//8)+3*longueur//20), anchor=CENTER)
#gyroscope
sense.set_imu_config(False,True,False)
orientation = sense.get_orientation_degrees()
roulis=round(orientation['pitch'],2)
tangage=round(orientation['roll']-360,2)
gyro = Label(fen, bg = '#ffffff',font = arial_font, text = "Orientation in degrees p: " +str(tangage)+ ", r: " +str(roulis)+", y: " +str(round(orientation['yaw']-97,2)))
gyro.place(x = largeur//2, y = ((longueur//8)+4*longueur//20), anchor=CENTER)
#bouton valider
valider = Button(fen, bg = '#32CD32', fg = '#ffffff', text="Confirm", width=20, command = lambda:commande_valider())
valider.place(x = largeur//2, y = (longueur//8)+14*longueur//20, anchor=CENTER)



# presentation_zone_commentaire = Label(fen, bg = '#ffffff', text="Comment section")
# presentation_zone_commentaire.place(x = largeur//2, y = (longueur//8)+9*longueur//20, anchor=CENTER)
# commentaire = Text(fen, width = largeur//20, height = longueur//80)
# commentaire.focus()
# commentaire.place(x = largeur//2, y = (longueur//8)+12*longueur//20, anchor=CENTER)
#bouton sauvegarder
# sauvegarder = Button(fen, bg = '#0000FF', fg = '#ffffff', text = "Save", width = 15, command = lambda:enregistrer_commentaire(commentaire))
# sauvegarder.place(x = largeur//2 - largeur//10, y = (longueur//6)+14*longueur//20, anchor=CENTER)
# effacer = Button(fen, bg = '#B22222', fg = '#ffffff', text = "Effacer", width = 15, command = lambda:commentaire.delete("1.0", "end"))
# effacer.place(x = largeur//2 + largeur//10, y = (longueur//6)+14*longueur//20, anchor=CENTER)
def leave_comment():
    from clavier import CreationPad
    fenetre_pad=CreationPad(fen)
comment = Button(fen, bg = 'grey', fg = '#ffffff', text = "Click here to leave a comment", width = 25, command = lambda:leave_comment())
comment.place(x = largeur//2, y = (longueur//6)+6*longueur//20, anchor=CENTER)


def commande_valider():
    fen.destroy()
        
    import horizon_artificiel
    from horizon_artificiel import HorizonArtificiel
    mon_horizon_artificiel=HorizonArtificiel()
    mon_horizon_artificiel.horizon_artificiel()
    
fen.mainloop()
