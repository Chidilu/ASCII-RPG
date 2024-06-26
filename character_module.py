from os import error
import colours
import json
import map_module
import tile_module

character_Icons = {
    'hero': {
        'icon': 'H',
        'colour': 'BLUE'
    },
    'goblin': {
        'icon': 'G',
        'colour': 'RED'
    },
    'orc': {
        'icon': 'O',
        'colour': 'GREEN'
    },
    'troll': {
        'icon': 'T',
        'colour': 'YELLOW'
    },
    'dragon': {
        'icon': 'D',
        'colour': 'PURPLE'
    }
}

class Character():
    global character_Icons

    def __init__(self, name: str, type: str, x: int =0, y: int =0, inv = {}) -> None:
        self.type = type
        self.name = name
        self.x = x
        self.y = y
        self.colour = colours.colours_dict[character_Icons[self.type]['colour']]
        self.icon = character_Icons[self.type]['icon']
        self.health = 10
        self.attack = 1
        self.alive = True
        self.file = 'character.json'
        self.inventory = inv

    def move(self, x, y, map:map_module.Map) -> None:
        if (x == +1 and map.map_data[self.y][self.x + 1].isWalkable) or (x == -1 and map.map_data[self.y][self.x - 1].isWalkable):
            self.x += x
        
        if (y == +1 and map.map_data[self.y + 1][self.x].isWalkable) or (y == -1 and map.map_data[self.y - 1][self.x].isWalkable):
            self.y += y

    def set_icon(self):
        self.colour = colours.DEFAULT
        raise error

    def attack(self, other):
        other.health -= self.attack
        print(f"{self.name} attacks {other.name} for {self.attack} damage.")
        if other.health <= 0:
            print(f"{other.name} has been defeated!")
            other.alive = False

    def save_character(self) -> None:
        with open(self.file, 'w') as f:
            f.write(json.dumps(self.__dict__()))
    
    def __dict__(self):
        return {
            'name': self.name,
            'type': self.type,
            'x': self.x,
            'y': self.y,
            'inv': self.inventory
        }