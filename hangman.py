import random
words=['help','humans','boy']
random_word=random.choice(words)
guess_word=['_']*len(random_word)
print('Welcome to the Hangman Game')
number_attempts=10
while number_attempts>0:
    print(' '.join(guess_word))
    guess_letter=input('enter a letter to guess the word: ')
    if guess_letter in random_word:
        i=random_word.find(guess_letter)
        guess_word[i]=guess_letter
    else:
        number_attempts-=1
    if '_' not in guess_word:
        print('congratulations on the win')
        break


