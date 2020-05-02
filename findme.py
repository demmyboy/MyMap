import folium 
import pandas
import pprint

data =pandas.read_csv("original.csv")
# to get the list of coluumns
# print(data.columns)
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

html = '''<h4> Volcano Information: </h4>
Height: %s m
'''
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

#  Add map to a feature group 
fg = folium.FeatureGroup(name="My Map")
# Below coode is good to iterate through a list hand written 
# cordinates = [[6.5244, 3.3792], [4.8156, 7.0498]]
# for cordinate in cordinates:
#     fg.add_child(folium.Marker(location=cordinate, popup="This is where I am from", icon=folium.Icon(color="Purple")))



# create a function to change colors based on elevation
def color_producer(color): 
    if el < 1000:
        return "orange"
    elif 1000 <= el < 3000: 
        return "pink"
    else:
        return "red"

# Below code is use to iterate through an excel file 
for lt, ln, el  in zip(lat, lon, elev): 
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), tooltip="Please Click me", icon=folium.Icon(color=color_producer(el))))
map.add_child(fg)
map.save("DemmyMap2.html")
#  print(help(folium.Map))
# pprint.pprint (help(folium))
# pprint.pprint(f"This is help for popup {str(help(folium.Marker))}")

