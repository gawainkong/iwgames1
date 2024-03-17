# uberClass.py
# author: JC
# Last mod: 2024-03-13 1500


import datetime

class UberClass(object):
   
    def __init__(self) -> None:
        
        self.attributes = {}  # Empty dictionary to store abilities
        self.project_type = project_type  # In initial development, this is likely to be "TREES" or "POLI", reflecting the particular project
        
        # debugging info
        self.creation_time = datetime.datetime.now()
        self.formatted_initTime = self.initTime.strftime("%Y-%m-%d %H:%M:%S")
        
    def bugReport(self):
        # for collecting user reported bug reports
        pass
    
    def displayInfo(self):
        # for displaying user functionality help
        pass
    
    def displayHistory(self):
        # for displaying historical/real world data about this item
        pass

    def modify_attribute(self, attribute_name, new_value):
        # modifies/creates an atrrtibute of a class, usually an NPC
        self.abilities[attribute_name] = new_value
            
    def add_attribute(self, name, value):
        """Adds a new ability with the given name and value"""
        self.abilities[name] = value

    def get_attribute(self, name):
        """Returns the value of an ability with the given name"""
        return self.abilities.get(name, 0)  # Return 0 if the ability doesn't exist

    def modify_attribute(self, name, modifier):
        # Modifies a number modifier by addition
        self.abilities[name] = self.get_ability(name) + modifier

class iwApp(UberClass):
        pass



