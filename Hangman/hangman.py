import random

# Hangman stages
hangman_stages = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]

# Game variables
word_list = ["python", "hangman", "challenge", "programming"]
secret_word = random.choice(word_list)
guessed_letters = []
wrong_attempts = 0
max_attempts = len(hangman_stages) - 1

# Function to display the current state
def display_current_state():
    print(hangman_stages[wrong_attempts])
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in secret_word])
    print(f"Word: {display_word}")
    print(f"Guessed Letters: {', '.join(guessed_letters)}")

# Main game loop
while wrong_attempts < max_attempts:
    display_current_state()
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        if all(letter in guessed_letters for letter in secret_word):
            print(f"Congratulations! You've guessed the word: {secret_word}")
            break
    else:
        wrong_attempts += 1

if wrong_attempts == max_attempts:
    display_current_state()
    print(f"Game Over! The word was: {secret_word}")
