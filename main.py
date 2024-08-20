import random
import os

HEAD = 1
TAIL = 2
BOWLING = 1
BATTING = 2

def crik(bowler, batter):
    if bowler == batter:
        return -1
    elif 1 <= batter <= 6:
        return batter
    else:
        return 0

def printToss(comToss):
    if comToss == HEAD:
        print("Coin Landed on HEAD!!!\n")
    elif comToss == TAIL:
        print("Coin Landed on TAIL!!!\n")

def play_innings(role, wicket, over, target=None):
    score = 0
    wicket_count = 0
    for ball in range((over * 6)+1):
        if target and score > target:
            break
        comp_choice = random.randint(1, 6)
        try:
            user_choice = int(input(f"Ball {ball} Total Run {score} Wicket {wicket_count}\nYou Choose for {'Bowling' if role == BOWLING else 'Batting'}: "))
        except ValueError:
            print("Invalid input, please enter a number between 1 and 6.")
            continue
        print(f"Computer Used {comp_choice}")
        result = crik(user_choice, comp_choice) if role == BOWLING else crik(comp_choice, user_choice)
        if result == -1:
            wicket_count += 1
            if wicket_count == wicket:
                print("ALL OUT!!!!!!!")
                break
        elif 1 <= result <= 6:
            score += result
        else:
            print("FOUL INPUT")
    return score

def main():
    try:
        over = int(input("How many over(s) do you want to play?:\n"))
        wicket = int(input("How many wicket(s) do you want to play?:\n"))
    except ValueError:
        print("Invalid input, please enter a valid number.")
        return

    comToss = random.randint(1, 2)
    try:
        toss = int(input("1. HEAD! or 2.TAIL!!\n"))
    except ValueError:
        print("Invalid input, please enter 1 or 2.")
        return

    if toss == comToss:
        printToss(comToss)
        try:
            tossChoice = int(input("You Won The toss!!!\n1. Bowling or 2. Batting\n"))
        except ValueError:
            print("Invalid input, please enter 1 or 2.")
            return

        if tossChoice == BOWLING:
            target = play_innings(BOWLING, wicket, over)
            print(f"!!!   Player Needs {target + 1} Run(s) to win  !!!")
            input("Press \"Enter\" to continue")
            os.system("cls" if os.name == "nt" else "clear")
            print(f"!!!   Player Needs {target + 1} Run(s) to win  !!!")
            score = play_innings(BATTING, wicket, over, target)
            if score > target:
                print("YOU WON THE MATCH!!!!!!!!!!!!!")
            else:
                print("YOU LOST THE MATCH!")
        elif tossChoice == BATTING:
            score = play_innings(BATTING, wicket, over)
            print(f"!!!   Computer Needs {score + 1} Run(s) to win  !!!")
            input("Press \"Enter\" to continue")
            os.system("cls" if os.name == "nt" else "clear")
            print(f"!!!   Computer Needs {score + 1} Run(s) to win  !!!")
            target = play_innings(BOWLING, wicket, over, score)
            if target < score:
                print("YOU WON THE MATCH!!!!!!!!!!!!!")
            else:
                print("YOU LOST THE MATCH!")
        else:
            print("INVALID INPUT")
    else:
        printToss(comToss)
        print("You lost the Toss")
        comChoice = random.randint(1, 2)
        if comChoice == BOWLING:
            print("Computer Chose to Bowl")
            score = play_innings(BATTING, wicket, over)
            print(f"!!!   Computer Needs {score + 1} Run(s) to win  !!!")
            input("Press \"Enter\" to continue")
            os.system("cls" if os.name == "nt" else "clear")
            print(f"!!!   Computer Needs {score + 1} Run(s) to win  !!!")
            target = play_innings(BOWLING, wicket, over, score)
            if target < score:
                print("YOU WON THE MATCH!!!!!!!!!!!!!")
            else:
                print("YOU LOST THE MATCH!")
        elif comChoice == BATTING:
            print("Computer Chose to Bat")
            target = play_innings(BOWLING, wicket, over)
            print(f"!!!   Player Needs {target + 1} Run(s) to win  !!!")
            input("Press \"Enter\" to continue")
            os.system("cls" if os.name == "nt" else "clear")
            print(f"!!!   Player Needs {target + 1} Run(s) to win  !!!")
            score = play_innings(BATTING, wicket, over, target)
            if score > target:
                print("YOU WON THE MATCH!!!!!!!!!!!!!")
            else:
                print("YOU LOST THE MATCH!")
        else:
            print("INVALID INPUT")
    r = input("Press \"Enter\" to continue or 'R' to Replay the Game\n")
    if r.lower() == "r":
        main()

if __name__ == "__main__":
    main()
