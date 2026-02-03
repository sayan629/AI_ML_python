#| Q8. Create a class with:            |
#| • a class variable player_count     |
#| • instance variables name and level |
#| Track how many players were created.|
#______________________________________|

class Player:
    ## Class variable (shared by all objects)
    player_count=0
    
    # Constructor
    def __init__(self,name,level):
        self.name=name          # Instance variable (unique for each player)
        self.level=level        # Instance variable
        Player.player_count+=1  ## Increase class variable whenever a new object is created
    
p1=Player("Messi",1)
p2=Player("Ronaldo",2)

print("Total Number of Players: ",Player.player_count) #Accessing class variable using class name