#cleans community clinics database from https://data.hrsa.gov/data/download?hmpgtitle=hmpg-hrsa-data
import pandas as pd
import plotly.express as px

url = 'https://data.hrsa.gov//DataDownload/DD_Files/Health_Center_Service_Delivery_and_LookAlike_Sites.csv'
data = pd.read_csv(url)
data = data[["Site Name", "Site Address", "Site City", "Site State Abbreviation", "Site Postal Code", "Site Telephone Number", "Site Web Address", "Health Center Service Delivery Site Location Setting Description", "Health Center Location Type Description", "Health Center Type Description", "Geocoding Artifact Address Primary X Coordinate", "Geocoding Artifact Address Primary Y Coordinate"]]
data = data[data["Health Center Service Delivery Site Location Setting Description"].isin(['All Other Clinic Types', 'Unknown', 'Hospital'])]
data = data[data["Health Center Location Type Description"].isin(['Permanent'])]
data = data[data["Health Center Type Description"].str.contains('Service Delivery Site', regex=False)]
data = data.dropna(subset=['Geocoding Artifact Address Primary Y Coordinate', 'Geocoding Artifact Address Primary X Coordinate'])


print(data)
data.to_csv('backend-python/data.csv')
fig = px.scatter_geo(data, lat='Geocoding Artifact Address Primary Y Coordinate', lon='Geocoding Artifact Address Primary X Coordinate', hover_name='Site Name', scope='usa')
fig.show()  
