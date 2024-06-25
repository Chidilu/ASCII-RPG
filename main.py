import os
from pynput.keyboard import Key, Listener
import colours
import map_module
import character_module

def main():
    menu = True
    play = False
    play_Menu = False

    map = map_module.Map(50, 50)
    hero: character_module.Character

    def show(key):
        nonlocal menu, play
        if hasattr(key, 'char'):
            key_char = key.char
            if key_char == 'w':
                if hero.y > 0:
                    hero.move(0, -1)
                    return False
                else: return False
            elif key_char == 'a':
                if hero.x > 0:
                    hero.move(-1, 0)
                    return False
                else: return False
            elif key_char == 's':
                if hero.y < map.height -1:
                    hero.move(0, +1)
                    return False
                else: return False
            elif key_char == 'd':
                if hero.x < map.width -1:
                    hero.move(1, 0)
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
                    hero.move(0, -1)
                    return False
                else: return False
            elif key == Key.left:
                if hero.x > 0:
                    hero.move(-1, 0)
                    return False
                else: return False
            elif key == Key.down:
                if hero.y < map.height -1:
                    hero.move(0, +1)
                    return False
                else: return False
            elif key == Key.right:
                if hero.x < map.width -1:
                    hero.move(1, 0)
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
                print(f"{colours.RED}9, QUIT GAME")

            choice = input(f"{colours.DEFAULT}\n# ")

            if choice == "1" and not play_Menu:
                os.system('cls')
                name = input(f"{colours.PURPLE}What is your name, hero?{colours.DEFAULT}\n> ")
                if name == "":
                    name = f"{colours.PURPLE}Hero{colours.DEFAULT}"
                hero = character_module.Character(name, 'hero', 0, 0)
                play = True
                menu = False
                play_Menu = True
                # Save
            elif choice == "1" and play_Menu:
                play = True
                menu = False
                continue
            elif choice == "2":
                try:
                    # Load
                    raise BaseException("Loading should be designed")
                    play = True
                    menu = False
                    continue
                except:
                    print("No save found")
            elif choice == "9":
                quit()

        while play:
            os.system('cls')
            map.display_map(hero)
            map.get_description(hero)
            with Listener(on_press = show, suppress= True) as listener:   
                listener.join()



if __name__ == "__main__":
    main()
