# alana holdaway 
# 2. Display of menu and return choice. 
# Store in variable and use this value to determine which function to call next.

def display_menu(): 
    print("\n--Menu--")
    print("1. Add Team")
    print("2. Enter number of games your team will play")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice 
