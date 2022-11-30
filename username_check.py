def validate_user_name(str):
    # print("Username provided inside the function is: {}".format(str))
    return_val = True
    try:
        countOfAt = str.count("@")
        countOfDot = str.count(".")
        indexOfAt = str.index("@")
        indexOfDot = str.index(".")
        lengthOfStr = indexOfDot - indexOfAt - 1

        if (countOfAt > 1) or (countOfDot > 1) or (indexOfAt < 3) or (lengthOfStr < 4):
            return_val = False
            print("Provide proper User name, Host name & Domain name")
            return return_val

        if str[0].isalpha() == False:
            return_val = False
            print("Provide User name starting with characters[a-z, A-Z]")
            return return_val

        # Returns True if username is proper else False is returned
        return return_val
    except:
        return_val = False
        print("Provide proper Username/Password")
        return return_val