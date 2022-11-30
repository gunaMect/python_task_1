# Function to validate the password
def validate_password(passwd):
    SpecialSym = "~`!@#$%^&*()_-+={[}]|\:;\"'<,>.?/"
    return_val = True
    # print("\nPassword provided inside the function is: {}".format(passwd))
    if not any(char in SpecialSym for char in passwd):
        print('\nPassword should have at least one of the special symbols')
        return_val = False
        return return_val
    if len(passwd) < 5:
        print('\nLength should be at least 5')
        return_val = False
        return return_val
    if len(passwd) > 15:
        print('\nLength should be not be greater than 15')
        return_val = False
        return return_val
    if not any(char.isdigit() for char in passwd):
        print('\nPassword should have at least one numeral')
        return_val = False
        return return_val
    if not any(char.isupper() for char in passwd):
        print('\nPassword should have at least one uppercase letter')
        return_val = False
        return return_val
    if not any(char.islower() for char in passwd):
        print('\nPassword should have at least one lowercase letter')
        return_val = False
        return return_val
    return return_val