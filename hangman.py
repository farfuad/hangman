from img import logo
import random
import data
import img

display = []

chosen_word = random.choice(data.word_list)

word_length = len(chosen_word)

for _ in range(word_length):
    display.append("_")

lives = 6

print(logo)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):

        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, thats not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")

    print(img.stages[lives])
