gitprint ('Welcome to the Guessing Game!!!\n Here you have to guess a secret word, you get 10 chances and 3 total hints')

secret_word = "King Kong"
guess = ''
guess_count = 0

while guess_count < 4 and guess != secret_word:
    guess = input('Guess the secret word : ')
    if guess == secret_word:
        print('You Win! Woohoo!')
    else:
        guess_count += 1
        print("Wrong guess, Try again")

while guess_count in range (4,6) and guess != secret_word:
    print(' Hint 1: monke')
    guess = input('Guess the word (ts easy) : ')
    if guess == secret_word:
        print("Victory is yours")
    elif guess == 'monkey':
        print('ts no that easy')
    else:
        guess_count += 1
        print('Still wrong')

while guess_count in range (6,8) and guess != secret_word:
    print(' Hint 1: monke\n Hint 2: it\'s a big one')
    guess = input('Guess the word(now you\'ve got two full hints): ')
    if guess == secret_word:
        print('You are a Winner!')
    else:
        guess_count += 1
        print('Nah still not correct')

while guess_count in range (8,11) and guess != secret_word:
    print(' Hint 1: monke\n Hint 2: it\'s a big one\n Hint 3: it\'s also a hollywood blockbuster')
    guess = input('Guess the word: ')
    if guess == secret_word:
        print('Finally, you guessed it, I was starting to think you might actually be stupid\n You win!')
    else:
        guess_count += 1
        print('Nah man you\'re stupid')
    
if guess_count == 11 and guess != secret_word:
    print('Okay man, one more try purely out of pity\n DONT MESS THIS UP!!!\n\
           Hint 1: monke\n Hint 2: it\'s a big one\n Hint 3: it\'s also a hollywood blockbuster\
          \n Final Hint: It\'s 2 words both have four letter each and both start with K')
    guess = input('Enter your guess: ')
    if guess == secret_word:
        print('You win!\n ( but honestly you were handed the victory out of pity)')
    else:
        guess_count += 1

if guess_count == 12 and guess != secret_word:
    print('man you really are stupid, the word is ' + secret_word)
    guess = input('ok just go type that word out: ')
    if guess == secret_word:
        print('Finally the game ends(sigh)I though you were just ragebaiting me with those awful guesses\n\n\
              oh yea and you win or whatever, yay!  ')
    else:
        print(' YOU!\n YOU!!!\nTHATS IT IM SICK OF THIS GAME, IM SICK OF BEING A PROGRAM WRITTEN FOR A RETARD LIKE YOU \n\n\
              GAME OVER')