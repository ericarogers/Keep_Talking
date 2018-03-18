'''Keep Talking & Nobody Explodes Solution package'''

# Intro for user
print ("Keep Talking And Nobody Explodes\n")
print ("Solving your bomb so you don't have to.")
print ("\n\n -- Defining your bomb --\n")

'''Define & set up the bomb'''
from Bomb import define_bomb

'''Import useful functions from useful_funct'''
from Bomb import useful_funct

# Boolean function from useful_funct for repeatability
get_Bool = useful_funct.get_Bool


'''Set up definitions from define_bomb'''
Bomb = define_bomb.Bomb
SerialEven = define_bomb.SerialEven
SerialVowel = define_bomb.SerialVowel
BombBatteries = define_bomb.BombBatteries
ParallelPort = define_bomb.ParallelPort

'''Repition of module options'''

while True:  # check if user wants to continue
    NextRound = get_Bool("\n***\n\nBomb complete. True or False: ")
    '''
    if the user would like to continue,
    set up the bomb again from prior inputs & send to modules
    '''
    if NextRound == False:
        print("\n\n***\n")
        Bomb.Module(SE=SerialEven, SV=SerialVowel, BB=BombBatteries, PP=ParallelPort)
    '''
    else, break the loop & end bomb soltion code
    '''
    if NextRound == True:
        print ("\n\nEND")
        break
