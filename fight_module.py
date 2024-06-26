import os
import sys
import player_module, enemy_module

def fighting(player, enemy):
        os.system('cls')
        while True:
            print(f"Player's health: {player.health}")
            print(f"Enemy's health: {enemy.health}")

            print("What do you want to do?")
            print("1. Attack")
            print("2. Run\n")
            choice = input("> ")

            if choice == '1':
                x = player.attack(enemy)
                print(f"{player.name} dealt {x} damage to {enemy.name}")
            elif choice == '2':
                print("You ran away!")
                return False
            
            if enemy.health <= 0:
                input(f"{enemy.name} has been defeated")
                player.looting(enemy)
                return False

            x = enemy.attack(player)
            print(f"{enemy.name} dealt {x} damage to {player.name}")

            if player.health <= 0:
                os.system('cls')
                print(f"Player's health: {player.health}")
                print(f"Enemy's health: {enemy.health}")

                input("\nYou died! Game over.")
                sys.exit()
            
            input()
            os.system('cls')

        return False