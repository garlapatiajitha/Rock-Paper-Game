import random

# Define the choices
choices = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(choices)

def get_user_choice():
    user_input = input("🎮 Enter your choice (rock, paper, or scissors): ").lower()
    while user_input not in choices:
        print("⚠️ Invalid choice. Please try again.")
        user_input = input("🎮 Enter rock, paper, or scissors: ").lower()
    return user_input

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Main game loop
def play_game():
    user_wins = 0
    computer_wins = 0
    ties = 0

    while True:
        print("\n--- 🌟 Rock-Paper-Scissors Game 🌟 ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\n🧍 You chose: {user_choice.capitalize()}")
        print(f"💻 Computer chose: {computer_choice.capitalize()}")
        
        result = determine_winner(user_choice, computer_choice)
        
        if result == "user":
            print("\n📢 Result: 🎉 You win!")
            user_wins += 1
        elif result == "computer":
            print("\n📢 Result: 💻 Computer wins!")
            computer_wins += 1
        else:
            print("\n📢 Result: 🤝 It's a tie!")
            ties += 1
        
        play_again = input("\n🔄 Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\n--- 🏆 Game Summary 🏆 ---")
            print(f"🎉 Your wins: {user_wins}")
            print(f"💻 Computer wins: {computer_wins}")
            print(f"🤝 Ties: {ties}")
            print("\n👋 Thanks for playing! Goodbye!")
            break

# Start the game
play_game()
