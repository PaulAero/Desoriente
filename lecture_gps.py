#test lecture data gps
fichier = open("flight_data.txt", "r")
lines = fichier.readlines()
print(lines)
latitude_gps = lines[0]
longitude_gps = lines[1]
print(latitude_gps, longitude_gps)
fichier.close()