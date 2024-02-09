import time 
import random
import sys

snakes = {
    17 : 7,
    54 : 34,
    62 : 19,
    64 : 60
}

ladders = {
    2 : 12,
    13 : 78,
    45 : 98
}

MAX = 100
dice_faces = 6

def diceVal():
    return random.randint(1,dice_faces)

def move_user(user,dice_value,current_position):
    final_value = current_position + dice_value
    print(user, "moved from",current_position,"to",final_value)
    
    if final_value in snakes:
        old_position = snakes.get(final_value)
        snake_bited(user, current_position, final_value)
    
    elif final_value in ladders:
        old_position = snakes.get(final_value)
        got_ladder(user, current_position, final_value)
    
    else:
        old_position = final_value
    return old_position
        
        
        
        

def snake_bited(user, current_position, old_position):
    print("Oops!! the snake have bited, the",user,"have moved from",current_position,"to","old position")
    
def got_ladder(user, current_position, old_position):
    print("HURRAY!!, the",user,"have moved from",current_position,"to",old_Prasaposition)
    
    

def start():
    print("Let's start playing SNAKE AND LADDER!!!!")
    user1 = input("Enter name of player1: ")
    user2 = input("Enter the name of player2: ")
    
    position_of_user1 = 0
    position_of_user2 = 0
    
    while (True):
        input(user1 + " Press enter to roll the dice.")
        dice_value = diceVal()
        final_position = move_user(user1, dice_value, position_of_user1)
        position_of_user1 = final_position
        
        input(user2 + " Press enter to roll the dice.")
        dice_value = diceVal()
        final_position = move_user(user1, dice_value, position_of_user2)
        position_of_user1 = final_position
        
        
if __name__ == "__main__":
    start()
    
        