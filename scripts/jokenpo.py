import random

possibility = ["rock", "paper", "scissor"]
play = random.choice(possibility)

played = int(input("1 for rock, 2 for paper, 3 for scissor: "))
player = possibility[played - 1]

print("computer played {}".format(play))

if play == "rock":
    if player == "rock":
        print("draw")
    if player == "paper":
        print("player won")
    if player == "scissor":
        print("computer won")


if play == "scissor":
    if player == "rock":
        print("player won")
    if player == "paper":
        print("computer won")
    if player == "scissor":
        print("draw")


if play == "paper":
    if player == "rock":
        print("computer won")
    if player == "paper":
        print("draw")
    if player == "scissor":
        print("player won")