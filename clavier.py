class CreationPad:
    def __init__(self,root):
        import tkinter as tk

#         self.ws = tk.Tk()
#         self.ws.title('Keyboard')
#         self.ws.geometry('250x400+500+100')
#         self.ws.resizable(0,0)
        self.win=tk.Toplevel(root)

        # global variables
        self.word = ''
        self.bouton_entrer_click=False
        
        var = tk.StringVar()

        # frames
        
        frame_0 = tk.Frame(self.win) 
        frame_0.pack(expand=True, fill=tk.BOTH)
        
        frame_1 = tk.Frame(self.win) 
        frame_1.pack(expand=True, fill=tk.BOTH)

        frame_2 = tk.Frame(self.win)
        frame_2.pack(expand=True, fill=tk.BOTH)

        frame_3 = tk.Frame(self.win)
        frame_3.pack(expand=True, fill=tk.BOTH)

        frame_4 = tk.Frame(self.win)
        frame_4.pack(expand=True, fill=tk.BOTH)

        frame_5 = tk.Frame(self.win)
        frame_5.pack(expand=True, fill=tk.BOTH)
        # label
        self.scr_lbl = tk.Label(
            frame_1,
            textvariable='',
            font=('Arial', 20),
            anchor = tk.SE,
            bg = '#595954',
            fg = 'white' 
            )

        self.scr_lbl.pack(expand=True, fill=tk.BOTH)

        key_1 = tk.Button(
            frame_0,
            text='1',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display2(1)
            )

        key_1.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        key_2 = tk.Button(
            frame_0,
            text='2',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display2(2)
            )

        key_2.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        key_3 = tk.Button(
            frame_0,
            text='3',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display2(3)
            )

        key_3.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)



        key_4 = tk.Button(
            frame_0,
            text='4',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display2(4)
            )

        key_4.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        key_5 = tk.Button(
            frame_0,
            text='5',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display2(5)
            )

        key_5.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        key_6 = tk.Button(
            frame_0,
            text='6',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display2(6)
            )

        key_6.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)



        key_7 = tk.Button(
            frame_0,
            text='7',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display2(7)
            )

        key_7.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        key_8 = tk.Button(
            frame_0,
            text='8',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display2(8)
            )

        key_8.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        key_9 = tk.Button(
            frame_0,
            text='9',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display2(9)
            )

        key_9.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)




        key_0 = tk.Button(
            frame_0,
            text='0',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display2(0)
            )

        key_0.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        # buttons
        key_a = tk.Button(
            frame_1,
            text='a',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display('a')
            )

        key_a.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        key_z = tk.Button(
            frame_1,
            text='z',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display('z')
            )

        key_z.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        key_e = tk.Button(
            frame_1,
            text='e',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display('e')
            )

        key_e.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)



        key_r = tk.Button(
            frame_1,
            text='r',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display('r')
            )

        key_r.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        key_t = tk.Button(
            frame_1,
            text='t',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display('t')
            )

        key_t.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        key_y = tk.Button(
            frame_1,
            text='y',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display('y')
            )

        key_y.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)



        key_u = tk.Button(
            frame_1,
            text='u',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display('u')
            )

        key_u.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        key_i = tk.Button(
            frame_1,
            text='i',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display('i')
            )

        key_i.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        key_o = tk.Button(
            frame_1,
            text='o',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display('o')
            )

        key_o.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        key_p = tk.Button(
            frame_1,
            text='p',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display('p')
            )

        key_p.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)


        key_q = tk.Button(
            frame_2,
            text='q',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display('q')
            )

        key_q.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        
        
        key_s = tk.Button(
            frame_2,
            text='s',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display('s')
            )

        key_s.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        
        
        key_d = tk.Button(
            frame_2,
            text='d',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display('d')
            )

        key_d.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        
        
        key_f = tk.Button(
            frame_2,
            text='f',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display('f')
            )

        key_f.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        key_g = tk.Button(
            frame_2,
            text='g',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display('g')
            )

        key_g.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        
        
        key_h = tk.Button(
            frame_2,
            text='h',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display('h')
            )

        key_h.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        
        
        key_j = tk.Button(
            frame_2,
            text='j',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display('j')
            )

        key_j.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        
        key_k = tk.Button(
            frame_2,
            text='k',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display('k')
            )

        key_k.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        
        key_l = tk.Button(
            frame_2,
            text='l',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display('l')
            )

        key_l.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        
        key_m = tk.Button(
            frame_2,
            text='m',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display('m')
            )

        key_m.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        
        key_w = tk.Button(
            frame_3,
            text='w',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display('w')
            )


        key_w.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        
        key_x = tk.Button(
            frame_3,
            text='x',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display('x')
            )


        key_x.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        
        key_c = tk.Button(
            frame_3,
            text='c',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display('c')
            )


        key_c.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        
        key_v = tk.Button(
            frame_3,
            text='v',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display('v')
            )


        key_v.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        
        key_b = tk.Button(
            frame_3,
            text='b',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display('b')
            )


        key_b.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        
        
        key_n = tk.Button(
            frame_3,
            text='n',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display('n')
            )


        key_n.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        
        
        key_clr = tk.Button(
            frame_4,
            text='C',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = self.clear_scr 
            )

        key_clr.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        key_space = tk.Button(
            frame_4,
            text=' ',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda:self.display(' ')
            )

        key_space.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        key_entrer = tk.Button(
            frame_5,
            text='Entrer',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.commande_entrer(self.word)
            )

        key_entrer.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        key_point = tk.Button(
            frame_4,
            text='.',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display(".")
            )

        key_point.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        


    # functions
    def display(self,letter):
        
        self.word = self.word + letter
        self.scr_lbl['text'] = self.word

    def display2(self,number):
        
        self.word = self.word + str(number)
        self.scr_lbl['text'] = self.word
    def commande_entrer(self,textcomment):
        self.enregistrer_commentaire(textcomment)
        self.win.destroy()

    
    def clear_scr(self):
        
        self.num = ''
        self.scr_lbl['text'] = self.num

    #gestion de la zone de commentaire
    def enregistrer_commentaire(self,textcomment) :
        fichier = open("comment.txt", "w")
        fichier.write(textcomment)
        fichier.close()
    
    
# import tkinter as tk
# root=tk.Tk()
# pad=CreationPad(root)
# # valeur=pad.recuperer_valeur()
# # print(valeur)
# root.mainloop()
    
