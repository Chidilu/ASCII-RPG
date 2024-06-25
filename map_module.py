import json
import mapGeneration_module
import tile_module
import sys
import colours

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

    def generateMap(self) -> None:
        self.map_data = mapGeneration_module.map_Generation(self.map_data)

    def display_map(self, character) -> None:
        char_x = character.x
        char_y = character.y
        start_x = max(char_x - 2, 0)
        end_x = min(char_x + 3, self.width)
        start_y = max(char_y - 2, 0)
        end_y = min(char_y + 3, self.height)

        # Ensure the 5x5 window is properly centered around the character if possible
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

        # Print the top border of the map view
        frame = f"{colours.RED}X {'= ' * (end_x - start_x)}X{colours.DEFAULT}"
        print(frame)

        for y in range(start_y, end_y):
            print(f"{colours.RED}| {colours.DEFAULT}", end='')
            for x in range(start_x, end_x):
                if y == char_y and x == char_x:
                    print(f'{character.colour}{character.icon}{colours.DEFAULT}', end=' ')  # Character's position
                else:
                    print(f"{self.map_data[y][x].tileColour}{self.map_data[y][x].tileType}{colours.DEFAULT}", end=' ')
            print(f"{colours.RED}|{colours.DEFAULT}")
        
        print(frame)
    
    def get_description(self, character):
        print(f"{self.map_data[character.y][character.x].tileDescription}")

    def to_json(self, obj):
        return json.dumps(obj, default=lambda obj: obj.__dict__)