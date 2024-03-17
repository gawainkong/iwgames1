# Master_iw.py

# Master program for iwgames projects
# Author: JC
# Last mod: 2024-03-14 1100

# controlling program for iwprojects.

import sys
print(sys.executable)

PROJECT_TYPE = "TREES"

# These next two relate to the size of the initial map (global) as a proportion of the total screen size
MAP_RATIO_SCREEN_HEIGHT = 1.0
MAP_RATIO_SCREEN_WIDTH = 1.0    # Coming in from the Right hand side - thus creating a left hand gutter for command buttons

# These next two relate to the size of the initial map (global) as a proportion of the total screen size
GAMEPLAYAREA_RATIO_SCREEN_HEIGHT = 0.8
GAMEPLAYAREA_RATIO_SCREEN_WIDTH = 0.8

ARE_ANIMALS_ANIMATED = True
ARE_PERSONS_ANIMATED = True
ARE_PLANTS_ANIMATED = True

ALL_ANIMALS_ANIMATION_SPEED = 100   # base factor
ALL_PLANTS_ANIMATION_SPEED = 100    # base factor
ALL_PERSONS_ANIMATION_SPEED = 100   # base factor

ANIMALS_ANIMATION_SPEED_PERCENTAGE = 100    # % as applied to base factor
PLANTS_ANIMATION_SPEED_PERCENTAGE = 100     # % as applied to base factor
PERSONS_ANIMATION_SPEED_PERCENTAGE = 100    # % as applied to base factor

GAME_FPS = 60

# external imports
import os
import sys
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import pygame
import time
from PIL import Image, ImageDraw
from shapely.geometry import Polygon, MultiPolygon
from shapely.geometry import LineString, shape 


# Get the full path of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Add the directories containing the source files and import them
next_source_dir = os.path.join(script_dir, "..", "common", "source")
sys.path.append(next_source_dir)
next_source_dir = os.path.join(script_dir, "..", "naturalWorld_classes")
sys.path.append(next_source_dir)

try:
    import iw_common
    #from iw_common import CanvasClass
    from iw_common import MapCanvas
except ModuleNotFoundError:
    print("Failed to import 'iw_common' module.")
    raise # Re-raise the exception for further analysis

try:
    import naturalWorld_classes
    # from naturalWorld_classes import displayWorld
except ModuleNotFoundError:
    print("Failed to import 'naturalWorld_classes' module.")
    raise # Re-raise the exception for further analysis

try:
    import uberClass
    from uberClass import iwApp
    from uberClass import UberClass
   
except ModuleNotFoundError:
    print("Failed to import 'uberClass' module.")
    raise # Re-raise the exception for further analysis


# Get the full path of the current script
script_path = os.path.abspath(__file__)

# Print the script path for informational purposes
print(f"Running script: {script_path}")

