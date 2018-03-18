'''Subject / module options for user'''

# Import Module/Subject options from Bomb
from Bomb import Subjects


class Bomb(object):

    def __init__(self, SE, SV, BB, PP):
        '''
        Initialize core variables for modules
        SerialEven, SerialVowl, BombBatteries & ParallelPort
        '''
        Bomb.__init__(self, SE, SV, BB, PP)

    def Module(SE, SV, BB, PP):
        '''Module Options'''

        # Subject / Module options for user
        print ("\n\n -- Modules Avaliable --")
        print ("Subject of Wires - SOW")
        print ("Subject of The Button - SOB")
        print ("Subject of Simon Says - SSS")
        print ("Subject of Who's on First - SWF")
        print ("Subject of Memory - SOM")
        print ("Subject of Complicated Wires - SCW")
        print ("Subject of Wire Sequences - SWS")
        print ("Subject of Passwords - SOP")

        while True:  # ask user for module to run chosen module & check
            Option = input("\nWhich module would you like to run? ")
            print ("\n***\n\n")

            if Option == "sow":  # Subject of Wires
                from Bomb.Subjects import SOW
                break

            if Option == "sob":  # Subject of The Button
                from Bomb.Subjects import SOB
                break

            if Option == "sss":  # Subject of Simon Says
                from Bomb.Subjects import SSS
                break

            if Option == "swf":  # Subject of Who's on First
                from Bomb.Subjects import SWF
                break

            if Option == "som":  # Subject of Memory
                from Bomb.Subjects import SOM
                break

            if Option == "scw":  # Subject of Complicated Wires
                from Bomb.Subjects import SCW
                break

            if Option == "sws":  # Subject of Wire Sequences
                from Bomb.Subjects import SWS
                break

            if Option == "sop":  # Subject of Passwords
                from Bomb.Subjects import SOP
                break

            else:
                print("Please input the three letter abbreviation of the module you would like to solve\n")
