import random
import hangman_art
import hangman_words
import replit

display = []
end_of_game = False
life = 6
all_guesses = []

chosen_word = random.choice(hangman_words.word_list)
# print(f'The solution is: {chosen_word}.\n')
print(hangman_art.logo)
print("\n")

for i in chosen_word:
    display += "_"
print(display)

while not end_of_game:
    guess = input("\nGuess a letter: \n").lower()
    print("\n")

    replit.clear()

    for p in range(len(chosen_word)):
        letter = chosen_word[p]
        if letter == guess:
            display[p] = letter
            all_guesses.append(guess)
            # print(all_guesses)

    print(display)

    if guess in all_guesses:
        print(f"You have already guessed \"{guess}\". Try another one!")

    if guess not in chosen_word:
        life -= 1
        print(
            f"You guessed \"{guess}\" which is a wrong letter. You lose a life."
        )
        print(hangman_art.stages[life])
        if life == 0:
            print("You Lose!")
            end_of_game = True

    if "_" not in display:
        end_of_game = True
        print("You Win")
