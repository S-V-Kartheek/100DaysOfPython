import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
#print(chosen_word)
lives = 6
print(chosen_word)
print("\n"*25)
print(hangman_art.logo)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    display = ""

    if guess in correct_letters:
            print(f"you've already guessed {guess}")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(hangman_art.lose)
            print(f"***********************It was '{chosen_word}'**********************")

    if "_" not in display:
        game_over = True
        print("\n"*30)
        print(hangman_art.won)
        print("********************************************************")


    print(hangman_art.stages[lives])
