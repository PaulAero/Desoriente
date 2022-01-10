from tkinter import *
from sense_emu import SenseHat

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

#initilaisation des capteurs
sense = SenseHat()
sense.set_imu_config(True, True, True)

#presentation des resultats des différetns capteurs
presentation = Label(fen, bg = '#ffffff',text = "Values returned by the sensors")
presentation.place(x = largeur//2,y = (longueur//8), anchor=CENTER)
#la pression
pressure = sense.get_pressure()
pression = Label(fen, bg = '#ffffff',text = "Pressure: %s Millibars" % pressure)
pression.place(x = largeur//2, y = (longueur//6), anchor=CENTER)
#compass
north = sense.get_compass()
compass = Label(fen, bg = '#ffffff',text = "North: %s" % north)
compass.place(x = largeur//2, y = ((longueur//6)+longueur//40), anchor=CENTER)
#accelerometre
accel = sense.get_accelerometer_raw()
accelero = Label(fen, bg = '#ffffff',text = "Accelerometer in Gs x: {x}, y: {y}, z: {z}".format(**accel))
accelero.place(x = largeur//2, y = ((longueur//6)+2*longueur//40), anchor=CENTER)
#gyroscope
orientation = sense.get_orientation_degrees()
gyro = Label(fen, bg = '#ffffff',text = "Orientation in degrees p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))
gyro.place(x = largeur//2, y = ((longueur//6)+3*longueur//40), anchor=CENTER)

#bouton valider
valider = Button(fen, bg = '#32CD32', fg = '#ffffff', text="Confirm", width=20, command = lambda:exec(open("horizon_artificiel.py").read(), globals()))
valider.place(x = largeur//2, y = (longueur//6)+5*longueur//40, anchor=CENTER)

#gestion de la zone de commentaire
def enregistrer_commentaire(textcomment) :
    fichier = open("comment.txt", "w")
    saisi = textcomment.get("1.0", "end-1c")
    #print("saisi: ",saisi)
    fichier.write(saisi)
    fichier.close()

presentation_zone_commentaire = Label(fen, bg = '#ffffff', text="Comment section")
presentation_zone_commentaire.place(x = largeur//2, y = (longueur//6)+7*longueur//40, anchor=CENTER)
commentaire = Text(fen, width = largeur//20, height = longueur//80)
commentaire.focus()
commentaire.place(x = largeur//2, y = (longueur//6)+12*longueur//40, anchor=CENTER)
#bouton sauvegarder
sauvegarder = Button(fen, bg = '#0000FF', fg = '#ffffff', text = "Save", width = 15, command = lambda:enregistrer_commentaire(commentaire))
sauvegarder.place(x = largeur//2 - largeur//10, y = (longueur//6)+18*longueur//40, anchor=CENTER)
effacer = Button(fen, bg = '#B22222', fg = '#ffffff', text = "Effacer", width = 15, command = lambda:commentaire.delete("1.0", "end"))
effacer.place(x = largeur//2 + largeur//10, y = (longueur//6)+18*longueur//40, anchor=CENTER)

fen.mainloop()
