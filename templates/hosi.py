import pandas as pd # for data processing
import folium   #for creating maps
import requests  #for retreiving Information from URL
from geopy.geocoders import Nominatim  #converting address to cordinates
from pandas.io.json import json_normalize


CLIENT_ID = '24BAGOCQB1CBUV3RKR0DTCEBUPPGHH1MFCOT5O0SH5MSCEBH ' # replace it with your Client id
CLIENT_SECRET = 'U1SGTRHPS0L0GSQINQKKHIXCQENGSXFFA2MQFQCGHMXKXZZD' # replace it with your client secret
VERSION = '20180604'

address = input("Enter address : ")
geolocator = Nominatim(user_agent="foursquare_agent") #
#converting address to coordinates
location = geolocator.geocode(address)
if(location == None):
    print('Please enter a Valid address')
    exit()
# reading latitude from location
latitude = location.latitude
# reading longitude from location
longitude = location.longitude
# reading radius from user
radius = input("Enter the radius for searching : ")
#reading search limit from user
Limit = input("enter the Limit for Results to display : ")
url  = 'https://api.foursquare.com/v2/venues/explore?client_id={}&client_secret={}&ll={},{}&v={}&radius={}&limit={}'.format(CLIENT_ID, CLIENT_SECRET, latitude, longitude, VERSION, radius, Limit)
results = requests.get(url).json()

items = results['response']['groups'][0]['items']
items[0]
def get_category_type(row):
    try:
        categories_list = row['categories']
    except:
        categories_list = row['venue.categories']
        
    if len(categories_list) == 0:
        return None
    else:
        return categories_list[0]['name']

#flatten JSON, Normalize JSON to Dataframe
dataframe = json_normalize(items) 

# filter columns,consider only required columns
filtered_columns = ['venue.name', 'venue.categories'] + [col for col in dataframe.columns if col.startswith('venue.location.')] + ['venue.id']
nearby = dataframe.loc[:, filtered_columns]

# filter the category for each row
nearby['venue.categories'] = nearby.apply(get_category_type, axis=1)

# clean columns
nearby.columns = [col.split('.')[-1] for col in nearby.columns]

#replce NaN values with Not found in address
nearby['address'] = nearby['address'].fillna("Not found")
nearby.head(10)    