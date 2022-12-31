#building a guessing game
secret_word = "matrix"
guess = ""
number_of_guesses = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word:
    if number_of_guesses < guess_limit:
        guess = input("Please guess the secret word: ")
        number_of_guesses += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You did not escape the matrix.")
else:
    print("You escaped the matrix.")
