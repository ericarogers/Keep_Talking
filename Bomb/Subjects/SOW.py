'''Subject of Wires'''

'''Import & define useful functions'''
from Bomb import useful_funct
get_NumRange = useful_funct.get_NumRange
get_RealCol = useful_funct.get_RealCol
from Bomb import define_bomb
SerialEven = define_bomb.SerialEven


# User input wire count
wire_count = get_NumRange("Input the number of wires:\n", 1, 7)

print ("\n-- Input the wires in order from top to bottom --\n")

wire_number = 1  # wire number for output
colours = []  # empty list to store colours


# Check and store colours for each wire
while True:  
    if wire_count > 0:
        # input & ensure it is a valid colour from specified indexing
        newwire = get_RealCol("Input the colour of wire "+str(wire_number)+":\n", 0, 1, 2, 3, 4)
        colours.append(newwire)  # add colours to list
        wire_number += 1  # wire number count for user output
        wire_count -= 1  # count down until no more colours to check
    else:
        break

# Wire solutions output
print("")
while True:
    if len(colours) == 3:  #3 Wire Options
        if "red" not in colours:
            print ("Cut the second wire")
            break
        if (colours.count("blue")) == 2:
            print ("Cut the last blue wire")
            break
        else:
            print ("Cut the last wire")
            break
    if len(colours) == 4:  #4 Wire Options
        if (colours.count("red")) > 1 and (SerialEven == True):
            print ("Cut the last red wire")
            break
        if (colours[-1] == "white") and ("red" not in wires) or ((colours.count("blue")) == 1):
            print ("Cut the first wire")
            break
        if (colours.count("yellow")) > 1:
            print ("Cut the last wire")
            break
        else:
            print ("Cut the second wire")
            break
    if len(colours) == 5:  #5 Wire Options
        if (colours[-1] == "black") and (SerialEven is True):
            print("Cut the forth wire")
            break
        if "black" not in colours:
            print ("Cut the second wire")
            break
        else:
            print("Cut the first wire")
            break
    if len(colours) == 6:  #6 Wire Options
        if ("yellow" not in colours) and (SerialEven is False):
            print("Cut the third wire")
            break
        if "red" not in colours:
            print("Cut the last wire")
            break
        else:
            print("Cut the fourth wire")
            break

