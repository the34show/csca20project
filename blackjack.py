import random
import pygame
#ever since adding this it takes so long to initate the funciton
from pygame import mixer
import matplotlib.pyplot as plt 
import time
icon_to_score={"cherry":1,7:3,"coin":2}
# create a list for icons and their values



def game_start():
    """
    """
    play_music()
    print("Welcome to the casino traveller(s)?")
    number_of_players()
    game_choice()

current_game=""
cont_play=""    
players_to_money={}
def number_of_players():
    global players_to_money
    player_answer= input("How many playas are with you? ")
    start_value=input("What is the starting value (money)? ")
    for i in range(int(player_answer)):
        players_to_money["player "+str(i+1)]=start_value
    print (players_to_money)
    
    # create the dictionary of players_to_money
    # ask for # of players
    # ask for start value for all players in players_to_money
    # create the dicitonary?


def game_choice():
    """
    >>>game_choice()
    
    This function asks what game?, the answer is current_game, if current_game is previously selected
    """    
    global current_game
    # ask for game and select the relevant game
    # if conndition
    # insert do while to prevent breaking
    while current_game != "slots" and current_game != "blackjack" and current_game !="Hong Kong" and current_game!="2048":
        # this validates the input and continues to ask it until they enter the right thing, a game may be selected already in which case it 
        #enters that it exits the while and goes to that if
        current_game=input("What game nerd? (slots or blackjack or 2048) ")
    if current_game == "slots":
        print("Spin to win baybee!")
        #most of the prints are just flavor text
        slots()
        #plays the slots game
    elif current_game == "blackjack":
        print("Excellent choice, welcome to jump street")
        blackjack()
        # this needs to be linked ot blackjack
    elif current_game == "Hong Kong":
        print ("Free Hong Kong the revolution of our times! Five demands not one!")
        #this is just an easter egg
    elif current_game == "2048":
        print ("Quick maffs")
        game_2048()
        #this is just an easter egg    
        


def game_continue():
    """
    Ask if the player will continue(yes) in which case it will run the same game, exit (no) in which case it will end the whole game
    or play a new game (different game/player) in which case it will return the player to game_choice.
    """
    #this runs after each game
    global cont_play
    global current_game
    #this makes sure the current_game enters this function
    
    cont_play=""
    cont_play=input("Hey nerd, do you want to keep playing? (yes, no or different game/player) ")
    while cont_play!= "yes" and cont_play!= "no" and cont_play!= "different game/player":
        # this validates the input and continues to ask it until they enter the right thing
        cont_play=input("Hey nerd, say something useful (yes, no or different game/player) " )
    if cont_play== "yes":
        game_choice()
        #if they say yes it lets them go back to game choice
    elif cont_play== "different game/player":
        print("ok, lets lose money another way")
        current_game=""
        game_choice()
        # if they say no it goes back to game choice, but it sets the current_game as blank
    else:
        print ("Goodbye travellars, see ya later")
        
"""
slots
"""

def slots():
    """
    """
    slot_list=["?","?","?"]
    #starts as an "empty" the defulats being a mystery?
    global cont_play
    #this is to see if the current player is the same or do we need to get a new player
    global curr_player
    if cont_play != "yes":
        curr_player = input("Who is playing?")
    bet = input("How much do you want to bet traveller? ")
    # have random text subject response
    #create a do while to ensure that this works
    ### everything above this is set up, below is the actual slots mechanics###
    print (slot_list, flush=True)
    #prints the first mystery list, flush is so that it doesnt buffer  the output and remove my pauses
    time.sleep(2)
    #pauses for two seconds
    for i in range(3):
        #changes each value in the slot list (3)
        value, score = random.choice(list(icon_to_score.items()))
        #random selection
        slot_list[i]=value
        #updates the value
        print (slot_list, flush=True)
        time.sleep(2)
        #prints it with the lag
    if slot_list[0]== slot_list[1] and slot_list[2]== slot_list[1]:
        #if same print winner
        print("Winner Winner Chicken Dinner")
        value_change(curr_player,(score*int(bet)))
        #update winnings using value_change see below
    else:
        print("Loser Loser Loser Loser")
        value_change(curr_player,-(score*int(bet)))
        #update loss
    game_continue()
  
    
