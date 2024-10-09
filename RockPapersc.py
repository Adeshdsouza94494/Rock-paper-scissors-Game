import random

# List of possible choices
item = ['Rock', 'Paper', 'Scissors']

# Get user's choice (convert to title case to handle case insensitivity)
userChoice = input("Enter Your Choice (Rock, Paper, Scissors): ").title()

# Randomly select the computer's choice
computerChoice = random.choice(item)
print(" ")

# Display both choices
print(f"Computer Choice is: {computerChoice}. User choice is: {userChoice}")
print(" ")

# Check for a draw
if userChoice == computerChoice:
    print("It's a Draw")

# Check for user wins
elif (userChoice == 'Rock' and computerChoice == 'Scissors') or \
     (userChoice == 'Scissors' and computerChoice == 'Paper') or \
     (userChoice == 'Paper' and computerChoice == 'Rock'):
    print(f"{userChoice} wins!")

# Check for computer wins
elif (computerChoice == 'Rock' and userChoice == 'Scissors') or \
     (computerChoice == 'Scissors' and userChoice == 'Paper') or \
     (computerChoice == 'Paper' and userChoice == 'Rock'):
    print(f"{computerChoice} wins!")

# Handle invalid input
else:
    print("Invalid input! Please enter Rock, Paper, or Scissors with proper spelling.")
