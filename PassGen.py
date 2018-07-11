####### REQUIRED IMPORTS #######
import os
import sys
import click
import random
import string
from time import sleep

####### FUNCTIONS ######
def displayHeader():
    """
    () -> ()

    Function that is responsible for printing the application header
    and menu
    """
    # Clear the console window
    os.system('cls')

    # Print the application header & menu
    print("\033[94m------------------------------\n" + 
          "||    \033[92mPassword Generator    \033[94m||\n" +
          "------------------------------\n\n" +
          "\033[0mWelcome to Password Generator v1.0\n" + 
          "\033[92mSource Code By: \033[0m\033[1mMark Philips (CoderMP)\n" +
          "\033[91mLicense: \033[0m\033[1mMIT\n\n" +
          "\033[0m\033[1m[1] Generate Password(s)\n" + 
          "[2] Exit Program\n")

def generator(len, num):
    """
    (int, int) -> list

    Function that is repsonsible for generating a random alphanumeric
    password based off the iser request parameters
    """
    # Initialize the list that will hold the generated passwords
    passList = []

    # Initialize a counter variable to assist with generation
    i = 0

    while i < num:
        # Assemble the password
        temp = ''.join(random.choices(string.ascii_lowercase + string.digits, k = len))

        # Append the temp variable value to the passList
        passList.append(temp)

        # Increment the counter
        i += 1
    # Return the password list
    return passList

def passParams():
    """
    () -> ()

    Function that is responsible for retrieving the desired password
    generation paramters of the user.
    """
    # Prompt the user for their desired pass length and how many to generate
    len = click.prompt('How long would you like your password(s) to be? >>', type=int)
    num = click.prompt('How many password(s) would you like to generate? >>', type=int)

    print('\n')

    # Assemble the password list
    passwordList = generator(len, num)

    # Print the password list to the console
    print(*passwordList, sep='\n')

def genLogic():
    """
    () -> ()

    Function that is responsible for executing the application logic based on the user's choice
    """
    # Prompt the user for input
    op = click.prompt('Enter choice >>', type=int)

    if (op == 1):
        print('\n')
        # Call method that retrieves the password generation parameters
        passParams()

        while(True):
            # Prompt the user as to whether or not they'd like to generate another set
            choice = click.prompt('\n\nWould you like to generate another set? (y/n) >>', type=str)

            # Execute accordingly
            if (choice == 'Y' or choice == 'y'):
                print('\n')

                # Call the function that retrieves the password generation parameters
                passParams()

            if (choice == 'N' or choice == 'n'):
                # Notify the user of navigation back to the main menu
                print('Returning you to the main menu....')
                sleep(1.3)
                os.system('cls')
                break

        # Display the main menu and prompt the user for input
        displayHeader()
        genLogic()

    if (op == 2):
        # Notify the user of the termination sequence
        print('\nTerminating program...')
        sleep(2)

        # Terminate
        sys.exit()

    else:
        # Notify the user of their command error and re-prompt them for input
        print('\033[91mInvalid command, please try again!\033[0m')
        genLogic()

####### MAIN PROGRAM #######
if __name__ == '__main__':
    displayHeader()
    genLogic()