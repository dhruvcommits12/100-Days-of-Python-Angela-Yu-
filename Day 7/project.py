import random
from hangman_art import stages,logo
from hangman_words import word_list

placeholder = ""

chosen_word = random.choice(word_list)
word_len = len(chosen_word)
lives = 6

print(logo)
print("Welcome to Hangman!")
print("Guess the word before the man is hanged.\n")

for position in range(word_len):
    placeholder+="_"

print(placeholder)

game_over=False
correct_words=[]
guessed_words=[]
correct_guess=False

while not game_over:
    guess=input("Guess a letter : ").lower()
    if guess in guessed_words:
        print(f"You have already guessed {guess}")
    
    else:
        display=""
        guessed_words.append(guess)
        for letter in chosen_word:
            if guess==letter:
                display+=letter
                correct_guess=True
                if letter not in correct_words:
                    correct_words.append(letter)
            
            elif letter in correct_words:
                display+=letter

            else:
                display+="_"
    
        print(display)

        if not correct_guess:
            lives-=1
            print(f"{guess} is not in the word. You lose a life.")
    
        correct_guess=False
    
        print(f"You have {lives} lives remaining")
        print(stages[lives])
    
        if lives==0:
            game_over=True
            print(f"You lose. The correct word was {chosen_word}")
        
        if "_" not in display:
            game_over=True
            print("You win")

    

    

        
  

    