import os
from password_check import validate_password
from username_check import validate_user_name

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if not len(username or password)<5:
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

        # print(data[username])

        if username in data.keys():
            print("\nUsername Present, ", end =" ")
            print("\nvalue =", data[username])
        else:
            print("\nUsername Not present")
            print("\nYou can go to Registration via the option 1")
            return False

        try:
            if data[username]:
                try:
                    if password == data[username]:
                        print("\nLogin Success")
                        print("Hi", username)
                        return True
                    else:
                        print("\nPassword or username is incorrect")
                except:
                    print("\nUser name exists, but incorrect password is provided")
            else:
                print("\nIncorrect password or username")
        except:
            print("\nLogin error")
    else:
        print("\nProvide Proper username/password")

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
            print("\nUser created successfully!")
            print("\nPlease login to proceed:")
        return True
    else:
        return False

# Below is the for loop to test password and username check
'''
    password = ["guna", "gunar393", "gunasekC1@", "gunasekC1@34"]
    for password_1 in password:
        password_check_status = validate_password(password_1)
        print("Username_check: {} and password_check: {}".format(user_name_check, password_check_status))

    for names in username:
        print("*******")
        print("Username: {} and password: {}".format(names, password))
        # Returns 0 if username is proper else 1 is returned
        user_name_check = validate_user_name(names)
        # user_name_check = validate_user_name(username)
        # password_check_status = validate_password(password)

        print("Username_check: {} and password_check: {}".format(user_name_check, password_check_status))
        print("*******")
'''

def forget_password():
    username = input("Enter your username: ")

    print("Username: {}".format(username))
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
                print("Username exists in the database, ", end =" ")
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

        # print(data)
        # Check the provided user name is available in the database
        # if username in data.keys():
        #     print("\nUsername Present, ", end =" ")
        #     print("\nvalue =", data[username])
        # else:
        #     print("\nUsername Not present")
        #     print("\nYou can go to Registration via the option 1")
        #     return False

    except:
        print("Error in forgot password")


def main():
    print("\nWelcome to the python authentication page")

    # Get the user_choice from the prompt
    user_choice = int(input("Please enter 1 for registration 2 for login 3 for forget password: "))
    # user_choice = 2
    if user_choice==1:
        print("\nYou have selected registration...")
        print("\nPlease enter user name which will be your email-id")
        registration_status = register()
        print("\nRegistration status: ", registration_status)

        if registration_status == True:
            print("\nRegistration successful")
        else:
            print("\nRegistration unsuccessful")
    elif user_choice==2:
        print("\nYou have selected login...")
        if login() == False:
            print("\nLogin failed")
    else:
        print("\nYou have selected forgot password...")
        print("\nYou can view old password or can update with the new password")
        forget_password()

if __name__ == "__main__":
    main()
