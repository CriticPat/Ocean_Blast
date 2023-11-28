def display_menu():
    print("Welcome to the Game!")
    print("1. Start Game")
    print("2. Instructions")
    print("3. High Score")
    print("4. Settings")
    print("5. Exit")
    print()

def start_game():
    print("Game is starting...")
    score = 100  
    return score

def display_instructions():
    print("Instructions:")
    print("This is a simple game. Use arrow keys to move.")
    input("Press Enter to go back to the menu.")

def display_high_score(high_score):
    print(f"High Score: {high_score}")
    input("Press Enter to go back to the menu.")

def display_settings():
    print("Settings:")
    print("1. Sound")
    print("2. Graphics")
    input("Press Enter to go back to the menu.")

def update_high_score(current_score, high_score):
    if current_score > high_score:
        high_score = current_score
        print("Congratulations! New high score!")
    return high_score


def main():
    high_score = 0  
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            current_score = start_game()
            high_score = update_high_score(current_score, high_score)
        elif choice == "2":
            display_instructions()
        elif choice == "3":
            display_high_score(high_score)
        elif choice == "4":
            display_settings()
        elif choice == "5":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
