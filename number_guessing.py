import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Type a number greater than 0. ")
        quit()
else:
    print("Type a guess")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Type a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Type a number. ")
        continue

    if user_guess == random_number:
        print("true")
        break
    elif user_guess > random_number:
        print("reduce the number")
    else:
        print("increase number")

print("You got it in", guesses, "guesses")
         
       
            