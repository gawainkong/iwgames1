# map_visualisation.py

# Author: JC
# Last mod: 2024-03-14 1100

# Draws the maps
'''
from naturalWorld_classes import NaturalWorld
import geopandas as gpd
import folium

# Load data 
data = NaturalWorld()  # Create an instance of your NaturalWorld class
physical_data = data.get_physical_data()  

# Define map styles (customize these as needed)
physical_style = {'fillColor': '#e0d4a2', 'color': '#8c7853'}  
political_style = {'fillColor': '#add8e6', 'color': '#000080'}

# Create the base Folium map
map = folium.Map(location=[40.7128, -74.0060], zoom_start=3, tiles="OpenStreetMap")

# Function to add physical layer
def add_physical_layer():
    folium.GeoJson(physical_data, style_function=lambda x: physical_style).add_to(map)

# Add initial view (physical)
add_physical_layer()

# Save the map
map.save("map.html")
'''
