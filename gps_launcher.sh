#!/bin/bash
sudo systemctl enable gpsd.socket
sudo systemctl start gpsd.socket
sudo python3 /home/pi/Desktop/A_jour/acquisition_gps.py &
