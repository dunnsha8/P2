# Display an introduction to the game explaining rules and 
# prompt for their name and display that in the welcome message. 
# Return the name to the main program and store it in variable so it can 
# be used throughout the program.

def introduction():
    
    print("Welcome to the Women's Soccer Season Game!")
    print("In this game you will choose a home team and opponents.")
    print("Random scores will be generated and ties are not allowed.\n")

    name = input("Enter your name: ")

    print(f"Welcome to the game, {name}!\n")

    return name