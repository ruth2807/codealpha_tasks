import random

words = ["python", "intern", "code", "project", "hangman"]
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("🎮 Welcome to Hangman!")

while incorrect_guesses < max_attempts:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)

    if display_word == word:
        print("🎉 Congratulations! You guessed the word!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        incorrect_guesses += 1
        print("❌ Wrong guess! Attempts left:", max_attempts - incorrect_guesses)

if incorrect_guesses == max_attempts:
    print("💀 Game over! The word was:", word)
