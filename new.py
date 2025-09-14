import phonenumbers
from phonenumbers import geocoder, carrier  
from test import number
import folium

check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")
print(number_location)

from phonenumbers import carrier
service_provider = carrier.name_for_number(check_number, "en")
print(service_provider)

from opencage.geocoder import OpenCageGeocode

key = "3defee6ad04d4c04b4e340db714e1b7f"
geocoder = OpenCageGeocode(key)
query = str(number_location)
result = geocoder.geocode(query)
print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat, lng)
myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=number_location).add_to((myMap))
myMap.save("mylocation.html")
