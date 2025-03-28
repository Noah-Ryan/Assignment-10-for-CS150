import Gamefunctions

def main():
    name = input("Enter your name: ")
    Gamefunctions.print_welcome(name, 40)
    print()
    user_hp = 50
    user_gold = 20
    max_hp = 100
    user_inventory = []
    equipped_weapon = None
    while True:
        print(f"\nYou have {user_hp} HP and {user_gold} gold.")
        print("What would you like to do?")
        print("  1) City")
        print("  2) Fight a monster outside of the city")
        print("  3) Sleep (Restore up to 10 HP)")
        print("  4) Visit the shop")
        print("  5) Manage Inventory")
        print("  6) Quit")
        choice = input("Enter your choice: ")
        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice. Please try again.")
            continue
        if choice == "1":
            print("\nYou head to the city. You see beautiful buildings, and shops all around")
        elif choice == "2":
            user_hp, user_gold = Gamefunctions.fight_monster(user_hp, user_gold, user_inventory, equipped_weapon)
            if user_hp <= 0:
                print("\nYou died. Game Over.")
                break
        elif choice == "3":
            heal_amount = 10
            old_hp = user_hp
            user_hp = min(user_hp + heal_amount, max_hp)
            print(f"\nYou rest, restoring {user_hp - old_hp} HP. Your HP is now {user_hp}.")
        elif choice == "4":
            user_gold, user_inventory = Gamefunctions.buy_from_shop(user_gold, user_inventory)
        elif choice == "5":
            equipped_weapon = Gamefunctions.manage_inventory(user_inventory, equipped_weapon)
        elif choice == "6":
            print("\nThanks for playing!")
            break
    print("Exiting game.")

if __name__ == "__main__":
    main()
