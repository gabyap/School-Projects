# Author: Gaby Pancu
# Date:   2017-06-07

#so that I can exit the program later on
import sys

#the intro() function calls on the game, allows user to play again or quit - called on by main()
def intro():
    choice=input("Press p to play again or q to quit ")

    #error detection
    while (choice!="p" and choice!="q"):
        print("This is not a valid entry\n")
        choice=input("Press p to play again or q to quit ")

    #game starts when p is pressed
    if (choice=="p"):
        game_of_pig()

    #program stops when q is pressed
    print("Thanks for playing!")
    sys.exit()

#the showDice() function prints the dice graphic of the roll value - called on by roll()
def showDice(roll_value):
    #reuse certain lines for ceratin dice Ex. 4 and 5 share the same 1st and 3rd line
    if(roll_value==1 or roll_value==3 or roll_value==5):
        line2="|   o   |"
    else:
        line2="|       |"

    if (roll_value==1):
        line1="|       |"
        line3="|       |"
    elif (roll_value==2 or roll_value==3):
        line1="| o     |"
        line3="|     o |"
    elif (roll_value==4 or roll_value==5):
        line1="| o   o |"
        line3="| o   o |"
    elif (roll_value==6):
        line1="| o o o |"
        line3="| o o o |"

    #print each line of the die individually
    print("+-------+")
    print (line1)
    print (line2)
    print (line3)
    print("+-------+")

#the roll() function allows the current user to roll on their first turn and then roll or hold on the next
#called on by game_of_pig()
def roll(player_total,current_player,win_total):
    
    #print whose turn it is
    if (current_player==1):
        print("\nPlayer 1\n")
    elif (current_player==2):
        print("\nPlayer 2\n")

    #round total begins at 0
    round_total=0

    #you can only roll on the first turn
    choice=input("\nEnter r to roll ")

    #error detection
    while (choice!="r"):
        print("This is not a valid entry\n")
        choice=input("\nEnter r to roll ")

    #keep rolling while they select r
    while (choice=="r"):
        #use random number generator to generate number between 1-6
        from random import randint
        roll_value=randint(1,6)
        #print dice graphic and roll value
        showDice(roll_value)
        print("You rolled a",roll_value)

        if (roll_value!=1):
            #if the roll value is not 1, add it to the round total
            round_total+=roll_value
            print("Your round total is",round_total)
            #if this roll has brought them to the win total, the game ends here, intro runs again
            if (player_total+round_total>=win_total):
                print("Congratulations Player"+str(current_player)+"! You win!")
                intro()
            #if they are not yet at the win total, they can roll again or hold
            else:
                choice=input("\nEnter r to roll or h to hold ")

                #error detection
                while (choice!="r" and choice!="h"):
                    print("This is not a valid entry")
                    choice=input("\nEnter r to roll or h to hold ")
        else:
            #if the roll value is 0, they get no points that round
            round_total=0
            print("Uh oh! You lost all your points from this round!")
            break

    #add round total to player total, print and return player total to game_of_pig()
    player_total+=round_total
    print("Your game total is",player_total)
    return(player_total)

#the function game_of_pig() runs the entire game - called on by main()
def game_of_pig():
    #error detection
    validEntry=False
    while (validEntry==False or win_total<=0):
        try:
            #ask user for what they're playing to, set a variable
            win_total=int(input("\nWhat would you like to play to?\nPlease enter a value > 0: "))
            validEntry=True
        except:
            print("This is not a valid entry")
            validEntry=False

    print("You are playing to",win_total,"points")
    #player totals begin at 0
    #player_total=0
    total1=0
    total2=0

    #Starts with player 1, runs roll(), switches to player 2, runs roll
    #until one of them reaches the win total
    current_player=1
    while (total1<win_total and total2<win_total):
        if current_player==1:
            total1=roll(total1,current_player,win_total)
        elif current_player==2:
            total2=roll(total2,current_player,win_total)
        if current_player==1:
            current_player=2
        else:
            current_player=1

    #game ends when someone reaches game total, runs intro()
    if (choice=="p"):
        print("Congratulations Player"+str(current_player)+"! You win!")
        intro()

#main()

#prints instructions
print("Welcome to Pig! Here's how to play:\n")
print("1. You and a friend take turns rolling a 6-sided dice, playing to reach a certain total (which you will choose).")
print("2. If you roll a value between  2 and 6 it is added to their score, and you can roll again.")
print("3. If you roll a 1 (a 'pig'), you lose your turn and add nothing to your score.")
print("4. At any point after rolling a 2-6, you may choose to to hold, which ends your turn, and adds your turn total to your score.")
print("5. The winner is the first player to get a score greater than or equal to the total.\n")

choice=input("Press p to play ")

#error detection
while (choice!="p"):
    print("This is not a valid entry\n")
    choice=input("Press p to play ")

#once f or c is pressed, game starts
game_of_pig()

"""
code for playing against computer:

def auto_roll(player_total,current_player,win_total):

        #print who's turn it is
        print("\nComputer\n")

        #round total begins at 0
        round_total=0

        while (round_total<10):
            choice='r'
        #keep rolling while they select r
        while (choice=='r'):
            #use random number generator to generate number between 1-6
            from random import randint
            roll_value=randint(1,6)
            #print dice graphic and roll value
            showDice(roll_value)
            print("Computer rolled a",roll_value)

            if (roll_value!=1):
                #if the roll value is not 1, add it to the round total
                round_total+=roll_value
                print("Computer's round total is",round_total)
                #if this roll has brought them to the win total, the game ends here, intro runs again
                if (player_total+round_total>=win_total):
                    print("Sorry! The computer won!")
                    intro()
                #if they are not yet at the win total, they can roll again or hold
                else:
                    while (round_total<10):
                        choice='r'

            else:
                #if the roll value is 0, they get no points that round
                round_total=0
                print("Uh oh! The computer lost all its points from this round!")




        #add round total to player total, print and return player total to game_of_pig()
        player_total+=round_total
        print("Computer's game total is",player_total)
        return(player_total)
"""
