import json
import os

# Define the file path for the JSON file where user details will be stored
file_path = 'Pradeep_Bhatta_user_data.json'

# Function to initialize an empty JSON file if it doesn't exist or is empty
def initialize_json_file():
    if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
        with open(file_path, 'w') as json_file:
            json.dump({}, json_file)

# Clear the console screen
os.system('clear')

print("Welcome to Pradeep Bhatta's User Management System!")

# Initialize the JSON file if needed
initialize_json_file()

# Main loop
while True:
    found = False
    print('----' * 20)
    choice = input('1. Sign Up\n2. Sign In\n0. Exit\nEnter your choice: ')
    
    if not choice.isdigit():
        print('Invalid input! Please enter a number.')
        continue
    
    choice = int(choice)
    print('----' * 20)

    os.system('clear')

    # Sign Up process
    if choice == 1:
        print('----' * 20)
        username = input('Enter a username: ')
        password = input('Enter a password: ')
        phone = input('Enter your phone number: ')
        print('----' * 20)

        try:
            # Load existing user data
            with open(file_path, 'r') as jsonRead:
                userDetail = json.load(jsonRead)

            # Check if the username already exists
            if username in userDetail:
                print('==' * 25)
                print('Username already exists! Please try a different username.')
                print('==' * 25)
            else:
                userDetail.update({
                    username: {
                        'password': password,
                        'phone': phone,
                    }
                })

                # Write the updated userDetail dictionary back to the JSON file
                with open(file_path, 'w') as jsonWrite:
                    json.dump(userDetail, jsonWrite)
                    os.system('clear')
                    print('==' * 25)
                    print('User Created Successfully!')
                    print('==' * 25)

        except Exception as e:
            print('==' * 25)
            print(f'Error occurred: {e}')
            print('==' * 25)

    # Sign In process
    elif choice == 2:
        print('----' * 20)
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        print('----' * 20)

        try:
            # Load user data from JSON file
            with open(file_path, 'r') as jsonRead:
                detail = json.load(jsonRead)

            # Check if the username exists in the user data
            if username in detail:
                # Validate password
                if detail[username]['password'] == password:
                    os.system('clear')
                    print('==' * 25)
                    print(f'Welcome to this device, {username}!')
                    print(f'Your phone number is: {detail[username]["phone"]}')
                    print('==' * 25)
                else:
                    os.system('clear')
                    print('==' * 25)
                    print('Incorrect password! Please try again.')
                    print('==' * 25)
            else:
                os.system('clear')
                print('==' * 25)
                print('Username not found! Please sign up first.')
                print('==' * 25)

        except Exception as e:
            print('==' * 25)
            print(f'Error occurred: {e}')
            print('==' * 25)

    # Exit case
    elif choice == 0:
        print('Thank you for using the system! Goodbye!')
        break

    # Invalid option handling
    else:
        os.system('clear')
        print('==' * 25)
        print('Invalid option! Please enter a valid choice.')
        print('==' * 25)
