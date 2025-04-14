import random
target = random.randint(1, 10)
attempts = 5

for i in range(attempts):
    guess = int(input("Guess the number (1–10): "))
    if guess == target:
        print("Correct number!")
        break
    elif guess < target:
        print("Too low.")
    else:
        print("Too high.")
else:
    print("Game Over. The number was", target)
