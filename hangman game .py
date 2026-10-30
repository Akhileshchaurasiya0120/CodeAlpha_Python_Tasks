import random

# 5 predefined words list
words_list = ["python", "coding", "laptop", "banana", "mango","guitar"]
secret_word = random.choice(words_list)

guessed_letters = []
incorrect_guesses = 0
max_lives = 6

print("--- Welcome to Hangman Game ---")

# Main Game Loop
while incorrect_guesses < max_lives:
    
    # Display the current status of the word
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
            
    print("\nWord: " + display_word)
    print(f"Remaining lives: {max_lives - incorrect_guesses}")
    
    # Check if the player won
    if "_" not in display_word:
        print("🎉 Congratulations! You Won!")
        break

    # Get input from player
    guess = input("Guess a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in secret_word:
        print("✅ Correct guess!")
    else:
        print("❌ Wrong guess!")
        incorrect_guesses += 1

# Check if player lost
if incorrect_guesses == max_lives:
    print(f"\n💀 Game Over! The correct word was: {secret_word}")
