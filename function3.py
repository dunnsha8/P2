def choose_team(excluded_team=""):
    teams = [
        "BYU",
        "Utah",
        "Utah State",
        "Weber State",
        "Gonzaga",
        "Pepperdine",
        "San Diego",
        "Santa Clara"
    ]

    if excluded_team != "":
        teams.remove(excluded_team)

    print("\nChoose a team:")
    for i in range(len(teams)):
        print(f"{i + 1}. {teams[i]}")

    choice = int(input("Enter your choice: "))
    return teams[choice - 1]