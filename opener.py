# Import the necessary modules
import random
import time
import webbrowser
import os

# Create a list to store the generated numbers
numbers = []
tnumbers = []

# Check if the file containing the list of numbers exists
if os.path.exists('numbers.txt'):
    # If it exists, open the file and read the numbers from it
    with open('numbers.txt', 'r') as f:
        numbers = f.read().splitlines()

print("""  #####                                                             #######                                    
 #     #  ####  #    #  ####   ####  #      #####   ####  #    #    #     # #####  ###### #    # ###### #####  
 #       #    # #    # #    # #    # #      #    # #    #  #  #     #     # #    # #      ##   # #      #    # 
  #####  #      ###### #    # #    # #      #####  #    #   ##      #     # #    # #####  # #  # #####  #    # 
       # #      #    # #    # #    # #      #    # #    #   ##      #     # #####  #      #  # # #      #####  
 #     # #    # #    # #    # #    # #      #    # #    #  #  #     #     # #      #      #   ## #      #   #  
  #####   ####  #    #  ####   ####  ###### #####   ####  #    #    ####### #      ###### #    # ###### #    # 
                                                                                                               """)
print('This will open random Schoolbox class pages.')
print('Then you can look through the tabs and see if any ones are your next years classes.')
print("")
print(""".-------------------------------------------------------------------------------------------.
| Make sure you are signed in on the version of Schoolbox that you are using before continuing. |
'-------------------------------------------------------------------------------------------'""")
input('Press ENTER to continue:')
print('')
url = input("What is the domain for your school's thing? ")
print(""".----------------------------------------------------------------------------------------------.
| ⚠️WARNING: Don't set it too low or it will freeze your PC and it will also be hard to close. |
'----------------------------------------------------------------------------------------------'""")
sleep_time = float(input('Enter the number of seconds to sleep for before opening a new tab: '))
staging = "n"
if staging == "n":
    teacher = input("Search Teachers? Y/N: ")

if staging == "n":
    if teacher == "n":
        while True:
            # Get a random number between 1 and 99999
            number = random.randint(1, 99999)
            print('making random number')

        # Check if the number has already been generated
            if number not in numbers:
                print('number not already generated')

                # Add the number to the list of generated numbers
                numbers.append(number)
                print('added number to list')

                # Open the page on the website
                webbrowser.open(url + '/homepage/%d' % number)
                print('opened ' + url + '/homepage/%d' % number)

                # Wait for the specified number of seconds before generating the next number
                print('waiting')
                time.sleep(sleep_time)

                # Convert the numbers in the list to strings
                numbers = [str(n) for n in numbers]
            
                # Save the list of numbers to the file
                with open('numbers.txt', 'w') as f:
                    f.write('\n'.join(numbers))
                print('saved number to numbers.txt')
    elif teacher == "y":
        while True:
            # Get a random number between 1 and 134
            number = random.randint(1, 134)
            print('making random number')

        # Check if the number has already been generated
            if number not in tnumbers:
                print('number not already generated')

                # Add the number to the list of generated numbers
                tnumbers.append(number)
                print('added number to list')

                # Open the page on the website
                webbrowser.open(url + '/eportfolio/%d/profile' % number)
                print('opened ' + url + 'eportfolio/%d/profile' % number)

                # Wait for the specified number of seconds before generating the next number
                print('waiting')
                time.sleep(sleep_time)

                # Convert the numbers in the list to strings
                tnumbers = [str(n) for n in tnumbers]
            
                # Save the list of numbers to the file
                with open('tnumbers.txt', 'w') as f:
                    f.write('\n'.join(tnumbers))
                print('saved number to tnumbers.txt')


