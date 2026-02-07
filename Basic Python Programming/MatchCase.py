color=input("Enter Color: ")

match color:
    case "Green":
        print("Go")
    case "Yellow":
        print("Look")
    case "Red":
        print("Stop")
    case _:
        print("Wrong Color!")