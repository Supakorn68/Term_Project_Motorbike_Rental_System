def display_heroes(heroes):
    """Displays all heroes in the list."""
    if heroes:
        print("Current Heroes:")
        for i, hero in enumerate(heroes):
            print(f"{i+1}. {hero}")
    else:
        print("No heroes to display.")

def add_hero(heroes, new_hero):
    """Adds a new hero to the list."""
    heroes.append(new_hero)
    print(f"'{new_hero}' has been added.")

def insert_hero(heroes, new_hero, position):
    """Inserts a new hero at a specified position."""
    try:
        heroes.insert(position - 1, new_hero)  # Adjust for 0-based indexing
        print(f"'{new_hero}' has been inserted at position {position}.")
    except IndexError:
        print(f"Error: Position {position} is out of bounds.")

def remove_hero(heroes, hero_to_remove):
    """Removes a hero from the list."""
    try:
        heroes.remove(hero_to_remove)
        print(f"'{hero_to_remove}' has been removed.")
    except ValueError:
        print(f"Error: '{hero_to_remove}' not found in the list.")

def display_sorted_heroes(heroes, ascending=True):
    """Displays heroes in sorted order (ascending or descending)."""
    sorted_heroes = sorted(heroes, reverse=not ascending)
    order = "Ascending" if ascending else "Descending"
    print(f"\nHeroes ({order} Order):")
    for i, hero in enumerate(sorted_heroes):
        print(f"{i+1}. {hero}")

def main():
    heroes = ['Ironman', 'Thor', 'Hulk', 'Spiderman']

    while True:
        print("\n--- HEROES.PY EXERCISE-I ---")
        print("1. Display Heroes")
        print("2. Add Heroes")
        print("3. Insert Heroes")
        print("4. Remove Heroes")
        print("5. Display Sorted Heroes (Ascending / Descending)")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_heroes(heroes)
        elif choice == '2':
            new_hero = input("Enter the name of the hero to add: ")
            add_hero(heroes, new_hero)
        elif choice == '3':
            new_hero = input("Enter the name of the hero to insert: ")
            try:
                position = int(input("Enter the position to insert (e.g., 1 for first): "))
                insert_hero(heroes, new_hero, position)
            except ValueError:
                print("Invalid input. Please enter a number for the position.")
        elif choice == '4':
            hero_to_remove = input("Enter the name of the hero to remove: ")
            remove_hero(heroes, hero_to_remove)
        elif choice == '5':
            sort_choice = input("Sort in (A)scending or (D)escending order? (A/D): ").lower()
            if sort_choice == 'a':
                display_sorted_heroes(heroes, ascending=True)
            elif sort_choice == 'd':
                display_sorted_heroes(heroes, ascending=False)
            else:
                print("Invalid sort choice. Displaying ascending by default.")
                display_sorted_heroes(heroes)
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()