from os import error
import colours

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

    def __init__(self, name: str, type: str, x: int =0, y: int =0) -> None:
        self.type = type
        self.name = name
        self.x = x
        self.y = y
        self.colour = colours.colours_dict[character_Icons[self.type]['colour']]
        self.icon = character_Icons[self.type]['icon']
        self.health = 10
        self.attack = 1
        self.alive = True

    def move(self, x, y) -> None:
        self.x += x
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