# 파일명 : Ex09_folium.py
import folium
import os
os.makedirs('map', exist_ok=True)

#설치 : pip instasll folium

map_osm = folium.Map(location=[37.572807, 126.975918], zoom_start=17)

folium.Marker(
    location=[37.572807, 126.975918]
    ,popup='세종문화회관'
    ,icon=folium.Icon(color='red', icon='info-sign')
).add_to(map_osm)

map_osm.save('./map/map1.html')
