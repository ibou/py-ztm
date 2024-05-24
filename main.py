class PlayerCharacter:
    membership = True  # Class Object Attribute
    def __init__(self, name, age):
        if(PlayerCharacter.membership):
            self.name = name
            self.age = age

    def shout(self):
        print(f"PlayerCharacter {self.name}")
        
    @classmethod
    def adding_things(cls, num1, num2): 
        return cls("somm", num1 + num2)
player1 = PlayerCharacter('Cindy', 22)
player2 = PlayerCharacter('Tom', 33)


print(player1.adding_things(2, 3))
print(PlayerCharacter.adding_things(2,5))
