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

def game_core(bot_item, user_item):
    print(emoji_items[user_item] + "\t" + emoji.emojize(":right_arrow:") + "\t" + emoji_items[bot_item])
    if user_item == bot_item:
        print("TIE! MOVE TO NEXT ROUND!")
        game()
    if user_item == 1:
        if bot_item == 2:
            print(f"YOU LOSE!")
        elif bot_item == 3:
            print("WIN!")
        elif bot_item == 4:
            print("WIN!")
        elif bot_item == 5:
            print("LOSE!")
    if user_item == 2:
        if bot_item == 1:
            print("WIN!")
        elif bot_item == 3:
            print("LOSE!")
        elif bot_item == 4:
            print("LOSE!")
        elif bot_item == 5:
            print("WIN!")
    if user_item == 3:
        if bot_item == 1:
            print("LOSE!")
        elif bot_item == 2:
            print("WIN!")
        elif bot_item == 4:
            print("WIN!")
        elif bot_item == 5:
            print("LOSE!")
    if user_item == 4:
        if bot_item == 1:
            print("LOSE!")
        elif bot_item == 2:
            print("WIN!")
        elif bot_item == 3:
            print("LOSE!")
        elif bot_item == 5:
            print("WIN!")
    if user_item == 5:
        if bot_item == 1:
            print("WIN!")
        elif bot_item == 2:
            print("LOSE!")
        elif bot_item == 3:
            print("WIN!")
        elif bot_item == 4:
            print("LOSE!")
