# This is a game called Hangman coded in Python
user = input("What is your name? ")
print(f"Hello {user} Let's play Hangman")

word= 'outstanding'
ready = input("Shall we start the guess?(Yes/No)")
guess = ''
turns = 10

if ready == 'Yes':
    print("You have 10 turns..")
    print(f"Lets guess {user}!!")
    while turns > 0:
        failed = 0
        for char in word:
            if char in guess:
                print(char, end='')

            else:
                print("_", end='')
                failed+=1

        if failed == 0:
            print("You won!!")
            break

        letter = input("Guess a character: ")
        guess += letter

        if letter not in word:
            turns -= 1
            print("!!Nuh Uh!! Wrong Guess")
            print(f"You have {turns} turns left to guess..")

            if turns == 0:
                print("You Lose!!")
                print("Better Luck next time.")
else:
    print("See you again")