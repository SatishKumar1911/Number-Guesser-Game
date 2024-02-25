print()
print("**********Welcome to Number Guessing Game**********")
print()

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

playing = input("Do you want to play? [yes/no] ").lower()
print()

if playing != "yes":
    quit()

from random import randint
low = 1
high = 10
random_number = randint(low, high)  # 7

end_game = False
guess_attempt = 0

while not end_game:
    try:
        guess = int(input("Guess a number between 1 to 10: "))   # 3, 7, 9
    except ValueError:
        guess = 0
    
    if guess < 1 or guess > 10:
        guess_attempt += 1
    else:
        if guess > random_number:
            print("Guess Lower")
            guess_attempt += 1
            end_game = False
        elif guess < random_number:
            print("Guess Higher")
            guess_attempt += 1
            end_game = False
        else:
            guess_attempt += 1
            print(f"Hurray! You guessed it in {guess_attempt} attempts :) ")
            print()
            play_again = input("Do you want to play again? [yes/no] ").lower()
            if play_again != "yes":
                end_game = True
                print()
                print("Thanks for playing :) Bye...")
            else:
                guess_attempt = 0
                random_number = randint(low, high)
                clear_screen()