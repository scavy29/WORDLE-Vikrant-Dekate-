from termcolor import colored                           #To turn letters into green and yellow whenever required
import random                                           #imports random module
import sys                                              #lets access system specific paramters and functions


def randomword_fromlist():                                 #defined Function for rrandom pulling of words from text file
    with open("words.txt") as f:
        word = f.read().splitlines()
        return random.choice(word)


print("------WORDLE-----")
print("Guess a 5 Letter Word:-\n")


word = randomword_fromlist()

for chance in range(6):
    guess = input().lower()
    
    
    # overwrite the last line in the console
    sys.stdout.write('\x1b[1A')                             #ANSI Escape Code
    sys.stdout.write('\x1b[2K')

    #Turn letters into Green, Yellow
    for i in range(min(len(guess), 5)):
        if guess[i] == word[i]:
            print(colored(guess[i], 'green'), end="")
        elif guess[i] in word:
            print(colored(guess[i], 'yellow'), end="")
        else:
            print(guess[i], end="")
    print()
    
#To check for Word in Text File
    filename = 'words.txt'

    with open(filename) as f:
        search = f.read()

    if guess not in search:
        print("Name not found.")

    #Final Guess 
    if len(guess)>5 or len(guess)<5:
        print("Letter must be 5 Letter only")
    if guess == word:                                                                       #Matching String with randomly picked Word
        print("Wohoo you guessed the WORDLE in %i times." %chance)
    elif chance == 5:                                                                          #Comparing the attempts
        print("6 Chances are Over")
        print("Wordle of the Day is: %s"%word)
        