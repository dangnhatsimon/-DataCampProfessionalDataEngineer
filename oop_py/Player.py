class Player:
    MAX_POSITION = 10
    
    # Define a constructor
    def __init__(self, position):
      
        # Check if position is less than the class-level attribute value
        if position <= Player.MAX_POSITION:
            self.position = position
      
        # If not, set equal to the class-level attribute
        else:
            self.position = Player.MAX_POSITION

# Create a Player object, p, and print its MAX_POSITITON
p = Player(6)
print(p.MAX_POSITION)


# Create Players p1 and p2
p1 = Player(9)
p2 = Player(5)

print("MAX_POSITION of p1 and p2 before assignment:")
# Print p1.MAX_POSITION and p2.MAX_POSITION
print(p1.MAX_POSITION)
print(p2.MAX_POSITION)

# Assign 7 to p1.MAX_POSITION
p1.MAX_POSITION = 7

print("MAX_POSITION of p1 and p2 after assignment:")
# Print p1.MAX_POSITION and p2.MAX_POSITION
print(p1.MAX_POSITION)
print(p2.MAX_POSITION)


class Player:
    MAX_POSITION = 10

    def __init__(self):
        self.position = 0

    def move(self, steps):
        if self.position + steps < Player.MAX_POSITION:
            self.position += steps 
        else:
            self.position = Player.MAX_POSITION     


# Create a Racer class inheriting from Player
class Racer(Player):
    # Create MAX_POSITION with a value of 15
    MAX_POSITION = 15


# Create a Player and a Racer objects
p = Player()
r = Racer()

print("p.MAX_POSITION = ", p.MAX_POSITION)
print("r.MAX_POSITION = ", r.MAX_POSITION)