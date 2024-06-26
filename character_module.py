from os import error
import os
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

    def __init__(self, name: str, type: str, x: int =0, y: int =0, gold =0, inv = {}, health = 10, damage = 1, defense = 0) -> None:
        self.type = type
        self.x = x
        self.y = y
        self.colour = colours.colours_dict[character_Icons[self.type]['colour']]
        self.name = f"{self.colour}{name}{colours.DEFAULT}"
        self.icon = character_Icons[self.type]['icon']
        self.alive = True
        self.file = 'character.json'
        self.gold = gold
        self.inventory = inv
        self.health = health
        self.damage = damage
        self.defense = defense

    def move(self, x, y, map:map_module.Map) -> None:
        if (x == +1 and map.map_data[self.y][self.x + 1].isWalkable) or (x == -1 and map.map_data[self.y][self.x - 1].isWalkable):
            self.x += x
        
        if (y == +1 and map.map_data[self.y + 1][self.x].isWalkable) or (y == -1 and map.map_data[self.y - 1][self.x].isWalkable):
            self.y += y

    def set_icon(self):
        self.colour = colours.DEFAULT
        raise error

    def attack(self, other):
        if self.alive and other.alive:
            damage = self.damage - other.defense
            if damage > 0:
                other.health -= damage
                if other.health <= 0:
                    other.alive = False
        return damage

    def looting(self, other):
        os.system('cls')
        if not other.alive and other.gold > 0:
            self.gold += other.gold
            print(f"{self.name} looted {other.gold} gold from {other.name}")
            input("Press Enter to continue...")
        if len(other.inventory) > 2:
            self.inventory.update(other.inventory)
            print(f"{self.name} looted {list(other.inventory.keys())} from {other.name}")
            input("Press Enter to continue...")

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