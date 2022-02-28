class CreationPad:
    def __init__(self,root):
        import tkinter as tk

#         self.ws = tk.Tk()
#         self.ws.title('Keyboard')
#         self.ws.geometry('250x400+500+100')
#         self.ws.resizable(0,0)
        self.win=tk.Toplevel(root)

        # global variables
        self.num = ''
        
        var = tk.StringVar()

        # frames 
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

        # buttons
        key_1 = tk.Button(
            frame_1,
            text='1',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display(1)
            )

        key_1.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        key_2 = tk.Button(
            frame_1,
            text='2',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display(2)
            )

        key_2.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        key_3 = tk.Button(
            frame_1,
            text='3',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display(3)
            )

        key_3.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)



        key_4 = tk.Button(
            frame_2,
            text='4',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display(4)
            )

        key_4.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        key_5 = tk.Button(
            frame_2,
            text='5',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display(5)
            )

        key_5.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        key_6 = tk.Button(
            frame_2,
            text='6',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display(6)
            )

        key_6.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)



        key_7 = tk.Button(
            frame_3,
            text='7',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display(7)
            )

        key_7.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        key_8 = tk.Button(
            frame_3,
            text='8',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display(8)
            )

        key_8.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        key_9 = tk.Button(
            frame_3,
            text='9',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display(9)
            )

        key_9.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)



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

        key_0 = tk.Button(
            frame_4,
            text='0',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.display(0)
            )

        key_0.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        key_entrer = tk.Button(
            frame_5,
            text='Entrer',
            font=('Arial', 22),
            border = 0,
            relief = tk.GROOVE,
            bg = '#2E2E2B',
            fg = 'white',
            command = lambda: self.commande_entrer()
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
    def display(self,number):
        
        self.num = self.num + str(number)
        self.scr_lbl['text'] = self.num
      
    def commande_entrer(self):
        
        self.win.destroy()

    def recuperer_valeur(self):
        if self.num == '':
            return(1018)
        else:
            return(float(self.num))
    def clear_scr(self):
        
        self.num = ''
        self.scr_lbl['text'] = self.num


# pad=CreationPad()
# valeur=pad.recuperer_valeur()
# print(valeur)
    