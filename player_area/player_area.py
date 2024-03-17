# player_area.py
# Author: JC
# Last mod: 2024-mar-17

import math

class Chunk:
    def __init__(self, chunk_id):
        self.chunk_id = chunk_id
        self.terrain = {}  # Dictionary to store terrain percentages

def generate_player_area_map(radius_km, chunk_size_km):

    
    # Generates a grid of Chunk objects representing the PLAYER_AREA.
    # The chunks are squares (width of chunk_size_km) within the PLAYER_AREA, 
    # arranged in a circle of radius radius_km
    
    # Returns:
    #    A list of Chunk objects representing the PLAYER_AREA grid.
        
    chunks_per_side = math.ceil(radius_km * 2 / chunk_size_km)
    total_chunks = chunks_per_side * chunks_per_side
    num_chunks = total_chunks

    # Create a list to store the chunks
    player_area_map = []

    # Create a grid of chunk objects (using placeholder logic for now)
    for chunk_id in range(1, num_chunks + 1):
        chunk = Chunk(chunk_id)
        # Placeholder for initializing terrain - replace this later
        chunk.terrain = {"HI": 20, "DE": 50, "RI": 10, "FO": 20}
        player_area_map.append(chunk)

    return player_area_map

# Example usage (assuming you want to test with a 5km radius)
player_area_map = generate_player_area_map(5, 0.5)

# Print the chunks in a basic format (you can enhance this later)
for chunk in player_area_map:
    print(f"Chunk {chunk.chunk_id}:")
    for terrain_type, percentage in chunk.terrain.items():
        print(f"{terrain_type}: {percentage}")