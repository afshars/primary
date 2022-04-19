# Created by : Sara  Afshar
# Program :  Game Rock , Paper ,Scissors 
# Delivery time : 1400/12/11

print('------------------------------------')

import random as rn

print ('Game Rock , Paper ,Scissors')

while True:
    move =['rock','paper','scissors']
    
    first_player= (input('first_player = ')).lower()


    if  (first_player!='rock') and (first_player!='paper')  and (first_player!='scissors') :
        print('The move is unknown. So , we move for you :)')
        first_player= rn.choice(move)
        print('first_player =' , first_player)
        
    second_player= rn.choice(move)
    
    print('second_player = ' ,second_player )
    
    if first_player == second_player:
        print('first_player equal second_player')
    
    elif first_player == 'rock':
        
        if second_player== 'paper':
            print('second_player is winner')
        elif second_player== 'scissors':
            print('first_player is winner')
            break

    elif first_player == 'paper':
        
        if second_player== 'scissors':
            print('second_player is winner')
        elif second_player== 'rock':
            print('first_player is winner')
            break
            
    elif first_player == 'scissors':
        
        if second_player== 'rock':
            print('second_player is winner')
        elif second_player== 'paper':
            print('first_player is winner')
            break
print('------------------------------------')