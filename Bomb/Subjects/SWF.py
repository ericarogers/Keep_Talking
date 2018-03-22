'''Subject of Who's on First'''

'''Import & define useful functions'''
from Bomb import useful_funct
get_Bool = useful_funct.get_Bool

# Display Options

disp1 = {"Top Left": ["ur"],
        "Top Right": ["first", "okay", "c"],
        "Middle Left": ["yes", "nothing", "led", "they are"],
        "Middle Right": ["blank", "read", "you", "your", "you're", "their"],
        "Bottom Left": [" ", "reed", "leed", "they're"],
        "Bottom Right": ["display", "says", "no", "lead", "hold on", "you are", "see", "cee"],
        }
disp2  = {"ready": ["yes, okay, what, middle, left, press, right, blank, ready"],
          "first": ["left, okay, yes, middle, no, right, nothing, uhhh, wait, ready, blank, what, press, first"],
          "no": ["blank, uhhh, wait, first, what, ready, right, yes, nothing, left, press, okay, no"],
          "blank": ["wait, right, okay, middle, blank"],
          "nothing": ["uhhh, right, okay, middle, yes, blank, no, press, left, what, wait, first, nothing"],
          "yes": ["okay, right, uhhh, middle, first, what, press, ready, nothing, no, what, left, uhhh, yes"],
          "what": ["uhhh, what"],
          "uhhh": ["ready, nothing, left, what, okay, yes, right, no, press, blank, uhhh"],
          "left": ["right,left"],
          "right": ["yes, nothing, ready, press, no, wait, what, right"],
          "middle": ["blank, ready, okay, what, nothing, press, no, wait, left, middle"],
          "okay": ["middle, no, first, yes, uhhh, nothing, wait, okay"],
          "wait": ["uhhh, no, blank, okay, yes, left, first, press, what, wait"],
          "press": ["right, middle, yes, ready, press"],
          "you": ["sure, you are, uh huh, what?, done, uh uh, hold, you"],
          "you are": ["your, next, like, uh huh, what?, done, uh uh, hold, you, u, you're, sure, ur, you are"],
          "your": ["uh uh, you are, uh huh, your"],
          "you're": ["you, you're"],
          "ur": ["done, u, ur"],
          "u": ["uh huh, sure, next, what?, you're, ur"],
          "uh huh": ["uh huh"],
          "uh uh": ["ur, u, you are, you're, next, uh uh"],
          "what?": ["you, hold, you're, your, u, done, uh uh, like, you are, uh huh, ur, next, what?"],
          "done": ["sure, uh huh, next, what?, your, ur, you're, hold, like, you, u, you are, uh uh, done"],
          "next": ["what?, uh huh, uh uh, your, hold, sure, next"],
          "hold": ["you are, u, done, uh uh, you, ur, sure, what?, youre, next, hold"],
          "sure": ["you are, done, like you're, you, hold, uh huh, ur, sure"],
          "like": ["you're, next, u, ur, hold, done, uh uh, what?, uh huh, you, like"],
          }


def disp_opt(display,disp):
    '''Return display options'''

    while True:
        output = 0
        if len(display) == 6:  # if Step 1
            for first, second in display.items():  # for word options
                for third in second:  # for each word
                    if third == disp:  # if the word is the same as user input
                        print("\nClick the label on the", first)
                        output = 1
        if len(display) == 28:  # if Step 2
            for first, second in display.items():  # for word options
                for third in second:  # for each word
                    if first == disp:  # if the word is the same as user input
                        print("\nClick the first word in the following options...", third)
                        output = 2
        if (output) == 1 or (output) == 2:  # if output achieved - continue
            break
        else:  # else repeat input until output achieved
            disp = input("Invalid input. Try again: ").lower() 

while True:

    # Define displays via user input & return options through funct
    disp_int = input("\n\n<<Step 1>>\nEnter the display label: ")
    
    # iterate through options step 1
    disp_opt(display=disp1, disp=disp_int)

    disp_int2 = input("\n\n<<Step 2>>\nEnter the label now in the position from Step 1: ")
    
    # iterate through options step 2
    disp_opt(display=disp2, disp=disp_int2)

    # Repeat function
    Cont = get_Bool("\n***\nModule incomplete. True or False? ")
    if Cont is True:
        pass
    else:
        break