class ControllerApp(iwApp):
    def __init__(self):
        # ... other initializations ...
        self.natural_world = naturalWorld_classes.NaturalWorld()
        self.world_data = self.natural_world.get_physical_data()
        
        self._GOD_MODE = False  # Initialize in some state
        self._DISPLAY_ZOOM = 1.0

        # Initialize map canvas
        info_object = pygame.display.Info()
        self.screen_width, self.screen_height = info_object.current_w, info_object.current_h
        map_canvas_width = int(MAP_RATIO_SCREEN_WIDTH * self.screen_width)
        map_canvas_height = int(MAP_RATIO_SCREEN_HEIGHT * self.screen_height)
        self.map_canvas = MapCanvas(width=map_canvas_width, height=map_canvas_height)

        self._zoom_factor = 1.0  # Initial zoom factor
        print("zoom_factor initialized:", self._zoom_factor) 

        self.draw_map_on_map_canvas(self.world_data)
        
        # The DEV MODE windows are used by the dev to paste up various bits of info
        self.dev_mode1_width = 180
        self.dev_mode1_height = 80
        self.dev_mode1_surface = pygame.Surface((self.dev_mode1_width, self.dev_mode1_height))

    @property
    def world_data(self):
        return self._world_data

    @world_data.setter
    def world_data(self, data):
        self._world_data = data

    @property
    def zoom_factor(self):
        return self._zoom_factor

    @zoom_factor.setter
    def zoom_factor(self, factor):
        self._zoom_factor = factor

    @property
    def GOD_MODE(self):
        return self._GOD_MODE

    @GOD_MODE.setter
    def GOD_MODE(self, value):
        self._GOD_MODE = value

    @property
    def DISPLAY_ZOOM(self):
        return self._DISPLAY_ZOOM

    @DISPLAY_ZOOM.setter
    def DISPLAY_ZOOM(self, value):
        self._DISPLAY_ZOOM = value

    def zoom_in(self):
        self._zoom_factor *= 1.1

    def zoom_out(self):
        self._zoom_factor /= 1.1

    def get_gutter_width(self):
        return self.screen_width * (1 - MAP_RATIO_SCREEN_WIDTH)

    def draw_map_on_map_canvas(self, world_data):
        width, height = self.map_canvas.width, self.map_canvas.height
        gutter_width = self.get_gutter_width()
        
        # Clear the canvas for redrawing the map
        self.map_canvas.surface.fill((40, 40, 40))  # Still fill with green for now

        # Calculate necessary scaling and translation factors
        minx, miny, maxx, maxy = world_data.total_bounds  
        scale_x = width / (maxx - minx)
        scale_y = height / (maxy - miny)

        for idx, row in world_data.iterrows():
            geometry = row['geometry'] 
            
            if isinstance(geometry, Polygon):
                coords = [(int((x - minx) * scale_x * self._zoom_factor), int((maxy - y) * scale_y * self._zoom_factor)) for x, y in geometry.exterior.coords]
                pygame.draw.polygon(self.map_canvas.surface, "blue", coords, width=3)  # Change color

            # ... other geometry types ...
                
        screen.blit(self.map_canvas.surface, (gutter_width, 0))  # Adjust coordinates if needed
    

    def draw_dev_mode_text(self):
        font = pygame.font.SysFont(None, 16)  # Use a default font
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if 0 <= mouse_x <= self.map_canvas.width and 0 <= mouse_y <= self.map_canvas.height:
            coords_text = font.render(f"Mouse: ({mouse_x:.1f}, {mouse_y:.1f})", True, (0,0,0))  # White text
        else:
            coords_text = font.render(f"Mouse: (0.000, 0.000)", True, (255, 0, 0))

        # Clear the dev_mode_surface before redrawing
        self.dev_mode1_surface.fill((200, 200, 255))  
        self.dev_mode1_surface.blit(coords_text, (10, 10))
              

    def main_loop(self):
        running = True
        clock = pygame.time.Clock()  

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                elif event.type == pygame.VIDEORESIZE:
                    self.screen_width, self.screen_height = event.size                              # Update screen dimensions
                    map_canvas_width = int(MAP_RATIO_SCREEN_WIDTH * self.screen_width)
                    map_canvas_height = int(MAP_RATIO_SCREEN_HEIGHT * self.screen_height)
                    self.map_canvas = MapCanvas(width=map_canvas_width, height=map_canvas_height)   # Recreate canvas with new dimensions
                    self.draw_map_on_map_canvas(self.world_data)                                    # Redraw the map

            # Update game logic (if needed)
                if event.type == pygame.MOUSEMOTION:
                    mouse_x, mouse_y = event.pos

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:  # Scroll up
                        self.zoom_in()
                    elif event.button == 5:  # Scroll down
                        self.zoom_out()

            # Draw game elements (including the map
            map_image = controller_app.draw_map_on_map_canvas(controller_app.world_data)
            gutter_width = controller_app.get_gutter_width()  # Calculate the gutter width
            screen.blit(self.map_canvas.surface, (gutter_width, 0))  # Place map with gutter offset
            
            
            # Update dev mode window contents
            self.draw_dev_mode_text()

            # Draw the dev mode window on the main screen
            dev_mode1_x = 10
            dev_mode1_y = 400
            screen.blit(self.dev_mode1_surface, (dev_mode1_x, dev_mode1_y))
            
            pygame.display.flip()





# And LET"S GO!
            
# Initialize Pygame
pygame.init()

# Create screen and game objects (including ControllerApp)
info_object = pygame.display.Info()  # Get system display information
screen_width, screen_height = info_object.current_w, info_object.current_h


screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
#screen = pygame.display.set_mode((screen_width, screen_height))
caption = "Trees"  # Replace with your desired caption
pygame.display.set_caption(caption)
clock = pygame.time.Clock()

# Create an instance of ControllerApp
controller_app = ControllerApp()

# ... (Optional: Set up initial game state)

# Call main_loop directly from ControllerApp
running = True  # Flag for main loop
controller_app.main_loop()

# Quit Pygame (after the main loop finishes)
pygame.quit()



