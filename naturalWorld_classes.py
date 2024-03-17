# naturalWorld_classes.py

# Author: JC
# Last mod: 2024-03-17

# geographic data

import geopandas as gpd
import folium
import fiona
from shapely.geometry import shape
import os

class NaturalWorld:
  def __init__(self):
    # Adjust the paths as needed
    self.physical_datapath = r"\iwdata\natural_earth_vector.gpkg"
    self.political_datapath = r"..."  # Add the path to your political data

    self._physical_data = None
    self._political_data = None

  def load_physical_data(self):

    # Little bit of test code
    self.physical_datapath = r"\iwdata\natural_earth_vector.gpkg"

    try:
      absolute_path = os.path.abspath(self.physical_datapath)

      with fiona.open(self.physical_datapath) as src:
        print("GeoPackage opened successfully")

        # Load desired layers
        for layer_name in ['ne_110m_land']:  # Add more as needed
          data = gpd.read_file(self.physical_datapath, layer=layer_name)
          self.create_map(data)  # Call the new function to create the map

    except Exception as e:
      print("Error Encountered:", e)

  def create_map(self, data):
    # Create a base folium map
    m = folium.Map(location=[0, 0], zoom_start=2)  # Initial center and zoom

    # Iterate through features (geometries) in the data
    for index, row in data.iterrows():
      # Extract the geometry
      geometry = row['geometry']

      # Convert the Shapely geometry to a format suitable for folium
      # (This might require converting the geometry type depending on what it is)
      geojson = geometry.__geo_interface__  # Assuming GeoJSON format for now

      # Create a folium Feature object based on the geometry
      folium.GeoJson(geojson, name="Landmass").add_to(m)

    # Display the map
    m

  def load_political_data(self):
    self._political_data = gpd.read_file(self.political_datapath)

  def get_physical_data(self):
    if not self._physical_data:
      self.load_physical_data()
    return self._physical_data

  def get_political_data(self):
    if not self._political_data:
      self.load_political_data()
    return self._political_data

# Example Usage (assuming you have an instance of NaturalWorld called 'world')
world = NaturalWorld()
world.load_physical_data()
