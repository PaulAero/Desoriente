# New class: Track


class Track:
    
    def __init__(self):

        ##Import libraries
        import folium
        from html2image import Html2Image

        ## Choice of the zoom
        
        self.zoom=14
        
        ##For the map in the backgroung, we choose to take the first position as reference (center point)
        hti = Html2Image()
        # Object fmap created
        map=folium.Map(location=[44.8448769,-0.656358],zoom_start=self.zoom)
        # Adding the line and saving the file
        map.save(r'C:\Users\dubou\Documents\Python\myMap.html')
        hti = Html2Image(output_path=r'C:\Users\dubou\Documents\Python')
        hti.screenshot(url=r'C:\Users\dubou\Documents\Python\myMap.html', save_as='map_adapted.gif')

##                                       End init                                         ##     
     
    # Create my track
    def create_my_track(self):
        
        import tkinter as tk
        from PIL import Image,ImageTk
        from tkinter import ttk
        
        
        ##Objects from classes Tk and Canvas created and customised

        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.bind('<Escape>',lambda e: self.root.destroy())
        size_map_x=2*self.root.winfo_screenwidth()
        size_map_y=2*self.root.winfo_screenheight()
        self.canvas=tk.Canvas(self.root,  scrollregion =(0, 0, size_map_x,size_map_y), width=self.root.winfo_screenwidth()-30, height=self.root.winfo_screenheight()-30, bg='ivory')
        self.canvas.grid()
        self.create_button_focus()
        
        ## Scrollbars
        self.xscroll=ttk.Scrollbar(self.root, orient=tk.HORIZONTAL)
        self.yscroll=ttk.Scrollbar(self.root, orient=tk.VERTICAL)
        
        
        self.xscroll.grid(row=1, column=0, sticky=tk.E+tk.W)
        self.yscroll.grid(row=0, column=1,  sticky=tk.S+tk.N)
        
        self.xscroll["command"]=self.canvas.xview
        self.yscroll["command"]=self.canvas.yview
        self.canvas.yview_moveto(0.25)
        self.canvas.xview_moveto(0.25)
        self.canvas['xscrollcommand']=self.xscroll.set
        self.canvas['yscrollcommand']=self.yscroll.set
        
        
        
        
        ##Backgroung picture imported, resized and included on the screen

        map_city=Image.open(r'C:\Users\dubou\Documents\Python\map_adapted.gif')
        w,h=2*self.root.winfo_screenwidth(),2*self.root.winfo_screenheight()
        map_city=map_city.resize((w,h))
        map_city=ImageTk.PhotoImage(map_city,master=self.root)
        self.canvas.create_image((size_map_x//2, size_map_y//2), image=map_city)
        self.data_initialisation()
        self.data_planned_flight()
        self.data_recovery()
        
        
        self.root.mainloop()
        
        
        
## This method is used to initialize the coordinates of the NW and SE points and to determinate the values of a pixel in both directions
    def data_initialisation(self):
        # Initialisation of the coordinates of the center point
        self.coordinates_y0=44.8448769
        self.coordinates_x0=-0.656358
        
        
        ####Value of a pixel  A GENERALISER AVEC LA TAILLE DE LA PHOTO SUR LE SITE 
        self.value_pixel_x=360/(256*pow(2,self.zoom))
        self.value_pixel_y=360/(256*7/5*pow(2,self.zoom))
        
    # This method is used to draw the planned path on the map
    def data_planned_flight(self):
            
        import gpxpy
        
        #Reading in a gpx file
        gpx_file= open(r'C:\Users\dubou\Documents\Python\trajet.gpx')
        gpx=gpxpy.parse(gpx_file)
        
        
        # Initialisation with the position of the gps before taking off
        old_map_x=self.root.winfo_screenwidth()
        old_map_y=self.root.winfo_screenheight()
        
        # These for are used to go through all the data in the gpx file
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    
                    # Conversion of the values of the latitude and longitude into the number of pixel they represent on the screen 
                    position_x=point.longitude
                    position_y=point.latitude
                    map_x=self.root.winfo_screenwidth()+2*(position_x-self.coordinates_x0)/self.value_pixel_x
                    map_y=self.root.winfo_screenheight()-2*(-self.coordinates_y0+position_y)/self.value_pixel_y
                    self.canvas.create_line(map_x,map_y,old_map_x,old_map_y,fill='blue',width=5)
                    
                    # We save the old value in order to link the last point to the new one
                    old_map_x=map_x
                    old_map_y=map_y
                    
                    
    # This method is used to recover the data from the GPS: altitude, coordinates on x and y
    def data_recovery(self):
        import time
        import gpxpy
        import tkinter as tk
        from PIL import Image,ImageTk
        from math import atan,pi
        
        
        # In this part, we import and resize the picture of the plane used for the animation
        
        plane=Image.open(r'C:\Users\dubou\Documents\Python\plane_above.png')
        w,h=self.root.winfo_screenwidth()//10,self.root.winfo_screenheight()//10
        plane=plane.resize((w,h))
        #plane=ImageTk.PhotoImage(plane,master=self.root)
        
        ## This part of the method is temporary.It is used to develop the part of the code where you draw the path of the plane in real time
        
        #Reading in a gpx file
        gpx_file= open(r'C:\Users\dubou\Documents\Python\trajet.gpx','r')
        gpx=gpxpy.parse(gpx_file)
        
        # Definition of the variables
        self.height=self.root.winfo_screenheight()
        self.width=self.root.winfo_screenwidth()
        
        # Initialisation with the position of the gps before taking off
        old_map_x=self.root.winfo_screenwidth()
        old_map_y=self.root.winfo_screenheight()
        old_position_x=self.coordinates_x0
        old_position_y=self.coordinates_y0
        modified_plane=plane.rotate(90)
        modified_plane=ImageTk.PhotoImage(plane,master=self.root)
        picture_plane=self.canvas.create_image(old_map_x,old_map_y, anchor='center',image = modified_plane)
        
        # These for are used to go through all the data in the gpx file
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    
                    
                    #print('({0},{1})->{2}'.format(point.latitude,point.longitude,point.elevation))
                    
                    
                    # Conversion of the values of the latitude and longitude into the number of pixel they represent on the screen 
                    position_x=point.longitude
                    position_y=point.latitude
                    self.map_x=self.root.winfo_screenwidth()+2*(position_x-self.coordinates_x0)/self.value_pixel_x
                    self.map_y=self.root.winfo_screenheight()-2*(-self.coordinates_y0+position_y)/self.value_pixel_y
                    self.canvas.create_line(self.map_x,self.map_y,old_map_x,old_map_y,fill='red',width=5)
                    if (position_x-old_position_x)!=0: #Division by 0
                        angle=0
                        if position_x-old_position_x>=0 and position_y-old_position_y>=0: #1st quarter
                            angle=atan((position_y-old_position_y)/(position_x-old_position_x))*180/pi+270
                        elif position_x-old_position_x>=0 and position_y-old_position_y<=0: #2nd quarter
                            angle=atan((position_y-old_position_y)/(position_x-old_position_x))*180/pi+270
                        elif position_x-old_position_x<=0 and position_y-old_position_y<=0: #3rd quarter
                           angle=atan((position_y-old_position_y)/(position_x-old_position_x))*180/pi+90
                        else: #Last quarter
                            angle=atan((position_y-old_position_y)/(position_x-old_position_x))*180/pi-270
                    
                    modified_plane=plane.rotate(angle)
                    modified_plane=ImageTk.PhotoImage(modified_plane,master=self.root)
                    picture_plane=self.canvas.create_image(old_map_x,old_map_y, anchor='center',image = modified_plane)
                    self.canvas.delete(self.root,picture_plane)
                    picture_plane=self.canvas.create_image(self.map_x,self.map_y, anchor='center',image = modified_plane)
                    
                    
                    
                    # We save the old values in order to link the last point to the new one
                    old_map_x=self.map_x
                    old_map_y=self.map_y
                    old_position_x=position_x
                    old_position_y=position_y
                    
                    
                    # If the image is already centered, we keep centering it. To know if we need to do something, we compare the position the bars should have to the one they have
                    
                    position_x,position_y=self.get_my_real_time_position_map()
                    ratio_x=abs(position_x)/(2*self.root.winfo_screenwidth())
                    ratio_y=abs(position_y)/(2*self.root.winfo_screenheight())
                    
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
                    time.sleep(0.3)
                    self.root.update()
                    
        

    ## This button can be used to update the position of the scrollbars in order to see the real time position at the center of the screen
    
    
    # Definition of the fonction used to get the real time position on the map (pixels)
    
    def get_my_real_time_position_map(self):
        return(self.map_x,self.map_y)
    # Definition of the command
    
    def focus_on_my_position(self):
        position_x,position_y=self.get_my_real_time_position_map()
        ratio_x=abs(position_x)/(2*self.root.winfo_screenwidth())
        ratio_y=abs(position_y)/(2*self.root.winfo_screenheight())
        # if the position is too close to a border, the position will be 0
        if ratio_x<0.25:
            self.canvas.xview_moveto(0)
        else:
            self.canvas.xview_moveto(ratio_x-0.25)
            
        if ratio_y<0.25: 
            self.canvas.yview_moveto(0)
        else:
            self.canvas.yview_moveto(ratio_y-0.25)
        
        
    # Button 'My position' is created
    def create_button_focus(self):
        import tkinter as tk
        from PIL import Image,ImageTk
        height_button=self.root.winfo_screenheight()/20
        width_button=self.root.winfo_screenwidth()/10
        button_coordinate_x=0
        button_coordinate_y=0
        valider =tk.Button(self.root, text = "Recenter", background='white',command=self.focus_on_my_position)
        valider.place(x = button_coordinate_x, y= button_coordinate_y, height=height_button, width=width_button)
        
        ### Add the logo of the project
        # logo=Image.open(r'C:\Users\dubou\Documents\Python\logo_mini.gif')
        # w,h=self.root.winfo_screenwidth()//20,self.root.winfo_screenheight()//20
        # logo=logo.resize((w,h))
        # logo=ImageTk.PhotoImage(logo,master=self.root)
        # self.canvas.create_image(self.root.winfo_screenwidth()/2,self.root.winfo_screenheight()/2, image=logo)



#     # #This method is used to save the data in a csv file in order to draw the path of the flight afterward
#     # def save_data_csv(self):
 
track = Track()
track.create_my_track()



