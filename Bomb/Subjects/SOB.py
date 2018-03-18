'''Subject of the Button'''

'''Import & define useful functions'''
from Bomb import useful_funct
get_Alpha = useful_funct.get_Alpha
get_RealCol = useful_funct.get_RealCol
from Bomb import define_bomb
BombBatteries = define_bomb.BombBatteries

# User input colour & text of button
colour = get_RealCol("Input colour of button:\n", 0, 1, 2, 3)
text = get_Alpha("Button text:\n")

print(" ")


def hold():
    '''Hold function for when strip colour leads to solution'''
    print("\nHold the button.")

    # Input strip colour
    strip = input("Input the colour of the strip: ").lower()

    while True:  # Strip colour options
        if strip == "blue":
            print("\nRelease when the countdown timer has a 4 in any position.")
            break
        if strip == "yellow":
            print("\nRelease when the countdown timer has a 5 in any position.")
            break
        else:
            print("\nRelease when the countdown timer has a 1 in any position.")
            break

# First function of checks for input
while True:
    if (BombBatteries > 1 and text == "detonate") or (colour == "red" and text == "hold"):
        print("\nPress and immediately release")
        break
    if BombBatteries > 2:
        FRKCheck = get_Bool("There is a 'FRK' label on the bomb. True or False? ")  # FRK label check
        if FRKCheck is True:
            print("\nPress and immediately release")
            break
        else:
            hold()
        break
    else:
        hold()  # If no initial checks trigger results, run Hold function
