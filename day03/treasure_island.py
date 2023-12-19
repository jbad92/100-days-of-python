print('Welcome to treasure island.')
print('Your mission is to find the treasure.')

choice1 = input('You\'re at a crossroad, where do you want to go? Type "Left" or "Right"').lower()


if choice1 == 'left':
    choice2 = input('You\'ve come to a lake. There is an island in the middle. Type "wait" to wait for a boat or type "swim" to swim across.').lower()
    if choice2 == 'wait':
        choice3 = input('You arrive at the island. There is a house with 3 doors. One red, one yellow, and one blue. Choose a door').lower()
        if choice3 == 'red':
            print("It's a room full of fire. Game over.")
        elif choice3 == 'yellow':
            print('You found the treasure! You win!')
        elif choice3 == 'blue':
            print('You enter a room full of beasts. Game over.')
        else:
            print('Invalid choice. Game over.')
    else:
        print('You got attacked by an angry trout. Game over')
else:
    print('You fell into a hole. Game over.')