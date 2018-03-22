'''Store of useful functions'''


def get_Bool(prompt):
    '''Boolean input check & converter'''
    
    while True:  # loop while input not true or false
        try:
            return {"true":True, "false":False, "t": True, "f":False}[input(prompt).lower()]
        except KeyError:
           print ("Please enter True or False! ")


def get_NumRange(prompt, limit1, limit2):
    '''Function to limit input within specified range'''
    
    while True:  # loop while input is not numerical or within limit
        try:
            num = int(input(prompt))  # asking for input & storing for checks
            if (limit1) <= num < (limit2):  # checking if input within limit
                return int(num)
            else:
                print("Invalid Input. Please try again!")
        except:
            print("Invalid Input. Please try again!")


def get_RealCol(prompt, *nums):
    '''
    Function to check colours if input
    included within specified for module
    by specifying them through indexing
    '''
    
    colslist = []
    validcolours = ["red", "blue", "yellow", "white", "black", "green"]

    for num in nums:  # create list for index colours referenced for module
        colslist.append(validcolours[num])

    while True:  # loop to ensure colour is within valid referenced for module
        colour = input(prompt).lower()
        if (colour) in (colslist):  # check input colour(s) in module specific list
            return(colour)
        else:
            print("Invalid Input. Please try again!")


def get_Alpha(prompt):
    '''Alphabetical input check & return in lower'''
    
    while True:  # loop to ensure alphabetical input
        try:
            letter = input(prompt)
            if (letter).isalpha():  # if input is alphabetical return lower
                return(str(letter).lower())
            else:
                print ("Invalid Input - please enter an alphabetical input!\n")
        except:
           print ("Invalid Input - please enter an alphabetical input!\n")
