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
     return "YOU WIN!"

def lose():
     return "YOU LOSE!"


def game_core(bot_item, user_item):
    print(emoji_items[user_item] + "\t" + emoji.emojize(":right_arrow:") + "\t" + emoji_items[bot_item])

    if user_item == bot_item:
        print("TIE! MOVE TO NEXT ROUND!")
        game()

    if (user_item == 1 and bot_item in (3, 4)) or (user_item == 2 and bot_item in (1, 5)) or \
            (user_item == 3 and bot_item in (2, 4)) or (user_item == 4 and bot_item in (2, 5))\
            or (user_item == 5 and bot_item in (1, 3)):
        print(win())
    else:
        print(lose())


def game():
    bot_item = random.randint(1, len(items.keys()))
    res = '\n'.join(map(lambda item: f'\t{item[0]}. {item[1].title()} {emoji_items[item[0]]}', items.items()))
    user_item = 0
    while user_item > len(items.keys()) or user_item <= 0:
        user_item = int(input(res + "\n\tYour item: "))

    print("\nYou chose " + items[user_item])
    time.sleep(1)
    print("Computer chose " + items[bot_item] + "\n")
    time.sleep(0.5)
    game_core(bot_item, user_item)

    print("==============================================================================")
    if input("Do you want to start a new game? (y) ").lower() == "y":
        game()
    else:
        print("Awesome game! See you...")
        exit(0)


try:
    with open("Greeting.txt") as file:
        print(file.read())
except:
    pass

start = str(input("Do you want to start the game? (y) "))

if start.lower() == "y":
    game()
else:
    print("\nOK, see you next time...Bye!")