def value_change(player,value):
    """
    this function takes player and value inputs and changes it inside player
    value_change("player 1",50)
    """
    global players_to_money
    #brings the player_to_money dictionary into this function
    diff= int(players_to_money.get(player))+int(value)
    #creates diff, a temp value to store the winnigns plus current money
    print(diff)
    players_to_money[player]=diff
    #sets the players value in the dicitonary to diff
    print(players_to_money)


""" is it worth building a validator? or can we assume inputs """
def validator_type(test, test_type):
    # generic validator but how to link it?
    return type(test)==test_type
def validator(test, list_of_possible):
    """
    Takes test inputs and list of possiblities and returns bool
    validator(1, [1,2,3])
    True
    """
    return test in list_of_possible
def testing_validator():
    #testing implementation
    test=0
    while not(validator(test, ["1","2","3"])):
        test=input("Input number in list ")
        

 


    
def play_music():
    """
    plays music using pygame
    """
    
    mixer.init()
    #intialize music
    #plays the music
    mixer.music.load(r"C:\Users\Albert\Documents\fourth year uoft\CSCA20\theme music.mp3")
    #prefixing with r fixes the unicode error, foudn on stack overflow
    pygame.mixer.music.play(loops=-1)
    #repeats the song 
    mixer.music.play()

