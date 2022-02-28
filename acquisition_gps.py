from math import *
from gps import *
#/lib/python3/dist-packages/gps
import time

running = True

def getPositionData(gps):
    nx=gpsd.next()
    print(nx['class'])
    if nx['class']=='TPV':
        latitude = getattr(nx, 'lat', "Unknown")
        longitude = getattr(nx, 'lon', "Unknown")
        fichier = open("flight_data.txt", "w")
        fichier.write(str(latitude)+"\n"+str(longitude))
        fichier.close()
        print("Your position: lon = " +str(longitude) + ", lat = "+str(latitude))
 
gpsd=gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)


# Creation du fichier txt
try:
    print("Application started")
    while running:
        getPositionData(gpsd)
        #fichier.write(str(latitude)+"\t"+str(longitude)+"\t"+str(altitude)+"\n")
        time.sleep(1.0)
except (KeyboardInterrupt):
   running=False
   print("Application closed")