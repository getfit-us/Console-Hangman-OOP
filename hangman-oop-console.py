"""practice re-write of my hangman console game"""

import random
from os import system, name
from pathlib import Path

"""  import sleep to show output for some time period"""
from time import sleep

""" improt external words from file, if not use a built in list of words"""
try:
    
    p = Path(__file__).with_name('words.txt')
    with p.open('r') as f:
        content = f.read()
        WORDS = content.split("\n")
        f.close()

except:
    WORDS = ["jazz", "magic", "money", "gold", "dollar", "ball", "doll", "billard", "soda", "sofa", "lunch", "ghost", "girl"]
    print("Could not load words from text file words.txt")
else:
    print("Loading words from text file words.txt")



def clear():
        """Clears Console Screen """
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')


class User():
    """User class"""
    numguesses = 0
    displayword = []


    

    def display(self,displayword, bksecret, guess, numguesses):
        """ take in secret guess word and return the currect guessed letters in correct spaces """

        
    
        #find position of letters in secret
        index = self.find_indexes(guess, bksecret)
        # print("return from find indexes:", index)
        if len(index) > 0:
            for i in index:
                #loop through returned index update display
                displayword[i] = guess
        return displayword

    def split(self,word,secret): 
        """ split string into list of characters from multiple character input """
        word = list(word)
        secret = list(secret)
        for l in word:
            if l in secret:
                print("You Guessed a correct letter:", l)
                secret.remove(l)
                
                
        
        secret = "".join(secret)
                

        return secret

    def find_indexes(self,letter, word):
        """ account for multiple letters at once.
         take input and split charaters into a list and iterate them to pass each letter and index to function """
        
        indexes = []
        for n,l in enumerate(word):
            if l == letter:
                indexes.append(n)
        
        return indexes

    def usedwords(self,word):
        """keeps track of used letters """
        listof_used_letters = []
        
        for l in word:
            listof_used_letters.append(l)

        return listof_used_letters


    def pick_secret(self,WORDS,word_length):
        """Random pick the secret word takes in desired lenght of word  """
        wordlist = []
        # check list of words create random secret word based on difficulty level
        for word in WORDS:
            if len(word) == word_length:
                wordlist.append(word)
        return random.choice(wordlist)
        


    def game(self,number_guesses,secret,maxguesses):
       
        bksecret  = secret
        guess = ""
        winner = 0
        
        guessmultichar = []
        listof_used_letters = []
        displayword = []

       

        while winner == 0:  # loop for word game play
            clear() #clear screen to keep current stats

            if number_guesses == maxguesses: #end game after 7 guesses 
                print("Sorry you have lost, Try Again!")
                print("You have made", number_guesses, "incorrect guesses.\n")
                print(f"The Correct Word was: {bksecret}.")
                sleep(3)
                winner = 1 
                break
        
            

            print(F"Current Number of Guesses: {number_guesses} \n")  #show number of Guesses

            if number_guesses == 0:
                for char in secret: #add space holders for charaters in secret word
                    displayword.append(" _ ")

            print("".join(displayword)) #display " _ _ _ " for secret word 
            print("Previosuly guessed letters:",",".join(listof_used_letters))

            guess = input("Guess a letter , multiple letter's or the whole word: ")
            guess = guess.lower() # change to lowercase 
            
            
            if guess in listof_used_letters and guess not in secret: #check for previous guess and restart before number of tries gets incremented 
                print("you already guessed this letter", guess)
                sleep(1)
                continue
            else: #letter is new so update list of guessed letters 
                listof_used_letters = listof_used_letters + self.usedwords(guess) # update list of used letters after checking for second time use
            
            number_guesses += 1 #increment number of guesses after checking to duplicate guess
            self.display(displayword, bksecret, guess, number_guesses) #update display word
            

            if guess == secret: #check for the whole word being guessed
            
                print("You Guessed The Correct Word!\n")
                print("You Win! it took you a total of", number_guesses, "guesses.\n")
                print("The word is", bksecret, "\n")

                winner = 1 # set winnder to 1 to end game play loop
                sleep(3)
                break

            elif len(guess) > 1 and guess in secret: # check for multiple chars being guessed at once if so split
                secret = self.split(guess,secret) #update new secret with removed letters and 
                for g in guess:
                    print(g)
                    displaystr = self.display(displaystr,bksecret,g,number_guesses)
                continue
                
            elif guess in secret: #if guessed character is found in secret and is now only one character 
                
                tempsec = [] #create temp secret list of letters
                for char in secret:
                    tempsec.append(char)
                    
                    if len(guess) == 1 and char == guess: #remove found letter and update secret with out guessed letter
                        print("You Guessed a correct letter")
                        tempsec.remove(char)
                    
                secret = "".join(tempsec)
                if len(secret) == 0: # verfiy all the letters have not been guessed
                    print("You Guessed The Correct Word!\n")
                    print("You Win! it took you a total of", number_guesses, "guesses.\n")
                    print("The word is", bksecret, "\n")

                    winner = 1 # set winnder to 1 to end game play loop
                    sleep(3)
                    break
                    


                    
                
            else:
                print("Incorrect Guess, Try Again")
                continue



# Ask the user to choose a difficulty level
while True:
    
    
    clear()

    print("Hangman Text Based Game\n")
    print("Input the number of letters for the secret word")
    print("Input the Maximum Numer of Guesses")
    print("Q to Quit")

    word_length = input("Please select desired worth length: ")
    if word_length.lower() == 'q':
        print("Exiting Game")
        break
    number_guesses = input("Enter Maximum number of guesses: ")
    if number_guesses.lower() == 'q':
        print("Exiting Game")
        break

    
    word_length , number_guesses = int(word_length) , int(number_guesses)
    player = User()
    secret = player.pick_secret(WORDS,word_length)

    # secret = "ball"   #testing  
    player.game(0,secret,number_guesses)

   

    