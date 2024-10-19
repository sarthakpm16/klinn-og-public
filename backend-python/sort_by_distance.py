import pandas as pd
from geopy import distance
from geopy.geocoders import Nominatim
#import plotly.express as px


ZIPCODE = 20852

data=pd.read_csv('backend-python/data.csv') 
geolocator = Nominatim(user_agent='Klinn')
coord = geolocator.geocode(query= ZIPCODE, country_codes='US')
coord = (coord.latitude, coord.longitude)
print(coord)

data['dist'] = data.apply(lambda d: distance.distance((d['Geocoding Artifact Address Primary Y Coordinate'], d['Geocoding Artifact Address Primary X Coordinate']), coord).miles, axis=1)

data = data.sort_values(by=['dist'], ascending=True)
print(data.iloc[1:50])

#fig = px.scatter_geo(data.iloc[1:50], lat='Geocoding Artifact Address Primary Y Coordinate', lon='Geocoding Artifact Address Primary X Coordinate', hover_name='Site Name', scope='usa')
#fig.show()  