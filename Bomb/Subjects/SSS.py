'''Subject of Simon Says'''

'''Import & define useful functions'''
from Bomb import useful_funct
get_NumRange = useful_funct.get_NumRange
get_RealCol = useful_funct.get_RealCol
get_Bool = useful_funct.get_Bool
from Bomb import define_bomb
SerialVowel = define_bomb.SerialVowel

# User input for strikes to specify which list necessary
strikes = get_NumRange("Input the current number of strikes: ", 0, 3)

# List of answers for user printed each time
simonsays = []

# Listed colour conversions for user input
NoVowel = {"0": {"Red": "Blue", "Blue": "Red", "Green": "Yellow", "Yellow": "Green"},
           "1": {"Red": "Yellow", "Blue": "Green", "Green": "Blue", "Yellow": "Red"},
           "2": {"Red": "Green", "Blue": "Red", "Green": "Yellow", "Yellow": "Blue"},
           }
Vowel = {"0": {"Red": "Blue", "Blue": "Yellow", "Green": "Green", "Yellow": "Red"},
         "1": {"Red": "Red", "Blue":"Blue", "Green": "Yellow", "Yellow":"Green"},
         "2": {"Red": "Yellow", "Blue": "Green", "Green": "Blue", "Yellow": "Red"},
         }

# Set list to use for colour output depending on if vowel in Serial Number
if SerialVowel is True:
    lst = Vowel
if SerialVowel is False:
    lst = NoVowel

while True:  # Repeat main code functions

    # Input colours for conversion into solution combo
    newcolour = get_RealCol("\nPlease input the first new colour displayed: ", 0, 1, 2, 5)

    for strike in lst:  # for the three options for number of strikes
        if int(strike) == int(strikes):  # for list for the current number of strikes
            # append the new colour in the output combo
            simonsays.append(lst[str(strikes)][newcolour.title()])
            # new list for output created for clearly formatted user output
            ColList = ", ".join(map(str, simonsays))
            print("\n\-- Simon says...", (ColList), " --")
    if len(simonsays) >= 5:  # after five iterations ask user if they want to cont
        Cont = get_Bool("\n***\nContinue? True or False: ")
        if Cont is True:
            pass
        else:
            break
