import random
score = 0

def roundStart():
    plMove = input("What will you do? (Rock, Paper, Scissors) ")
    global score
    choiceList = [1,2,3]
    choice = random.choice(choiceList)
    if choice == 1 and plMove == "Rock":
        print("I choose rock! We tied.")
        print("Your score is",str(score))
        print()
        roundStart()
    if choice == 2 and plMove == "Rock":
        print("I choose paper! You lose.")
        score -= 1
        print("Your score is",str(score))
        print()
        roundStart()
    if choice == 3 and plMove == "Rock":
        print("I choose scissors! You win.")
        score += 1
        print("Your score is",str(score))
        print()
        roundStart()
    if choice == 1 and plMove == "Paper":
        print("I choose rock! You win.")
        score += 1
        print("Your score is",str(score))
        print()
        roundStart()
    if choice == 2 and plMove == "Paper":
        print("I choose paper! We tied.")
        print("Your score is",str(score))
        print()
        roundStart()
    if choice == 3 and plMove == "Paper":
        print("I choose scissors! You lose.")
        score -= 1
        print("Your score is",str(score))
        print()
        roundStart()
    if choice == 1 and plMove == "Scissors":
        print("I choose rock! You Lose.")
        score -= 1
        print("Your score is",str(score))
        print()
        roundStart()
    if choice == 2 and plMove == "Scissors":
        print("I choose paper! You win.")
        score += 1
        print("Your score is",str(score))
        print()
        roundStart()
    if choice == 3 and plMove == "Scissors":
        print("I choose scissors! We tied.")
        print("Your score is",str(score))
        print()
        roundStart()

try:
    roundStart()
except ValueError:
    print("Please select 'Rock', 'Paper', or 'Scissors'")
    roundStart()
