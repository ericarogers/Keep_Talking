'''Subject of Passwords'''

'''Import & define useful functions'''
from collections import Counter
from Bomb import useful_funct
get_RealCol = useful_funct.get_RealCol
get_Alpha = useful_funct.get_Alpha
get_Bool = useful_funct.get_Bool


# Password combinations
passopts = {"Again": ["a", "a", "n"],
            "After": ["a", "t", "r"],
            "About": ["a", "o", "t"],
            "Below": ["b", "l", "w"],
            "Could": ["c", "u", "d"],
            "Every": ["e", "e", "y"],
            "First": ["f", "i", "t"],
            "Great": ["g", "e", "t"],
            "House": ["h", "u", "e"],
            "Large": ["l", "r", "e"],
            "Learn": ["l", "a", "n"],
            "Never": ["n", "v", "r"],
            "Place": ["p", "a", "e"],
            "Plant": ["p", "a", "t"],
            "Point": ["p", "i", "t"],
            "Right": ["r", "i", "t"],
            "Small": ["s", "a", "l"],
            "Spell": ["s", "e", "l"],
            "Still": ["s", "i", "l"],
            "Their": ["t", "e", "r"],
            "These/There": ["t", "e", "e"],
            "Thing": ["t", "i", "g"],
            "Think": ["t", "i", "k"],
            "Three": ["t", "r", "e"],
            "Water": ["w", "t", "r"],
            "World": ["w", "r", "d"],
            "Would": ["w", "u", "d"],
            "Write": ["w", "i", "e"],
            "Which": ["w", "i", "h"],
            "Where": ["w", "e", "e"],
            }


# Input Check - must be 6 letters
def pass_Check(prompt):
    while True:
        password = get_Alpha(prompt)
        if len(password) == 6:
            return str(password)
        else:
            print("Invalid input! Please try again!\n")
    
# User input for columns
column1 = pass_Check("<<Input letters of first column>>\n")
column3 = pass_Check("<<Input letters of third column>>\n")
column5 = pass_Check("<<Input letters of final column>>\n")

# Lists & Counters for Solution
options = [column1, column3, column5]  # user inputted letters
words = []  # list for options from user input
n = -1

# Building up list of options from user input
for option in options: # checking per input for columns
    n += 1
    for word, letters in passopts.items():
        for letter in letters[n]:  # iterating letters in combinations
            if letter in options[n]:  # iterating letters in input
                    words.append(word)  # list of words with the letters input
            else:
                pass

b = Counter(words)  # count the frequency of the words in words list
solution = b.most_common(1)[0][0]  # store the most common answer

# Return most common word in list as solution
print ("\n-- Password:", solution, " --")

# Addition for single possible issue with repeated letters
if solution == "These/There":
    print("Check the fourth column for 's' or 'r' to determine which.")
