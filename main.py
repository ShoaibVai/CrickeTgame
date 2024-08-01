import random
import os

def crik(bowler, batter):
    if bowler == batter:
        return -1
    elif 1 <= batter <= 6:
        return batter
    else:
        return 0

def printToss(comToss):
    if comToss == 1:
        print("Coin Landed on HEAD!!!\n")
    if comToss == 2:
        print("Coin Landed on TAIL!!!\n")

def BowlingWtarget(wicket, over, target):
    score = 0
    wicketCount = 0
    
    for ball in range(over * 6):
        if score > target:
            break
        comBat = random.randint(1, 6)
        plyrBall = int(input(f"Ball {ball + 1} Total Run {score}\nYou Choose for Bowling: "))
        print(f"Computer Used {comBat}")
        if crik(plyrBall, comBat) == -1:
            wicketCount += 1
            if wicketCount == wicket:
                print("ALL OUT!!!!!!!")
                break
        elif 1 <= crik(plyrBall, comBat) <= 6:
            score += crik(plyrBall, comBat)
        else:
            print("FOUL INPUT")
    return score

def Bowling(wicket, over):
    score = 0
    wicketCount = 0
    
    for ball in range(over * 6):
        comBat = random.randint(1, 6)
        plyrBall = int(input(f"Ball {ball + 1} Total Run {score}\nYou Choose for Bowling: "))
        print(f"Computer Used {comBat}")
        if crik(plyrBall, comBat) == -1:
            wicketCount += 1
            if wicketCount == wicket:
                print("ALL OUT!!!!!!!")
                break
        elif 1 <= crik(plyrBall, comBat) <= 6:
            score += crik(plyrBall, comBat)
        else:
            print("FOUL INPUT")
    return score

def BattingWtarget(wicket, over, target):
    score = 0
    wicketCount = 0
    for ball in range(over * 6):
        if score > target:
            break
        comBall = random.randint(1, 6)
        plyrBat = int(input(f"Ball {ball + 1} Total Run {score}\nYou Choose for Batting: "))
        print(f"Computer Used {comBall}")
        if crik(comBall, plyrBat) == -1:
            wicketCount += 1
            if wicketCount == wicket:
                print("ALL OUT!!!")
                break
        elif 1 <= crik(comBall, plyrBat) <= 6:
            score += crik(comBall, plyrBat)
        else:
            print("FOUL INPUT")
    return score

def Batting(wicket, over):
    score = 0
    wicketCount = 0
    for ball in range(over * 6):
        comBall = random.randint(1, 6)
        plyrBat = int(input(f"Ball {ball + 1} Total Run {score}\nYou Choose for Batting: "))
        print(f"Computer Used {comBall}")
        if crik(comBall, plyrBat) == -1:
            wicketCount += 1
            if wicketCount == wicket:
                print("ALL OUT!!!")
                break
        elif 1 <= crik(comBall, plyrBat) <= 6:
            score += crik(comBall, plyrBat)
        else:
            print("FOUL INPUT")
    return score

def play():
    over = int(input("How many over(s) do you want to play?:\n"))
    wicket = int(input("How many wicket(s) do you want to play?:\n"))
    comToss = random.randint(1, 2)
    toss = int(input("1. HEAD! or 2.TAIL!!\n"))
    if toss == comToss:
        # player Won the toss
        printToss(comToss)
        tossChoice = int(input("You Won The toss!!!\n1. Bowling or 2. Batting\n"))
        if tossChoice == 1:  # player chose to bowl
            bowlingResult = Bowling(wicket, over)
            print(f"!!!   Player Needs {bowlingResult + 1} Run(s) to win  !!!")
            input("Press \"Enter\" to continue")
            os.system("cls" if os.name == "nt" else "clear")
            print(f"!!!   Player Needs {bowlingResult + 1} Run(s) to win  !!!")
            battingResult = BattingWtarget(wicket, over, bowlingResult)
            if bowlingResult < battingResult:
                print("YOU LOST THE MATCH!")
            elif bowlingResult > battingResult:
                print("YOU WON THE MATCH!!!!!!!!!!!!!")
        elif tossChoice == 2:  # player chose to bat
            battingResult = Batting(wicket, over)
            print(f"!!!   Computer Needs {battingResult + 1} Run(s) to win  !!!")
            input("Press \"Enter\" to continue")
            os.system("cls" if os.name == "nt" else "clear")
            print(f"!!!   Computer Needs {battingResult + 1} Run(s) to win  !!!")
            bowlingResult = BowlingWtarget(wicket, over, battingResult)
            if battingResult > bowlingResult:
                print("YOU WON THE MATCH!!!!!!!!!!!!!")
            elif bowlingResult > battingResult:
                print("YOU LOST THE MATCH!")
        else:
            print("INVALID INPUT")
    # if computer wins the toss        
    else:
        printToss(comToss)
        print("You lost the Toss")
        comChoice = random.randint(1, 2)
        if comChoice == 1:
            print("Computer Chose to Bowl")
        elif comChoice == 2:
            print("Computer Chose to Bat")

        if comChoice == 1:
            battingResult = Batting(wicket, over)
            print(f"!!!   Computer Needs {battingResult + 1} Run(s) to win  !!!")
            input("Press \"Enter\" to continue")
            os.system("cls" if os.name == "nt" else "clear")
            print(f"!!!   Computer Needs {battingResult + 1} Run(s) to win  !!!")
            bowlingResult = BowlingWtarget(wicket, over, battingResult)
            if battingResult > bowlingResult:
                print("YOU WON THE MATCH!!!!!!!!!!!!!")
            elif bowlingResult > battingResult:
                print("YOU LOST THE MATCH!")
        elif comChoice == 2:
            bowlingResult = Bowling(wicket, over)
            print(f"!!!   Player Needs {bowlingResult + 1} Run(s) to win  !!!")
            input("Press \"Enter\" to continue")
            os.system("cls" if os.name == "nt" else "clear")
            print(f"!!!   Player Needs {bowlingResult + 1} Run(s) to win  !!!")
            battingResult = BattingWtarget(wicket, over, bowlingResult)
            if bowlingResult < battingResult:
                print("YOU LOST THE MATCH!")
            elif bowlingResult > battingResult:
                print("YOU WON THE MATCH!!!!!!!!!!!!!")
        else:
            print("INVALID INPUT")
    r = input("Press \"Enter\" to continue or 'R' to Replay the Game")
    if r.lower() == "r":
        play()

play()