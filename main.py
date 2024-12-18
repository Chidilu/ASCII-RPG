import os
from pynput.keyboard import Key, Listener
import colours
import map_module
import character_module, player_module, fight_module
from enemy_module import setEnemyLocations
import json
import sys
from pathlib import Path

def main():
    menu = True
    play = False
    play_Menu = False
    fight = False
    enemy: character_module.Character

    MAPX = 50
    MAPY = 50

    map: map_module.Map
    hero: player_module.Player

    def show(key):
        nonlocal menu, play, hero, map
        if hasattr(key, 'char'):
            key_char = key.char
            if key_char == 'w':
                if hero.y > 0:
                    hero.move(0, -1, map)
                    return False
                else: return False
            elif key_char == 'a':
                if hero.x > 0:
                    hero.move(-1, 0, map)
                    return False
                else: return False
            elif key_char == 's':
                if hero.y < map.height -1:
                    hero.move(0, +1, map)
                    return False
                else: return False
            elif key_char == 'd':
                if hero.x < map.width -1:
                    hero.move(1, 0, map)
                    return False   
                else: return False     
            elif key_char == 'q':
                menu = True
                play = False
                return False
            else: return False
        else:
            if key == Key.esc:
                menu = True
                play = False
                return False
            elif key == Key.up:
                if hero.y > 0:
                    hero.move(0, -1, map)
                    return False
                else: return False
            elif key == Key.left:
                if hero.x > 0:
                    hero.move(-1, 0, map)
                    return False
                else: return False
            elif key == Key.down:
                if hero.y < map.height -1:
                    hero.move(0, +1, map)
                    return False
                else: return False
            elif key == Key.right:
                if hero.x < map.width -1:
                    hero.move(1, 0, map)
                    return False   
                else: return False
            else: return False

    while True:
        while menu:
            os.system('cls')
            if not play_Menu:
                print(f"{colours.PURPLE}Welcome to the Slayer's uprising\n")
                print(f"{colours.YELLOW}1, NEW GAME")
                print(f"{colours.BLUE}2, LOAD GAME")
                print(f"{colours.RED}9, QUIT GAME")
            else:
                print(f"{colours.YELLOW}1, CONTINUE GAME")
                print(f"{colours.BLUE}2, LOAD GAME")
                print(f"{colours.GREEN}3, SAVE GAME")
                print(f"{colours.RED}9, QUIT GAME")

            choice = input(f"{colours.DEFAULT}\n# ")

            if choice == "1" and not play_Menu:
                # Start
                os.system('cls')
                generate_dir()
                name = input(f"{colours.PURPLE}What is your name, hero?{colours.DEFAULT}\n> ")
                if name == "":
                    name = f"Hero"
                map = map_module.Map(MAPX, MAPY)
                setEnemyLocations([MAPX, MAPY])
                hero = player_module.Player(name)
                play = True
                menu = False
                play_Menu = True
                hero.save_character()
                map.make_map()
                generate_new_map(map)
                map.save_map(hero)
                continue
            elif choice == "1" and play_Menu:
                # Continue
                play = True
                menu = False
                continue
            elif choice == "2":
                try:
                    # Load
                    hero = load_character()
                    map = load_map()
                    play = True
                    menu = False
                    play_Menu = True
                    continue
                except:
                    print("No save found")
                    input()
            elif choice == '3' and play_Menu:
                # Save
                map.save_map(hero)
                hero.save_character()
            elif choice == "9":
                # Quit
                os.system('cls')
                quit()

        while play:
            if map.getEnemy(hero) != None:
                tempEnemy = map.getEnemy(hero)
                enemy = character_module.Character(tempEnemy[0], tempEnemy[1])
            else:
                enemy = None
            
            if map.event(hero) == "fight" and enemy != None:
                os.system('cls')
                fight = True

            if fight:
                os.system('cls')
                fight = fight_module.fighting(hero, enemy, map)
            os.system('cls')
            map.display_map(hero)
            print(f"{colours.YELLOW}Your Position: X={hero.x} Y={hero.y}{colours.DEFAULT}")
            map.get_description(hero)
            with Listener(on_press = show, suppress= True) as listener:
                listener.join()

