'''Subject of Wire Sequences'''

'''Import & define useful functions'''
from Bomb import useful_funct
get_RealCol = useful_funct.get_RealCol
get_Alpha = useful_funct.get_Alpha
get_Bool = useful_funct.get_Bool


'''List of wire cut options'''
cutopts = {"red": [["c"], ["b"], ["a"], ["a", "c"], ["b"], ["a", "c"], ["a", "b", "c"], ["a", "b"], ["b"]],
          "blue": [["b"], ["a", "c"], ["b"], ["a"], ["b"], ["b", "c"], ["c"], ["a", "c"], ["a"]],
          "black": [["a", "b", "c"], ["a", "c"], ["b"], ["a", "c"], ["b"], ["b", "c"], ["a", "b"], ["c"], ["c"]],
          }


def wire_action():
    '''
    Takes user input, makes note,
    supplies solution by checking lists for occurance
    '''

    Red = 0
    Blue = 0
    Black = 0
    Cont = True

    while Cont is True:  # ensure valid input for wire
        col = get_RealCol("\nDescribe your wire (colour): ", 0, 1, 4)
        while True:
            letter = get_Alpha("\nDescribe your wire (letter): ")
            if letter == "a" or letter == "b" or letter == "c":
                break
            else:
                print("Please enter a, b, or c!")

        # Store current wire description for list search & user output
        Dec_Wire = [col,letter]

        if Dec_Wire[0] == "red":
            Colour = Red
            Red += 1  # Add to red count
        if Dec_Wire[0] == "blue":
            Colour = Blue
            Blue += 1  # Add to blue count
        if Dec_Wire[0] == "black":
            Colour = Black
            Black += 1  # Add to black count

        # Empty list to store final solution (rewritten on each iteration of code)
        Sol = []

        # Check cut options list for occurance
        for let in cutopts[Dec_Wire[0]][Colour]:
            if let in Dec_Wire:
                Sol.append("cut")
            else:
                pass

        # Solution Output
        if "cut" in Sol:
            print("\n-- Action: Cut! --")
        else:
            print("\n-- Action: Don't cut! --")

        # After 6 wires, ask if user would like to continue
        if (Blue+Red+Black) >= 6:
            Cont = get_Bool("\n***\nContinue? True or False: ")
            if Cont is True:
                pass
            else:
                break

wire_action()
