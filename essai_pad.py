class UtilisationPad:

    def __init__(self):

        import tkinter as tk
        import math as m
        self.root2 = tk.Tk()
        self.root2.attributes('-fullscreen', True)
        self.root2.bind('<Escape>',lambda e: self.root2.destroy())
        self.canvas2 = tk.Canvas(self.root2, width=self.root2.winfo_screenwidth(), height=self.root2.winfo_screenheight(), borderwidth=0, highlightthickness=0, bg="black")
        self.canvas2.grid()


    def afficher_pad(self):
        import sys
        import PyQt5
        import functools
        sys.path.append("D:\FAC\L3\Projet")
        import pad_numerique_deux
        from pad_numerique_deux import AppView
        monPad=AppView()
        monPad.__init__()


    def bouton_pad (self):
        import tkinter as tk
        hauteur_bouton=self.root2.winfo_screenheight()//150
        largeur_bouton=self.root2.winfo_screenheight()//50
        bouton = tk.Button (self.root2,text = "Click to show the pad",fg="white",bg="grey",height = hauteur_bouton, width = largeur_bouton,command=lambda:self.afficher_pad())
        ordonnee_bouton=(self.root2.winfo_screenheight()//2)-(self.root2.winfo_screenheight()//30)
        bouton.place(x=self.root2.winfo_screenwidth()//2-largeur_bouton, y=ordonnee_bouton)


    def ouvrir_fenetre(self):
        self.bouton_pad()
        self.root2.mainloop()

fenetre_essai=UtilisationPad()
fenetre_essai.ouvrir_fenetre()

