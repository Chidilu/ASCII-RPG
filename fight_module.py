import os
import sys
import player_module, enemy_module
import colours

def fighting(player, enemy, map):
        os.system('cls')
        while True:
            print(f"{player.name}'s health: {colours.BRIGHT_RED}{player.health}{colours.DEFAULT}")
            print(f"{enemy.name} the {(enemy.type).capitalize()}'s health: {colours.BRIGHT_RED}{enemy.health}{colours.DEFAULT}")

            print("What do you want to do?")
            print("1. Attack")
            print("2. Run\n")
            choice = input("> ")

            if choice == '1':
                x = player.attack(enemy)
                print(f"{player.name} dealt {colours.BRIGHT_YELLOW}{x}{colours.DEFAULT} damage to {enemy.name}")
            elif choice == '2':
                print("You ran away!")
                return False
            
            if enemy.health <= 0:
                input(f"{enemy.name} has been defeated")
                player.looting(enemy)
                map.setEvent_flag(player, False)
                return False

            x = enemy.attack(player)
            print(f"{enemy.name} dealt {colours.BRIGHT_YELLOW}{x}{colours.DEFAULT} damage to {player.name}")

            if player.health <= 0:
                os.system('cls')
                print(f"Player's health: {player.health}")
                print(f"Enemy's health: {enemy.health}")

                input("\nYou died! Game over.")
                sys.exit()
            
            input()
            os.system('cls')

        return False