"""
Black jack
"""
# Create the dictionary for 52 cards and their values  card_to_values
card_to_values= {'A of Diamonds': 1, '2 of Diamonds': 2, '3 of Diamonds': 3, '4 of Diamonds': 4, '5 of Diamonds': 5, '6 of Diamonds': 6, '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9, '10 of Diamonds': 10, 'A of Hearts': 1, '2 of Hearts': 2, '3 of Hearts': 3, '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6, '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9, '10 of Hearts': 10, 'A of Clubs': 1, '2 of Clubs': 2, '3 of Clubs': 3, '4 of Clubs': 4, '5 of Clubs': 5, '6 of Clubs': 6, '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs': 9, '10 of Clubs': 10, 'A of Spades': 1, '2 of Spades': 2, '3 of Spades': 3, '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6, '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9, '10 of Spades': 10, 'Jack of Diamonds': 10, 'Queen of Diamonds': 10, 'King of Diamonds': 10,'Jack of Hearts': 10,'Queen of Hearts': 10,'King of Hearts': 10,'Jack of Clubs': 10,'Queen of Clubs': 10,'King of Clubs': 10,'Jack of Spades': 10,'Queen of Spades': 10,'King of Spades': 10}

max_value = 0
winner=[]
#player=[value(start at 0),cards,cards]
#make the dict player_to_player_hand
player_to_player_hand = {}
player_to_bet= {}

    
#for turn amount of players()
    #draw first
    #enter stage 2
    #black_jack
    
def blackjack():
    for key in players_to_money:
        player_to_player_hand [key] = [0]
        player_to_bet [key] = 0
    for player in player_to_player_hand.keys():
        draw(player)
        betting(player)
    score_all()
    #print everyone's hand
    for player in player_to_player_hand.keys():
        hit_or_stand(player)
    for player in winner:
        # change value to 2
        winnings= player_to_bet.get(player)
        winnings= -(winnings*2)
        #times two to positive
        player_to_bet[player]=winnings
    for player, bet in player_to_bet.items():
        value_change(player,bet)
    game_continue()

#draw(player)
def draw(player):
    global stand
#draw a card by assinging key to player_hand list inside player_to_player_hand
    player_hand = player_to_player_hand.get(player)
    card, value = random.choice(list(card_to_values.items()))
    # randomly assign key,value from the dicitonary to player_hand 
    player_hand[0] += value 
    player_hand.append(card)
    # remove key,value pair from dicitonary
    del card_to_values[card]
    
    
    
    #add values of key to player_hand[0]
        #player_hand[0] += value 
        #append key to player_hand
    #bet  everytime


#stage2- hit or stand
def hit_or_stand(player):
    """
    REQ: answer= hit or stand
    """
#ask for input hit/stand
    answer = input("Would "+ player + " like to hit or stand? ")
    #if hit draw
    player_hand = player_to_player_hand.get(player)
    #if player_hand[0]<=21:
    while player_hand[0]<=21 and answer!= "stand":
        if answer == "hit":        
            draw(player)
            score_all() 
            if player_hand[0]<=21:
                answer = input("Would "+ player + " like to hit or stand? ")
            else:
                answer="stand"
        else:    
            score_all()
            max_val(player)

        

 
#elif stand
def score_all():
    for key, value in player_to_player_hand.items():
        print(key, "->", value)



    
#define win
def max_val(player):
    global max_value
    global winner
    player_hand = player_to_player_hand.get(player)
    #gets the hand
    if max_value< player_hand[0] and player_hand[0] < 22:
        max_value= player_hand[0]
        # goes into the betting dicitonary
        winner=[player]
    elif max_value== player_hand[0] and player_hand[0] < 22:
        winner.append(player)

def betting(player):
    """
    REQ: new_bet must be integer
    """
    # grab key of player
    old_bet = player_to_bet.get(player)
    new_bet= -(int(input("How much would you like to bet "+ player+ "? ")))
    player_to_bet[player]= (new_bet-old_bet)
    # add the bet to the value
    # create a dictionary
    # ask if they want to bet

#bet
#winner=value*2
#loser=-value
#loop thru all players
  #value_change(player,value)
  #game_continue()
  
"""
2048
"""

import matplotlib.pyplot as plt
directions= ["up","right","down","left","stop","graph"]
#board=[[1024,1024,0,0],[1024,0,0,0],[1024,0,0,0],[0,0,0,0]]
#win set
board=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#base set
#board=[[16,8,4,2],[16,8,4,2],[2,2,2,2],[2,2,2,0]]
#testing board
#board=[[192,7,3,1],[19,15,13,11],[24,37,29,15],[6,30,32,0]]
#one step board
score=0
graph_score=[0]
num_turns=[]
error_counter=0
#counts the amount of errors, unique to direction
error_set=set()
winner_2048=0
# i want to createa set(), {} gives a dict
"""
I can detect errors for direction, now how to influence player to move in useful directions
if 
"""

def game_2048():
    global cont_play
    #this is to see if the current player is the same or do we need to get a new player
    global curr_player
    if cont_play!="yes":
        curr_player=input("Who is playing? ")
    bet= input("How much do you want to bet traveller? ") 
    #above is taken from slots
    direction=""
    turn=0
    movement=""
    add_number()
    printer()
    while movement!= "stop":
        #stops the game
        movement= ask_for_movement()
        #asks for input of movement
        if movement=="graph":
            graph()
        if movement!= 'stop' and movement !="graph":
            generic_mover(movement)
            #first alignment
            generic_adder(movement)
            #adds any values
            generic_mover(movement)
            #realigns them in that direction again
            
            if error_counter==12:
                #error_counter coutns the number of errors, if 12 that means no space
                error_set.add(movement)
                #appends it to a list of dis-allowed movements
                print(movement +" is not a valid direction")
            else:
                add_number()
                error_set=set()
                #this will reset the error set  once a valid move has been made
                 
            if error_set== {"up","right","down","left"}:
                 # if all directions are in teh error set, ya lose
                movement="stop"
            # if this all the squares are filled in then don't add a number
            graph_score.append(score)
            turn+=1
            num_turns.append(turn)
             #number spawn
             #check if they lose
        
        printer()
         #print current board
    graph()
    print("Thanks for playing!")
    if winner_2048==1:
        value_change(curr_player, (bet*2))
    game_continue()
     
     
     

def ask_for_movement():
     #asks for input of movement and forces it to be a relevant direction
    movement=""
    while not (movement in directions):
        movement= input("Which direction? ")
    return movement

def add_number():
    global board
    #generates a number in the board
    new_num= random.randint(1, 2)*2
    #random number
    row=random.randint(0, 3)
    column=random.randint(0, 3)
    #the row and column start as random integers between 0-3
    while board[row][column]!=0:     
        row=random.randint(0, 3)
        column=random.randint(0, 3)
        first=1
    #print(row,column)
    board[row][column]=new_num
     # puts it in the board

"""
directions and additions
"""
def generic_mover(direction):
    """
    (str)->(none)
    >>>generic_adder("left") 
    
    """
    global error_counter
    for iteration in range(3):
        error_counter=0
        #repeats the whole block three times, it works if there is a back to back char i.e. 0,2,2,0 going right, the first iteration
        #0,2,0,2 the first two can't move because there is the second two blocking it, 3 times for each of the possible filled squares
        for row in range(len(board)):
            for column in range(len(board)):
                 # creates two indexes, one that indexes the row and one that indexes the column, by nesting one it allows for 
                 # the function to run through every possible cell, row,column: 0,0 0,1 0,2 0,3 1,0 1,1 etc.
                if direction== "left":
                    mover= column+1
                    indexers=[row,mover]
                elif direction== "right":
                    mover= column-1
                    indexers=[row,mover]
                elif direction== "up":
                    mover= row+1
                    indexers=[mover,column]
                elif direction== "down":
                    mover= row-1
                    indexers=[mover,column]
                 # this block sets the mover, either to the next column, previous column etc. 
                 # mover is then added to a list called indexers depending on which value of row,column mover affects
                 #side note this is not inverted b/c i don't care about which line to start moving from but i do from where it adds
                if mover>-1 and mover<4:
                     #the mover only runs on cells that are within the matrix, 12 possible iterations
                    if board[indexers[0]][indexers[1]]!=0 and board[row][column]==0:
                        #mover cell has a value and #the current cell is empty to move it over
                        board[row][column]= board[indexers[0]][indexers[1]]
                        #mover cell goes to the current cell
                        board[indexers[0]][indexers[1]]=0
                        #removes the value of the mover cell
                    if board[indexers[0]][indexers[1]]!=0:
                        error_counter+=1
                            # the error_counter should increase by 1 everytime a cell is filled, if all 12 possible movers are filled 
                             # that direction should not be allowed to move, see main_game for the if command that stops the program

  

####
#Adds are added below
####
def generic_adder(direction):
    """
    (str)->(none)
    >>>generic_adder("left")
    
    """
    global winner_2048
    global score
    #global score to update the score
    for iteration in range(1):
         #i dont think i need this line.....
        fail_counter=0
        for row in range(len(board)):
            for column in range(len(board)):
                 # goes thru each cell of the matrix for 0,0 0,1.....
                if direction== "left":
                    mover= column+1
                    indexers=[row,mover]
                elif direction== "right":
                    column= 3-column
                    # this inverts my counter starting at the right most column (3) instead of (0) to add prevents my 
                    #2,2,2 =>0,4,2 error becomes =>0,2,4
                    mover= column-1
                    indexers=[row,mover]
                elif direction== "up":
                    mover= row+1
                    indexers=[mover,column]
                elif direction== "down":
                    row= 3-row
                    #this inverst
                    mover= row-1
                    indexers=[mover,column]
                # this block sets the mover, either to the next column, previous column etc. 
                # mover is then added to a list called indexers depending on which value of row,column mover affects
                if mover>-1 and mover<4:
                     #othe mover only runs on cells that are within the matrix   
                     #if down or left/right(find out which) then switch direction of calculating
                    if direction== "down" or direction =="right":
                         #down and right
                        if board[indexers[0]][indexers[1]]!=0 and board[indexers[0]][indexers[1]]== board[row][column]:
                             #the current celler has a value
                             #the mover cell and current cell are the same
                            if (board[row][column] *2)== 2048 and winner_2048 !=1:
                                winner_2048=1
                                print("Congratulaitons you win! Type stop if you would like end the game!")                           
                            board[indexers[0]][indexers[1]]= board[row][column] * 2
                            #mover cell goes to the current cell
                            score=score+ board[row][column]
                            board[row][column]=0       
                        else:
                            fail_counter+=1
                              #print(fail_counter)                                   
                    else:
                         #left and up basically
                        if board[row][column]==board[indexers[0]][indexers[1]] and board[row][column]!=0:
                             #the mover cell and current cell are the same
                             #the current celler has a value                                
                            board[row][column]= board[indexers[0]][indexers[1]] * 2
                            if (board[indexers[0]][indexers[1]]* 2) == 2048 and winner_2048!=1:
                                winner_2048=1
                                print("Congratulaitons you win! Type stop if you would like end the game!")                          
                            #mover cell goes to the current cell
                            score=score+ board[indexers[0]][indexers[1]]
                            board[indexers[0]][indexers[1]]=0
                             #removes the value of the mover cell
                        else:
                            fail_counter+=1
                            #print(fail_counter)
                                  

                 


def printer():
    global score
    #updates the score
    print(board[0])
    print(board[1])     
    print(board[2])
    print(board[3])
    #prints the board line by line
    print ("score:" +str(score))  
    #pritns the final score

 
def graph():
    y1=graph_score
    plt.plot(y1, label = "line 1")
    plt.xlabel('time') 
     # naming the y axis 
    plt.ylabel('score') 
     # giving a title to my graph 
    plt.title("Score Over Time")        
    # function to show the plot 
    plt.show()