import random
import time
import emoji
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a","--action",help="What to do with numbers",default="easy")
args = parser.parse_args()


def easy(a,b):
    print(a+b)

def hard(a,b):
    print(a-b)

if args.action == "easy":
    pass
elif args.action == "hard":
    pass
else:
    print("Nothing")


rock = emoji.emojize(":rock:")
paper = emoji.emojize(":page_facing_up:")
scissors = emoji.emojize(":scissors:")
lizard = emoji.emojize(":lizard:")
spock = emoji.emojize(":vulcan_salute:")

items = {1: "rock", 2: "paper", 3: "scissors", 4: "lizard", 5: "spock"}
emoji_items = {1: rock, 2: paper, 3: scissors, 4: lizard, 5: spock}
i = 0


def is_win(user_item,bot_item):
    """
    Analyze bot item and user item. Define the winner.

    This function compare two items: which has been chosen by CPU
    and which was chosen by user. Thus, the winner is defined.

    Parameters
    ----------------
    user_item : int
        The item, chosen by user.
    bot_item : int
        The item, chosen by CPU.

    Returns
    ----------------
    bool
        True or false, depending on the results of comparing the items.
    """
    if (user_item == 1 and bot_item in (3, 4)) or (user_item == 2 and bot_item in (1, 5)) or \
            (user_item == 3 and bot_item in (2, 4)) or (user_item == 4 and bot_item in (2, 5)) \
            or (user_item == 5 and bot_item in (1, 3)):
        return True
    return False


def win_mes(user_item,bot_item,mode="CPU"):
    """
    Print result message depending on a mode of game.

    This function print a message, which contains results of the game, to console.

    Parameters
    ----------------
    user_item : int
        The item, chosen by user.
    bot_item : int
        The item, chosen by CPU.
    mode : string
        Type of game (with computer or with another player)
    Returns
    ----------------
    string
        String message - results of the game.
    """
    if mode == "CPU":
        if is_win(user_item,bot_item):
            return "You WIN!"
        else:
            return "You LOSE!"
    elif mode == "Player":
        if is_win(user_item,bot_item):
            return "WIN of Player 1"
        else:
            return "WIN of Player 2"


def lose():
    """
    Return lose message.
    """
    return "YOU LOSE!"


def choise():
    """
    A process-function, which gets from user mode of the game
    (vs CPU or vs user).
    """
    global i
    if i == 0:
        print("1 - vs CPU\n2 - vs Player")
        i = int(input())
        while i != 1 and i != 2:
            print(f"Wrong, try again:")
            i = int(input())


def bot(user_item,bot_item):
    """
    Notifies the user about the progress of the game.

    This function notifies the user about the progress of the game
    (what was chosen by user, what was chosen by CPU, who wins etc.).

    Parameters
    ----------------
    user_item : int
        The item, chosen by user.
    bot_item : int
        The item, chosen by CPU.
    """
    print("\nYou chose " + items[user_item])
    time.sleep(1)

    print("Computer chose " + items[bot_item] + "\n")
    time.sleep(0.5)
    game_core(bot_item, user_item)


def player(user_item,bot_item):
    """
    Notifies the user about the progress of the game.

    This function notifies the user about the progress of the game
    (what was chosen by first user, what was chosen by second user,
     who wins etc.).

    Parameters
    ----------------
    user_item : int
        The item, chosen by first player.
    bot_item : int
        The item, chosen by second player.
    """
    print("\nPlayer 1 " + items[user_item])
    time.sleep(0.5)

    print("Player 2 " + items[bot_item] + "\n")
    time.sleep(0.5)
    game_core(bot_item, user_item)


def game_core(bot_item, user_item):
    """
    Core function that displays game process, who win etc.

    This function shows the user the progress of the game,
    notify who won, or maybe it is a tie.

    Parameters
    ----------------
    user_item : int
        The item, chosen by first player.
    bot_item : int
        The item, chosen by second player.
    """
    print(emoji_items[user_item] + "\t" + emoji.emojize(":right_arrow:") + "\t" + emoji_items[bot_item])

    if user_item == bot_item:
        print("TIE! MOVE TO NEXT ROUND!")
        game()

    if i == 2:
        print(win_mes(user_item,bot_item,mode="Player"))
    else:
        print(win_mes(user_item, bot_item))

def selection(res:str,number:int):
    user_item = 0
    while user_item > number or user_item <= 0:
        user_item = int(input(res + "\n\tYour item: "))

    if i == 2:
        a = "\n" * 15
        print(f"{a}" + "Do not scroll up :)\n")
        bot_item = 0
        while bot_item > number or bot_item <= 0:
            bot_item = int(input(res + "\n\tYour item: "))
        player(user_item, bot_item)
    else:
        bot_item = random.randint(1, number)
        bot(user_item, bot_item)

def game():
    """
    Main function that processes whole the game.

    This function processes user inputs
    (game mode, new game, game process).
    """
    choise()

    res = ""
    number = 0
    if args.action == "easy":
        number = 3
        for a in range(3):
           print(f'\t{a+1} - {items[a+1]}. {items[a+1].title()} {emoji_items[a+1]}')

    elif args.action == "hard":
        number = 5
        res = '\n'.join(map(lambda item: f'\t{item[0]}. {item[1].title()} {emoji_items[item[0]]}', items.items()))
    selection(res,number)

    print("==============================================================================")
    if input("Do you want to start a new game? (y) ").lower() == "y":
        game()
    else:
        print("Awesome game! See you...")
        exit(0)


if __name__ == "__main__":
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
