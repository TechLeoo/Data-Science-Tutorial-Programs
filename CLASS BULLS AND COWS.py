# Bulls and Cows 
# Bulls are gotten when you get the exact location of the generated number.
# Cows are gotten when you guess a number correctly but not the location correctly.
# JACKPOT - You guess the EXACT NUMBER.
# Jackpot ---> 20points
# Bulls ---> 3points (for each bull)
# Cows ---> 1point (for each cow)

import random
# Data Storage
Player1_Bulls = 0
Player2_Bulls = 0

Player1_Cows = 0
Player2_Cows = 0

Player1_Jackpot = False
Player2_Jackpot = False

Jackpot = 20

GAME_TOTALPOINTS1 = 0
GAME_TOTALPOINTS2 = 0

game_database = {}



# Data Collection
Round = 1

print("Insert your names.")
player1 = input("Player One: ").capitalize().strip()
player2 = input("Player Two: ").capitalize().strip()

print(f"\nOur guess competition between {player1} and {player2} is about to begin. \nWho is going to be our GUESS CHAMPION??? ")
while True:
    game_generated = random.randint(1000, 9999)
    print(f"\n\nR O U N D   {Round}")
    player1_guess = int(input(f"\nGuess a 4 digit number {player1}.\n     RESPONSE: "))
    player2_guess = int(input(f"Guess a 4 digit number {player2}.\n     RESPONSE: "))
    
    # str(player1_guess), str(player2_guess), str(game_generated)
    # CHECK FOR BULLS
    index = 0
    str_player1 = str(player1_guess)
    str_player2 = str(player2_guess)
    str_game = str(game_generated)
    
    while index < len(str_game):
        if str_player1[index] == str_game[index]:
            Player1_Bulls = Player1_Bulls + 1
        if str_player2[index] == str_game[index]:
            Player2_Bulls = Player2_Bulls + 1
        index = index + 1
        
    # CHECK FOR COWS
    value = 0
    while value < len(str_game):
        if (str_player1[value] in str_game) and (str_player1[value] != str_game[value]):
            Player1_Cows = Player1_Cows + 1
        if (str_player2[value] in str_game) and (str_player2[value] != str_game[value]):
            Player2_Cows = Player2_Cows + 1
        value = value + 1
    
    
    # Game Calculation
    player1_totalbulls = Player1_Bulls * 3
    player2_totalbulls = Player2_Bulls * 3
    
    player1_totalcows = Player1_Cows * 1
    player2_totalcows = Player2_Cows * 1
    
    Player1_TotalPoints = player1_totalbulls + player1_totalcows
    Player2_TotalPoints = player2_totalbulls + player2_totalcows
    
    GAME_TOTALPOINTS1 = GAME_TOTALPOINTS1 + Player1_TotalPoints
    GAME_TOTALPOINTS2 = GAME_TOTALPOINTS2 + Player2_TotalPoints
    
    print("\n\n")
    print("Points for each BULL ---> 3 points\nPoints for each COW ---> 3 points")
    print(f"Number Generated: {game_generated}\n")
    print(f"{player1}:\n     BULLS: {Player1_Bulls}     COWS: {Player1_Cows}     TOTAL POINTS: {Player1_TotalPoints}")     
    print(f"{player2}:\n     BULLS: {Player2_Bulls}     COWS: {Player2_Cows}     TOTAL POINTS: {Player2_TotalPoints}")
    
    if player1_guess == game_generated:
        print("\nJACKPOT!!! 🔥🔥🔥")
        print(f"Brilliant Job {player1}. You hit a jackpot of 20 points.")
        Player1_Jackpot = True
        Player1_TotalPoints = Player1_TotalPoints + Jackpot
        
    elif player2_guess == game_generated:
        print("\nJACKPOT!!! 🔥🔥🔥")
        print(f"Brilliant Job {player1}. You hit a jackpot of 20 points.")
        Player2_Jackpot = True
        Player2_TotalPoints = Player2_TotalPoints + Jackpot
    
    game_database[f"Round {Round}"] = {}
    game_database[f"Round {Round}"][player1] = {
                                                "Guess": int(player1_guess),
                                                "Game Generated": int(game_generated),
                                                "Number of Bulls": Player1_Bulls,
                                                "Number of Cows": Player1_Cows,
                                                "Points from Bulls": player1_totalbulls,
                                                "Points from Cows": player1_totalcows,
                                                "Jackpot": Player1_Jackpot,
                                                "Total Points": Player1_TotalPoints,
                                                f"Total Points after Round {Round}": GAME_TOTALPOINTS1
                                                }
    game_database[f"Round {Round}"][player2] = {
                                                "Guess": int(player2_guess),
                                                "Game Generated": int(game_generated),
                                                "Number of Bulls": Player2_Bulls,
                                                "Number of Cows": Player2_Cows,
                                                "Points from Bulls": player2_totalbulls,
                                                "Points from Cows": player2_totalcows,
                                                "Jackpot": Player2_Jackpot,
                                                "Total Points": Player2_TotalPoints,
                                                f"Total Points after Round {Round}": GAME_TOTALPOINTS1
                                                }
    
    while True:
        question = int(input("\nPlay another round? \nPRESS 1: Continue\nPRESS 2: Exit\nRESPONSE: "))
        if question == 1 or question == 2:
            break
        else:
            print("Invalid Response")

    if question == 1:
        Round = Round + 1
    elif question == 2:
        if GAME_TOTALPOINTS1 > GAME_TOTALPOINTS2:
            print(f"{player1} is our guess champion!!! 💥🔥🎉")
        elif GAME_TOTALPOINTS1 < GAME_TOTALPOINTS2:
            print(f"You are our guess champion {player2}. Well done!!! 💥🔥🎉")
        else:
            print("You guys are boring because it is a DRAW.")
        break
    
        
# BUGS DETECTED
# Calculating the bulls after each round. IT IS SUMMING IT UP
# THE TOTAL POINTS IN THE STORE HAD ISSUES.