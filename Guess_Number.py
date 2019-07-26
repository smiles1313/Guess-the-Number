#Guess_Number

import random

name = input('Hello! What is your name?')
intro = print('Well, %s, I am thinking of a number between 1 and 20. You have six chances to get it right.' %(name))


def game():
	tries = 0
	secret_number = random.randint(1,20)

	while tries < 6:
		tries = tries + 1
		guess = input('Take a guess.')

		if guess.isdigit() == False:
			print('Please remember to enter a number.')

		else:
			guess = int(guess)

			print(guess)

			if guess == secret_number:
				if tries == 1:
					print('Good job, %s! You guessed my number in %d guess!' %(name, tries))
					break
				else:
					print('Good job, %s! You guessed my number in %d guesses!' %(name, tries))
					break 
			elif guess < secret_number:
				print('Your guess is too low.')
			elif guess > secret_number:
				print('Your guess is too high.')
	else:
		print('My number was %d. You did not guess my number in the six chances you were given.' %(secret_number))



game()

	

