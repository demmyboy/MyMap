import folium 
import pandas

data = pandas.read_csv("original.csv")
# to get the list of coluumns
# print(data.columns)
lat = list(data["LAT"])
lon = list(data["LON"])
map = folium.Map(location=[6.5244, 3.3792], zoom_start=6, tiles="Stamen Terrain")

#  Add map to a feature group 
fg = folium.FeatureGroup(name="My Map")
# Below coode is good to iterate through a list hand written 
# cordinates = [[6.5244, 3.3792], [4.8156, 7.0498]]
# for cordinate in cordinates:
#     fg.add_child(folium.Marker(location=cordinate, popup="This is where I am from", icon=folium.Icon(color="Purple")))

# Below code is use to iterate through an excel file 
for lt, ln in zip(lat, lon): 
    fg.add_child(folium.Marker(location=[lt, ln], popup="This is where I am from", icon=folium.Icon(color="Purple")))

map.add_child(fg)
map.save("DemmyMap.html")
#  print(help(folium.Map))
#  print (dir(folium))
print(dir(pandas))

