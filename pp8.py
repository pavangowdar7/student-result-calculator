secret = 7

guess = int(input("Guess the number (1-10): "))

if guess == secret:
    print("Correct guess!")
else:
    print("Wrong guess!")