def generate_new_map(map):
    map.create_biome_patch("forest", 'blob', 5, 5, 10)
    map.create_biome_patch("forest", 'blob', 45, 5, 7)
    map.create_biome_patch("forest", 'circle', 15, 45, 4)
    map.create_biome_patch("forest", 'blob', 25, 35, 13)
    map.create_biome_patch("mountain", 'blob', 15, 20, 5)
    map.create_biome_patch("mountain", 'circle', 20, 5, 5)
    map.create_biome_patch('walls', 'rectangle', 40, 40, [5, 10])
    map.create_biome_patch('gate', 'rectangle', 40, 45, [1, 1])
    map.create_biome_patch('plain', 'rectangle', 41, 41, [3, 8])

def generate_dir():
    try:
        Path('saves/player').mkdir(parents=True, exist_ok=True)
        Path('saves/map').mkdir(parents=True, exist_ok=True)
        Path('saves/enemy').mkdir(parents=True, exist_ok=True)
    except Exception as e:
        input(e)


def load_character():
    file = 'saves/player/hero.json'
    try:
        with open(file, 'r') as f:
            save_Dict: dict = json.load(f)
            name, x, y = ['Hero', 0, 0,]
            for i in save_Dict.items():
                if i[0] == 'name':
                    name = i[1]
                elif i[0] == 'x':
                    x = i[1]
                elif i[0] == 'y':
                    y = i[1]
            return player_module.Player(name, x, y)
    except FileNotFoundError as e:
        print(e)
        sys.exit()
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        sys.exit()
    except Exception as e:
        print(f"Error initializing character: {e}")
        sys.exit()

def load_map() -> None:
    file = 'saves/map/map_hero.json'
    try:
        with open(file, 'r') as f:
            save_Dict: dict = json.load(f)
            width, height, save_Tile_dict = [50, 50, {}]
            for i in save_Dict.items():
                if i[0] == 'width':
                    width = i[1]
                elif i[0] == 'height':
                    height = i[1]
                elif i[0] == 'map_data':
                    save_Tile_dict = i[1]
            map = map_module.Map(width, height)
            
            for y in range(height):
                for x in range(width):
                    for i in save_Tile_dict[y][x].items():
                        if i[0] == 'tileName':
                            tileName = i[1]
                        elif i[0] == 'isTransparent':
                            isTransparent = i[1]
                        elif i[0] == 'isBlocking':
                            isBlocking = i[1]
                        elif i[0] == 'isDoor':
                            isDoor = i[1]
                        elif i[0] == 'doorDirection':
                            doorDirection = i[1]
                        elif i[0] == 'isStair':
                            isStair = i[1]
                        elif i[0] == 'stairDirection':
                            stairDirection = i[1]
                        elif i[0] == 'isExit':
                            isExit = i[1]
                        elif i[0] == 'exitDirection':
                            exitDirection = i[1]
                        elif i[0] == 'isItem':
                            isItem = i[1]
                        elif i[0] == 'itemID':
                            itemID = i[1]
                        elif i[0] == 'isNPC':
                            isNPC = i[1]
                        elif i[0] == 'nPCID':
                            nPCID = i[1]
                        elif i[0] == 'isEvent':
                            isEvent = i[1]
                        elif i[0] == 'eventID':
                            eventID = i[1]
                        elif i[0] == 'isTrigger':
                            isTrigger = i[1]
                        elif i[0] == 'triggerID':
                            triggerID = i[1]
                    map.set_tile(x, y, tileName, isTransparent, isBlocking, isDoor, doorDirection, isStair, stairDirection, isExit, exitDirection, isItem, itemID, isNPC, nPCID, isEvent,eventID, isTrigger, triggerID)
            return map
    
    except FileNotFoundError as e:
        print(e)
        sys.exit()
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        sys.exit()
    except Exception as e:
        print(f"Error initializing map: {e}")
        sys.exit()


if __name__ == "__main__":
    main()
