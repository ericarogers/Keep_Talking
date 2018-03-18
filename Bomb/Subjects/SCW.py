'''Subject of Complex Wires'''

'''Import & define useful functions'''
from Bomb import useful_funct
get_NumRange = useful_funct.get_NumRange
get_Bool = useful_funct.get_Bool
from Bomb import define_bomb
SerialEven = define_bomb.SerialEven
ParallelPort = define_bomb.ParallelPort
BombBatteries = define_bomb.BombBatteries


# User instruction & example for usability
print("Input the wire colours & 'LED' or 'Star', seperated by spaces")
print("For example, a red wire connected to a star, would be inputted as 'red star'")
    
while True:

    # User input to describe wire
    descript = input("***\n\nInput the wire description:\n").lower()

    # Combination options for wires
    comb_NA = [["star"], ["red", "star"], ["white"]]  # without restriction
    comb_SN = [["red", "blue","led"], ["red", "blue"], ["red"], ["blue"],]  # with even ending to SerialNumber
    comb_PP = [["red", "blue", "star"], ["blue", "star", "led"], ["blue", "led"],]  # with Parallel Port
    comb_BB = [["red", "star", "led"], ["red", "led"], ["star", "led"],]  # with 2+ Batteries
    comb_all = []

    # Create list of options depending on defined bomb
    def combos_all(combos):
        comb_all.append(combos)
    combos_all(comb_NA)  # auto add combos without restrictions
    if SerialEven is True:
        combos_all(comb_SN)  # add if Serial number end even
    if ParallelPort is True:
        combos_all(comb_PP)  # add if Parallel Port
    if BombBatteries >= 2:
        combos_all(comb_BB)  # add if 2 or more Batteries

    # Listing wire description from user input in order for search
    PlexWire = []
    def wire_desc(colour):
        PlexWire.append(colour)  # append wire details function
    if "red" in descript:
        wire_desc("red")
    if "blue" in descript:
        wire_desc("blue")
    if "white" == descript:
        wire_desc("white")
    if "star" in descript:
        wire_desc("star")
    if "led" in descript:
        wire_desc("led")

    CutCount = 0  # set cut count to ensure singular output
    for l in comb_all:  # iterate through options
        for item in l:
            if item == PlexWire:
                print("\n-- Cut wire! --")
                CutCount += 1
                break
            else:
                pass
    if CutCount == 0:
        print("\n-- Don't cut wire! --")

    Cont = get_Bool("\n***\nContinue? True or False: ")
    if Cont is True:
        pass
    else:
        break
