# New class: Track


class Track:
    
    #Attributes
    zoom=14
    
    #Method used to create the backgroung of the gps
    def create_map(self):

        ##Import libraries
        import folium
        from html2image import Html2Image
        from gps import gps,WATCH_ENABLE,WATCH_NEWSTYLE

 
        
        ##For the map in the backgroung, we choose to take the first position as reference (center point)
        hti = Html2Image()
        # Object fmap created
        gpsd=gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
        initial_lat,initial_lon=self.getPositionData(gpsd)
        fichier = open("coordonnees_init.txt", "w")
        fichier.write(str(initial_lat)+"\n"+str(initial_lon))
        fichier.close()
        map=folium.Map(location=[initial_lon,initial_lat],zoom_start=self.zoom)
#         # Adding the line and saving the file
        map.save('myMap.html')
        #hti = Html2Image(output_path='Python')
        hti.screenshot(url='myMap.html', save_as='map_adapted.gif')

    
    
    # Create my track
    def create_my_track(self):
        
        import tkinter as tk
        from PIL import Image,ImageTk
        from tkinter import ttk
        import time
        
        
        ##Objects from classes Tk and Canvas created and customised

        self.root3 = tk.Tk()
        self.root3.attributes('-fullscreen', True)
        self.root3.bind('<Escape>',lambda e: self.root3.destroy())
        size_map_x=2*self.root3.winfo_screenwidth()
        size_map_y=2*self.root3.winfo_screenheight()
        self.canvas3=tk.Canvas(self.root3,  scrollregion =(0, 0, size_map_x,size_map_y), width=self.root3.winfo_screenwidth()-16, height=self.root3.winfo_screenheight()-16, bg='ivory')
        self.canvas3.grid()
        self.create_button_focus()
        self.create_button_horizon()
        self.create_button_variometer()
               
        ## Scrollbars
        self.xscroll=ttk.Scrollbar(self.root3, orient=tk.HORIZONTAL)
        self.yscroll=ttk.Scrollbar(self.root3, orient=tk.VERTICAL)
        
        
        self.xscroll.grid(row=1, column=0, sticky=tk.E+tk.W)
        self.yscroll.grid(row=0, column=1,  sticky=tk.S+tk.N)
        
        self.xscroll["command"]=self.canvas3.xview
        self.yscroll["command"]=self.canvas3.yview
        self.canvas3.yview_moveto(0.25)
        self.canvas3.xview_moveto(0.25)
        self.canvas3['xscrollcommand']=self.xscroll.set
        self.canvas3['yscrollcommand']=self.yscroll.set
        
        
        
        
        ##Backgroung picture imported, resized and included on the screen

        map_city=Image.open('map_adapted.gif')
        w,h=2*self.root3.winfo_screenwidth(),2*self.root3.winfo_screenheight()
        map_city=map_city.resize((w,h))
        map_city=ImageTk.PhotoImage(map_city,master=self.root3)
        self.canvas3.create_image((size_map_x//2, size_map_y//2), image=map_city)
        self.data_initialisation()
        self.logo=tk.PhotoImage(file="logo_mini.gif",master=self.root3)
        self.canvas3.create_image(2*self.root3.winfo_screenwidth()-self.root3.winfo_screenwidth()/20,2*self.root3.winfo_screenheight()-self.root3.winfo_screenheight()/12,image=self.logo)
        self.bouton_click=False
        while self.bouton_click==False:
            self.data_recovery(self.root3)
            time.sleep(7)
            self.root3.update()
            
        
        
        self.root3.mainloop()
        
        
        
## This method is used to initialize the coordinates of the NW and SE points and to determinate the values of a pixel in both directions
    def data_initialisation(self):
        # Initialisation of the coordinates of the center point
        
        fichier = open("flight_data.txt", "r")
        lines = fichier.readlines()
        self.coordinates_x0,self.coordinates_y0= float(lines[0]), float(lines[1])
        
        
        ####Value of a pixel  A GENERALISER AVEC LA TAILLE DE LA PHOTO SUR LE SITE 
        self.value_pixel_x=360/(256*800/1920*pow(2,self.zoom))
        self.value_pixel_y=360/(256*480/1080*7/5*pow(2,self.zoom))
        ## 7/5 facteur agrandissement entre la page html et la photo + les rapports de pixels entre la photo et la taille de l'écran
        return(self.value_pixel_x,self.value_pixel_y)
    
    def data_screen(self):
        #return(self.root3.winfo_screenwidth(),self.root3.winfo_screenheight())
        return(480,800)
    
    #This method gets the gps position
    def getPositionData(self,gps):
        fichier = open("flight_data.txt", "r")
        lines = fichier.readlines()
        latitude_gps_txt = lines[0]
        longitude_gps_txt = lines[1]
        latitude_gps = float(latitude_gps_txt)
        longitude_gps = float(longitude_gps_txt)
        fichier.close()
        return(longitude_gps, latitude_gps)
    
        # This method is used to recover the data from the GPS: altitude, coordinates on x and y
    def data_recovery(self,root):
        import time
        import gps
        from gps import WATCH_ENABLE, WATCH_NEWSTYLE
        import gpxpy
        import tkinter as tk
        from PIL import Image,ImageTk
        from math import atan,pi
        
        
        
        # In this part, we import and resize the picture of the plane used for the animation
        
        plane=Image.open('plane_above.png')
        self.width,self.height=self.data_screen()
        w,h=self.width//20,self.height//15
        plane=plane.resize((w,h))
        #plane=ImageTk.PhotoImage(plane,master=self.root3)
        
    
        # Initialisation with the position of the gps before taking off
        old_map_x=self.width
        old_map_y=self.height
        old_position_x=self.coordinates_x0
        old_position_y=self.coordinates_y0
        modified_plane=plane.rotate(90)
        modified_plane=ImageTk.PhotoImage(plane,master=root)
        picture_plane=self.canvas3.create_image(old_map_x,old_map_y, anchor='center',image = modified_plane)

    
        # Conversion of the values of the latitude and longitude into the number of pixel they represent on the screen 
        gpsd=gps.gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
        position_x, position_y = self.getPositionData(gpsd)
        self.map_x=self.width+2*(position_x-self.coordinates_x0)/self.value_pixel_x
        self.map_y=self.height-2*(-self.coordinates_y0+position_y)/self.value_pixel_y
        self.canvas3.create_line(self.map_x,self.map_y,old_map_x,old_map_y,fill='red',width=3)
        if (position_x-old_position_x)==0: #Division by 0
            angle=0
        elif position_x-old_position_x>=0 and position_y-old_position_y>=0: #1st quarter
            angle=atan((position_y-old_position_y)/(position_x-old_position_x))*180/pi+270
        elif position_x-old_position_x>=0 and position_y-old_position_y<=0: #2nd quarter
            angle=atan((position_y-old_position_y)/(position_x-old_position_x))*180/pi+270
        elif position_x-old_position_x<=0 and position_y-old_position_y<=0: #3rd quarter
           angle=atan((position_y-old_position_y)/(position_x-old_position_x))*180/pi+90
        else: #Last quarter
            angle=atan((position_y-old_position_y)/(position_x-old_position_x))*180/pi-270
    
        modified_plane=plane.rotate(angle)
        modified_plane=ImageTk.PhotoImage(modified_plane,master=self.root3)
            
        self.canvas3.delete(self.root3,picture_plane)
        picture_plane=self.canvas3.create_image(self.map_x,self.map_y, anchor='center',image = modified_plane)
        
        
        
        # We save the old values in order to link the last point to the new one
        old_map_x=self.map_x
        old_map_y=self.map_y
        old_position_x=position_x
        old_position_y=position_y
        
            
        # If the image is already centered, we keep centering it. To know if we need to do something, we compare the position the bars should have to the one they have
            
        position_x,position_y=self.map_x,self.map_y
        ratio_x=abs(position_x)/(2*self.width)
        ratio_y=abs(position_y)/(2*self.height)
        
        # if the position is too close to a border, the position will be 0
        if ratio_x<0.25:
            centered_position_x=0
        else:
            centered_position_x=ratio_x-0.25
        
        if ratio_y<0.25: 
            centered_position_y=0
        else:
            centered_position_y=ratio_y-0.25

        horizontal_1,horizontal_2=self.xscroll.get()
        vertical_1,vertical_2=self.yscroll.get()
        if abs(horizontal_1-centered_position_x)<=0.05 and abs(vertical_1-centered_position_y)<=0.05:
            self.focus_on_my_position()
        self.root3.update()

                
    

    ## This button can be used to update the position of the scrollbars in order to see the real time position at the center of the screen
    
    def focus_on_my_position(self):
        from gps import WATCH_ENABLE,WATCH_NEWSTYLE,gps
        gpsd=gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
        position_x,position_y=self.getPositionData(gpsd)
        value_pixel_x,value_pixel_y=self.data_initialisation()
        self.width,self.height=self.data_screen()
        where_map_x=self.width+2*(position_x-self.coordinates_x0)/value_pixel_x
        where_map_y=self.height-2*(-self.coordinates_y0+position_y)/value_pixel_y
    ### En pixels pas en degres########################################"
        ratio_x=abs(where_map_x)/(2*self.width)
        ratio_y=abs(where_map_y)/(2*self.height)
        # if the position is too close to a border, the position will be 0
        if ratio_x<0.25:
            self.canvas3.xview_moveto(0)
        else:
            self.canvas3.xview_moveto(ratio_x-0.25)
            
        if ratio_y<0.25: 
            self.canvas3.yview_moveto(0)
        else:
            self.canvas3.yview_moveto(ratio_y-0.25)
        
        
    # Button 'My position' is created
    def create_button_focus(self):
        import tkinter as tk
        from PIL import Image,ImageTk
        height_button=self.root3.winfo_screenheight()/20
        width_button=self.root3.winfo_screenwidth()/10
        button_coordinate_x=0
        button_coordinate_y=0
        valider =tk.Button(self.root3, text = "Recenter", background='white',command=lambda:self.focus_on_my_position())
        valider.place(x = button_coordinate_x, y= button_coordinate_y, height=height_button, width=width_button)
        
        
    def draw_variometer(self):

        self.root3.destroy()
        
        import Variometre_classe
        from Variometre_classe import Variometre
        mon_variometre=Variometre()
        mon_variometre.tracer_le_variometre()
        self.bouton_click=True


    def create_button_variometer(self):
        import tkinter as tk
        import tkinter.font as font
        height_button=4
        width_button=len('To Variometer')
        font_size=self.root3.winfo_screenheight()//55
        f = font.Font(family='Arial', size=font_size, weight="bold")
        button = tk.Button (self.root3,text = "To Variometer",font= f,fg="white",bg="grey",height = height_button, width = width_button,command=lambda:self.draw_variometer())
        button_vario_coordinate_y=self.root3.winfo_screenheight()/2-(height_button+1)*font_size
        button.place(x=self.root3.winfo_screenwidth()//50, y=button_vario_coordinate_y)


    def draw_horizon(self):

        self.root3.destroy()
        
        import horizon_artificiel
        from horizon_artificiel import HorizonArtificiel
        mon_horizon_artificiel=HorizonArtificiel()
        mon_horizon_artificiel.horizon_artificiel()
        self.bouton_click=True


    def create_button_horizon(self):
        import tkinter as tk
        import tkinter.font as font
        height_button=4
        width_button=len('To Atificial Horizon')
        font_size=self.root3.winfo_screenheight()//55
        f = font.Font(family='Arial', size=font_size, weight="bold")
        button = tk.Button (self.root3,text = "To Artificial Horizon",font= f,fg="white",bg="grey",height = height_button, width = width_button,command=lambda:self.draw_horizon())
        button_coordinate_y=self.root3.winfo_screenheight()/2-(height_button+1)*font_size
        button.place(x=self.root3.winfo_screenwidth()-((self.root3.winfo_screenwidth()//10)+width_button*3)-25, y=button_coordinate_y)
    
 
        ### Add the logo of the project
        # logo=Image.open(r'C:\Users\dubou\Documents\Python\logo_mini.gif')
        # w,h=self.root3.winfo_screenwidth()//20,self.root3.winfo_screenheight()//20
        # logo=logo.resize((w,h))
        # logo=ImageTk.PhotoImage(logo,master=self.root3)
        # self.canvas3.create_image(self.root3.winfo_screenwidth()/2,self.root3.winfo_screenheight()/2, image=logo)



#     # #This method is used to save the data in a csv file in order to draw the path of the flight afterward
#     # def save_data_csv(self):
 
track = Track()
track.create_map()
track.create_my_track()