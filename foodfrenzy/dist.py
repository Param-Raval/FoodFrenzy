from geopy.distance import geodesic
from geopy.geocoders import Nominatim

geolocator = Nominatim()
loca = geolocator.geocode("Thaltej, Ahmedabad")
print(loca.address)

l1=(loca.latitude,loca.longitude)

import gmplot 
  
latitude_list = [ 30.3358376, 30.307977, 30.3216419 ] 
longitude_list = [ 77.8701919, 78.048457, 78.0413095 ] 
  
gmap3 = gmplot.GoogleMapPlotter(30.3164945, 
                                78.03219179999999, 13) 
  
# scatter method of map object  
# scatter points on the google map 
gmap3.scatter( latitude_list, longitude_list, '# FF0000', 
                              size = 40, marker = False ) 
  
# Plot method Draw a line in 
# between given coordinates 
  
gmap3.draw("map13.html" )
