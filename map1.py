import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")         # get data of volcanoes 
lon = list(data["LON"])                         # longitude
lat = list(data["LAT"])                         # latitude
elev = list(data["ELEV"])                       # Elevation
    
def color_producer(elevation):                  # function to change color based on elevation 
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
 
map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Stamen Terrain")         # to show map using coordinates with tiles

featureGroupVolcanoes = folium.FeatureGroup(name="Volcanoes")                           # create feature group 

for lt,ln, el in zip(lat,lon,elev):                                                     # show locations of volcanoes using markers
    featureGroupVolcanoes.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=str(el)+"m",fill=True, 
    fill_color=color_producer(el), color='grey', fill_opacity=0.7))

featureGroupPopulation = folium.FeatureGroup(name="Population")                         # create feature group 

featureGroupPopulation.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(),           # Change color of areas based on the population
    style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
    else 'orange' if 10000000 <= x['properties']['POP2005'] < 2000000 else 'red'}))

map.add_child(featureGroupVolcanoes)            # add feature group volcanoes to map 
map.add_child(featureGroupPopulation)           # add feature group population to map 
map.add_child(folium.LayerControl())            # add layer

map.save("Map1.html")                           # save file