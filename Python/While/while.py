# for i in range(10):
#     print("i is now {} ".format(i))

# i = 0
# while i < 10:  # while True:  creates an infinite loop
#     print("i is now {} ".format(i))
#     i += 1


# available_exits = ["east", "north east", "south"]
#
# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit == "quit":
#         print("Game Over")
#         break
#
# else:
#     print("Aren't you glad you got out of there!")


import random

# highest = 10
# answer = random.randint(1, highest)
#
# print("Please guess a number between 1 and {}, or choose 0 to end game: ".format(highest))
# guess = int(input())

# Game without While Loop --
# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time!")

# Game with while loop --
# while True:
#     if guess == 0:
#         print("Game over, number was {}".format(answer))
#         break
#     elif guess < answer:
#         print("Please guess higher")
#         guess = int(input())
#     elif guess > answer:
#         print("Please guess lower")
#         guess = int(input())
#     elif guess == answer:
#         print("Well done, you guessed it!")
#         break

# Instructor's version --
highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}, or choose 0 to end game: ".format(highest))
guess = 0

while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    else:
        print("Well done, you guessed it!")
