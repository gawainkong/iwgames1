# iw_common.py

# "iw" is the name for the set of game apps that I'm writing.

# This is the set of the cross app classes for iw projects.  It includes "CommonMasterApp" from which all
# other top level app classes inherit, and also any utilities that I suspect all my game apps will need

# Author: JC
# Last mod: 2024-03-14 1100

from uberClass import UberClass
import pygame

class CommonMasterApp:
    def __init__(self, app_name):
        self.app_name = app_name
    
    def save_status(self, status):
        # This method saves the status of the application
        with open(f"{self.app_name}_status.txt", "w") as file:
            file.write(status)
        print(f"Status saved for {self.app_name}")

    def load_status(self):
        # This method loads the status of the application
        try:
            with open(f"{self.app_name}_status.txt", "r") as file:
                status = file.read()
            print(f"Status loaded for {self.app_name}: {status}")
            return status
        except FileNotFoundError:
            print(f"No status found for {self.app_name}")

    def start_app(self):
        # This method starts the application
        print(f"Starting {self.app_name}...")


    def exit_app(self):
        # Clean up resources, save any necessary data, etc.
        self.save_status("Exiting")
        print(f"Exiting the app... {self.app_name}")

class PersonAttributes():
    
    # Define the attributes of a person
        
    def __init__(self, project_type):
        pass

    def initialize_attributes(self):
        """Set up initial abilities based on the project type"""
        if PROJECT_TYPE == "TREES" or self.PROJECT_TYPE == "POLI":
            self.add_attribute("intelligence", 1)                 # Pure brain power
            self.add_attribute("strength", 1)                     # Pure muscle strength
            self.add_attribute("woodcutting", 1)                  # Chopping trees, whittling etc
            self.add_attribute("gathering", 1)                    # Picking up berries, sticks etc
            self.add_attribute("attack_chance", 1)                # Specific chance qualifier to hit an enemy
            self.add_attribute("defend_chance", 1)                # Specific chance qualifier to defend against a enemy attack
            self.add_attribute("sexiness", 1)                     # how attractive the person is to people who like this gender
            self.add_attribute("presented_gender", "female")      # Basically whether they have a penis ("male) or vagina ("female")
            self.add_attribute("attracted_to_male", True)         # Likes to have sex with presenting males
            self.add_attribute("attracted_to_female", False)      # Likes to have sex with presenting females
            self.add_attribute("presented_age", adult)            # infant/child/adult/elder (player only sees these "ages")
            self.add_attribute("age", 15)                         # Age - internal use only as we never display this to players
            
class ResourceNode(UberClass):
    def __init__(self):
        self.type = "UNDEF"                         # eg rock, plant, etc.
        self.name = "UNDEF"                         # eg. gold, grass etc.
        self.is_infinite = "True"                   # Are we the gift that keeps giving, like an underwater spring? 
        self.max_quantity = 100                     # Maximum amount of resource at this node
        self.current_quantity = self.max_quantity   # How much is currently left at this node

class Plant(ResourceNode):
    
    # A "plant" in this project is essentially an organic resource node.
    def __init__(self):
        self.type = "PLANT"                         # eg rock, plant, etc.
        self.name = "UNDEF"                         # yes, I know that this is redundant :-)
    

class Creature(UberClass):
    pass

class Species(UberClass):
    # Eg. panthera
    pass

class SubSpecies(Species):
    # Eg. lion
    pass



# % as applied to base factor

ANIMAL_HAS_MUGSHOT = True

ANIMALS_GLOBAL_EFFICIENCY_PERCENTAGE = 100


class Animal(Creature):
    # Specific intance of an animal, like "Simba the lion".  
    def __init__(self, name, age):
        self.species = 'unspecified'
        self.subspecies = 'unspecified'
        self.attributes = initialise_attributes()        

        self.animated = ALL_ANIMALS_ANIMATED and ARE_NPCS_ANIMATED
        self.animation_speed = int((ANIMALS_ANIMATION_SPEED_PERCENTAGE / 100) * ALL_ANIMALS_ANIMATION_SPEED)
        
    pass

class Person(Creature):
    # Creates a speciifc instance of a person (eg. "bob")
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skin_colour = 'undef'
        self.hair_colour = 'undef'
        self.clothing = set()
        self.kit = set()
        self.attributes = initialise_attributes()     
        self.animated = ALL_PERSONS_ANIMATED and ARE_NPCS_ANIMATED
        self.animation_speed = int((PERSONS_ANIMATION_SPEED_PERCENTAG / 100) * ALL_ANIMALS_ANIMATION_SPEED)
        

class Tribe(UberClass):
    
    # Define the attributes of a tribe
    def __init__(self, name):
        self.name = name
        # Initialize an empty set to store the persons
        self.members = set()
        self.npc = True

    def add_person(self, person):
        # Add a person to the tribe (usually through specific addition or birth)
        # (All persons belong to a tribe, even if the tribe consists of only one person)
        self.members.add(person)
        
    def remove_person(self, person):
    # Remove a person to the tribe (usually through expulsion or death)
        if person in self.members:
            self.members.remove(person)
            

import pygame

class MapCanvas:
    # Dedicated canvas for drawing a map.

    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.surface = pygame.Surface((width, height))  # Create a Pygame surface
        self.map_data = None  # Placeholder for map data (modify as needed)

    def draw_map(self):

        # Clear the map canvas
        self.surface.fill((255, 255, 255))  # Example: fill with white

        # Draw map elements using self.surface (lines, shapes, etc.)

    def map_is_visible(self):
        return self.map_data is not None  # Modify based on your map data handling

    def set_map_data(self, data):
        
        # Sets the map data for the map canvas.

        self.map_data = data
        self.draw_map()  # Update map based on new data (optional)

    def clear():
        pass





