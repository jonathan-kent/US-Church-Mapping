from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

geolocator = Nominatim(user_agent="email=jonathanskent@gmail.com")

def get_coords(state):
    file = open(state+".txt", "r")
    output = open(state+"_coords.txt", "w")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    lines = file.readlines()
    for line in lines:
        parts = line.split(";")
        location = geocode(parts[0])
        try:
            output.writelines(str(location.latitude)+", "+str(location.longitude)+";"+line)
        except:
            print("error: "+parts[0])
    file.close()
    output.close()

get_coords("ma")
    

