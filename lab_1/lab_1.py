import random
import time
import emoji

rock = emoji.emojize(":rock:")
paper = emoji.emojize(":page_facing_up:")
scissors = emoji.emojize(":scissors:")
lizard = emoji.emojize(":lizard:")
spock = emoji.emojize(":vulcan_salute:")

items = {1: "rock", 2: "paper", 3: "scissors", 4: "lizard", 5: "spock"}
emoji_items = {1: rock, 2: paper, 3: scissors, 4: lizard, 5: spock}


def win():
    print("YOU WIN!")


def lose():
    print(f"YOU LOSE!")


def game_core(bot_item, user_item):
    print(emoji_items[user_item] + "\t" + emoji.emojize(":right_arrow:") + "\t" + emoji_items[bot_item])

    if user_item == bot_item:
        print("TIE! MOVE TO NEXT ROUND!")
        game()

    if user_item == 1:
        if bot_item == 3 or 4:
            win()
        else:
            lose()

    if user_item == 2:
        if bot_item == 1 or 5:
            win()
        else:
            lose()

    if user_item == 3:
        if bot_item == 2 or 4:
            win()
        else:
            lose()

    if user_item == 4:
        if bot_item == 2 or 5:
            win()
        else:
            lose()

    if user_item == 5:
        if bot_item == 1 or 3:
            win()
        else:
            lose()


def game():
    bot_item = random.randint(1, 5)

    user_item = 0
    while user_item > 5 or user_item <= 0:
        user_item = int(
            input("\n\tChoose the item: \n\t\t1. Rock " + rock + "\n\t\t2. Paper " + paper + "\n\t\t3. Scissors " +
                  scissors + "\n\t\t4. Lizard " + lizard + "\n\t\t5. Spock " + spock + "\n\tYour item: "))

    print("\nYou chose " + items[user_item])
    input()
    print("Computer chose " + items[bot_item] + "\n")
    time.sleep(0.5)
    game_core(bot_item, user_item)

    print("==============================================================================")
    if str(input("Do you want to start a new game? (y) ")) == "y":
        game()
    else:
        print("Awesome game! See you...")
        exit(0)


greeting = open("Greeting.txt").read()
print(greeting)

start = str(input("Do you want to start the game? (y) "))

if start == "y":
    game()
else:
    print("\nOK, see you next time...Bye!")