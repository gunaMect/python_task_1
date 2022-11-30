import os
from password_check import validate_password
from username_check import validate_user_name

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Returns True if username is proper else False is returned
    if validate_user_name(username) == False:
        return False

    # Returns True if password is proper else False is returned
    if validate_password(password) == False:
        return False

    # Check if file exist or not
    if os.path.exists("database.txt") == False:
        print("Database does not exists, Please Register to create database")
        return False

    db = open("database.txt", "r")
    d = []
    f = []
    for i in db:
        a,b = i.split(",")
        b = b.strip()
        d.append(a)
        f.append(b)
        data = dict(zip(d, f))
    db.close()

    if username in data.keys():
        print("\nUsername Present in the database")
    else:
        print("\nUsername Not present")
        print("\nYou can go to Registration via the option 1")
        return False

    try:
        if data[username]:
            try:
                if password == data[username]:
                    print("Hi", username)
                    return True
                else:
                    print("\nPassword or username is incorrect")
                    return False
            except:
                print("\nUser name exists, but incorrect password is provided")
        else:
            print("\nIncorrect password or username")
            return False
    except:
        print("\nLogin error")

'''
Validate the user name which is provided by the user
Check 1: "@" should not be followed by "."
Check 2: Should not start with number or special characters
Check 3: Also handles other error cases
'''

def register():
    user_name_check = False
    password_check_status = False
    names = []

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Returns True if username is proper else False is returned
    user_name_check = validate_user_name(username)

    # Returns True if password is proper else False is returned
    password_check_status = validate_password(password)

    # Write data to the database only if the validation is successful
    if user_name_check == True and password_check_status == True:
        names.append(username)
        names.append(password)
        with open("database.txt", mode="a") as file:
            file.write(", ".join(names))
            file.write("\n")
            print("\nUser created successfully!", end=" ")
            print("Please login to proceed")
        return True
    else:
        return False

'''
Based on the user input, either current password is displayed or
new password will be updated if the username exist in the database
'''
def forgot_password():
    username = input("Enter your username: ")

    print("Username: {}".format(username))
    if validate_user_name(username) == False:
        return False

    if os.path.exists("database.txt") == False:
        print("Database does not exists, Please Register to create database")
        return False

    try:
        if not len(username)<5:
            db = open("database.txt", "r")
            d = []
            f = []
            for i in db:
                a,b = i.split(",")
                b = b.strip()
                d.append(a)
                f.append(b)
                data = dict(zip(d, f))
            db.close()

        if username not in data:
            print("Username does not exists in the database\n")
            print("Goto Registration first")
            return False
        user_choice = int(input("Choose 1 to view password or 2 to update password: "))

        if user_choice == 1:
            print("Password is: ", data[username])
        elif user_choice == 2:
            new_password = input("Enter the new password: ")
            if username in data.keys():
                print("Username exists in the database")
                if validate_password(new_password) == False:
                    return False
                data.update({username:new_password})
                    # Update the database with the provided new password
                with open("database.txt", 'w') as f:
                    for key, value in data.items():
                        f.write('%s, %s\n' % (key, value))
                print("\nPassword updated successfully\n")
            else:
                print("Username does not exist")

    except:
        print("Error in forgot password")


def main():
    print("\nWelcome to the python authentication page")

    try:
        # Get the user_choice from the prompt
        user_choice = int(input("Please enter 1 for registration, 2 for login, 3 for forget password: "))
        if user_choice==1:
            print("\nYou have selected registration...")
            print("\nPlease enter user name which will be your email-id")
            registration_status = register()

            if registration_status == True:
                print("\nRegistration successful")
            else:
                print("\nRegistration unsuccessful")
        elif user_choice==2:
            print("\nYou have selected login...")
            if login() == False:
                print("\nLogin failed")
            else:
                print("\nLogin Success")
        elif user_choice==3:
            print("\nYou have selected forgot password...")
            print("\nYou can view old password or can update with the new password")
            if forgot_password() == False:
                print("\nForgot password request failed")
            else:
                print("Forgot password request Success")
        else:
            print("\nSelect proper choice")
    except:
        print("\nProvide proper user inputs")

if __name__ == "__main__":
    main()
