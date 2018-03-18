'''Subject of Memory'''

'''Import & define useful functions'''
from Bomb import useful_funct
get_NumRange = useful_funct.get_NumRange

# Step 1
Display1 = get_NumRange("\n\n<<Stage 1>>\nInput the display: ", 1, 5)
if Display1 == 1 or Display1 == 2:
    print("-- Press the button in the second position --")
    Position1 = 2
if Display1 == 3:
    print("-- Press the button in the third position --")
    Position1 = 3
if Display1 == 4:
    print("-- Press the button in the fourth position --")
    Position1 = 2
Label1 = get_NumRange("Input the label of this button: ", 1, 5)

# Step 2
Display2 = get_NumRange("\n\n<<Stage 2>>\nInput the display: ", 1, 5)
if Display2 == 1 or Display2 == 4:
    print("-- Press the button labelled 4 --")
    Label2 = 4
    Position2 = get_NumRange("Input the position of this button: ", 1, 5)
if Display2 == 2:
    print("-- Press the button in position", (Position1, " --"))
    Position2 = Position1
    Label2 = get_NumRange("Input the label of this button: ", 1, 5)
if Display2 == 3:
    print("-- Press the button in the first position --")
    Position2 = 1
    Label2 = get_NumRange("Input the label of this button: ", 1, 5)

# Step 3
Display3 = get_NumRange("\n\n<<Stage 3>>\nInput the display: ", 1, 5)
if Display3 == 1:
    print("-- Press the button labelled", (Label2), " --")
    Label3 = Label2
if Display3 == 2:
    print("-- Press the button labelled", (Label1), " --")
    Label3 = Label1
if Display3 == 3:
    print("-- Press the button in the third position --")
    Label3 = get_NumRange("Input the label of this button: ", 1, 5)
if Display3 == 4:
    print("-- Press the button labelled 4 --")
    Label3 = 4

# Step 4
Display4 = get_NumRange("\n\n<<Stage 4>>\nInput the display: ", 1, 5)
if Display4 == 1:
    print("-- Press the button in position", (Position1), " --")
if Display4 == 2:
    print("-- Press the button in the first position --")
if Display4 == 3 or Display4 == 4:
    print("-- Press the button in position", (Position2), " --")
Label4 = get_NumRange("Input the label of this button: ", 1, 5)

# Step 5
Display5 = get_NumRange("\n\n<<Stage 5>>\nInput the display: ", 1, 5)
if Display5 == 1:
    print("-- Press the button with the label", (Label1), " --")
if Display5 == 2:
    print("-- Press the button with the label", (Label2), " --")
if Display5 == 3:
    print("-- Press the button with the label", (Label3), " --")
if Display5 == 4:
    print("-- Press the button with the label", (Label4), " --")
