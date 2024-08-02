from random import randint
from art  import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess , answer , turns):
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it , Your answer is {answer}")

def set_difficulty():
    level = input("choose a difficulty. Type 'easy' or 'hard' : ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return  HARD_LEVEL_TURNS

def game():
    print(logo)

    print("WelCome to Number Guessing Game")
    print("I am thinking of a number between 1 and 100")
    answer = randint(1,100)
    print(f"pssst, the correct answer is {answer}")

    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number")

        guess = int(input("Make a guess : "))

        turns = check_answer(guess , answer , turns)
        if turns ==0:
            print("you have run out of guesses you lose")
            return
        elif guess != answer:
            print("Guess Again ")
game()