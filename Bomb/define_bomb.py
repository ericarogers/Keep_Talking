'''Define bomb'''

'''
Import functions from useful_funct
Import module_options for user to choose
'''

from Bomb import useful_funct

from Bomb import module_options

# Set definitions from useful_funct
get_Bool = useful_funct.get_Bool
get_NumRange = useful_funct.get_NumRange

# Set definitions from module_options
Module = module_options.Bomb.Module
Bomb = module_options.Bomb


'''Set up core bomb elements'''

print("\n- The last number of the serial number is even -")
SerialEven = get_Bool("True or False? ")

print("\n- There is a vowel in the serial number -")
SerialVowel = get_Bool("True or False? ")

print("\n- How many batteries are there on the bomb? -")
BombBatteries = get_NumRange("Batteries: ", 0, 7)

print("\n- There is a parallel port on the bomb -")
ParallelPort = get_Bool("True or False? ")

# Send up bomb from user input & send to choose module options
Bomb.Module(SE=SerialEven, SV=SerialVowel, BB=BombBatteries, PP=ParallelPort)

