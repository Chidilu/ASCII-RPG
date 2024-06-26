import json
import mapGeneration_module
import tile_module
import sys
import colours
import random
import math

class Map():
    def __init__(self, width: int, height: int) -> None:
        if width < 5:
            raise ValueError("Width must be at least 5")
        if height < 5:
            raise ValueError("Height must be at least 5")
        
        self.file = "map.json"
        self.map_data: list = []
        self.width: int = width
        self.height: int = height
        self.load_map()
    
    def load_map(self) -> None:
        try:
            with open(self.file, 'r') as f:
                self.map_data = json.load(f)
                if self.width != len(self.map_data):
                    self.make_map()
        except FileNotFoundError as e:
            print(e)
            self.make_map()
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            sys.exit()
        except Exception as e:
            print(f"Error initializing map: {e}")
            sys.exit()
        

    def save_map(self) -> None:
        x = self.to_json(self.map_data)
        with open(self.file, 'w') as f:
            json.dump(x, f)

    def make_map(self) -> None:
        self.map_data = [[tile_module.Tile(k, i, 'plain') for k in range(self.width)] for i in range(self.height)]
        self.save_map()

    def display_map(self, character) -> None:
        char_x = character.x
        char_y = character.y
        start_x = max(char_x - 2, 0)
        end_x = min(char_x + 3, self.width)
        start_y = max(char_y - 2, 0)
        end_y = min(char_y + 3, self.height)

        if end_x - start_x < 5:
            if start_x == 0:
                end_x = min(5, self.width)
            else:
                start_x = max(0, self.width - 5)
        
        if end_y - start_y < 5:
            if start_y == 0:
                end_y = min(5, self.height)
            else:
                start_y = max(0, self.height - 5)

        frame = f"{colours.RED}X {'= ' * (end_x - start_x)}X{colours.DEFAULT}"
        print(frame)

        for y in range(start_y, end_y):
            print(f"{colours.RED}| {colours.DEFAULT}", end='')
            for x in range(start_x, end_x):
                if y == char_y and x == char_x:
                    print(f'{character.colour}{character.icon}{colours.DEFAULT}', end=' ')
                else:
                    if self.map_data[y][x].tileType == '█' and self.map_data[y][x].tileType != None:
                        if self.map_data[y][x].x < end_x-1:
                            if self.map_data[y][x+1].tileType != '█':
                                print(f"{self.map_data[y][x].tileColour}{self.map_data[y][x].tileType}{colours.DEFAULT}", end=' ')
                                continue
                        print(f"{self.map_data[y][x].tileColour}{self.map_data[y][x].tileType}", end=f'█{colours.DEFAULT}')
                    else:
                        print(f"{self.map_data[y][x].tileColour}{self.map_data[y][x].tileType}{colours.DEFAULT}", end=' ')
            print(f"{colours.RED}|{colours.DEFAULT}")
        print(frame)
    
    def get_description(self, character):
        print(f"{self.map_data[character.y][character.x].tileDescription}")

    def to_json(self, obj):
        return json.dumps(obj, default=lambda obj: obj.__dict__)




    def create_biome_patch(self, biome_name, shape, start_x, start_y, size):
        if shape == 'rectangle':
            width, height = size
            self._create_rectangle_patch(biome_name, start_x, start_y, width, height)
        elif shape == 'circle':
            radius = size
            self._create_circle_patch(biome_name, start_x, start_y, radius)
        elif shape == 'blob':
            irregularity = size
            self._create_blob_patch(biome_name, start_x, start_y, irregularity)

    def _create_rectangle_patch(self, biome_name, start_x, start_y, width, height):
        for x in range(start_x, start_x + width):
            for y in range(start_y, start_y + height):
                if 0 <= x < self.width and 0 <= y < self.height:
                    self.map_data[y][x].tileName = biome_name
                    self.map_data[y][x].update_tile()

    def _create_circle_patch(self, biome_name, center_x, center_y, radius):
        for x in range(center_x - radius, center_x + radius + 1):
            for y in range(center_y - radius, center_y + radius + 1):
                dist_sq = (x - center_x) ** 2 + (y - center_y) ** 2
                if radius ** 2 * 0.75 < dist_sq <= radius ** 2:
                    if 0 <= x < self.width and 0 <= y < self.height:
                        continue
                elif dist_sq < radius ** 2:
                    if 0 <= x < self.width and 0 <= y < self.height:
                        self.map_data[y][x].tileName = biome_name
                        self.map_data[y][x].update_tile()

    def _create_blob_patch(self, biome_name, start_x, start_y, irregularity):
        num_points = irregularity * 10
        points = [(start_x, start_y)]
        
        for _ in range(num_points):
            direction = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
            new_point = (points[-1][0] + direction[0], points[-1][1] + direction[1])
            if 0 <= new_point[0] < self.width and 0 <= new_point[1] < self.height:
                points.append(new_point)

        for x, y in points:
            if 0 <= x < self.width and 0 <= y < self.height:
                self.map_data[y][x].tileName = biome_name
                self.map_data[y][x].update_tile()