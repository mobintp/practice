
import random
import requests 
import string 
import json


url = "https://www.randomlists.com/data/words.json"
response = requests.get(url)


if response.status_code == 200:
    data = json.loads(response.text)
else:
    print("Request Failed", response.status_code)


words = list(data['data'])


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()



def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alph = set(string.ascii_uppercase)
    used_letters = set()

    lives = 8
    
    # getting user letter
    while len(word_letters) > 0 and lives > 0:
        # letters used 
        # ' '.join(['a', 'b', 'cc',]) ---> 'a b cd'ArithmeticError
        print('you have:', lives, 'lives, You have used these letters: ', ' '.join(used_letters))
        
        # what current word is (ie W - R D) 
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ", ' '.join(word_list))
        
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alph - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1 
                
        elif user_letter in used_letters:
            print("you have already used that character, pls try again.")

        else:
            print("Invalid character, please try again.")
            
    if lives == 0:
        print('you died, the word was: ', word)
    else:
        print(f"you guessed the word {wrod} correctly, goodbye.")
        


hangman()


