secretWord = "girraffe"
guess = ""
guessCount = 0
guesslimit = 3
out_of_guesses = False

while guess != secretWord and not(out_of_guesses):   #the loop goes on as long as the conditions here are true
    if guessCount < guesslimit:
        guess = input("Enter guess: ")
        guessCount += 1 #incrementing the guess count
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("you win")





