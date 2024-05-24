class User(object):
    def __init__(self, email) -> None:
        self.email = email
        
    def sign_in(self):
        print("logged in")
        
    def attack(self):
        print("do nothing")
        
class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email)
        self.name = name
        self.power = power
        
    def attack(self):
        User.attack(self)
        print(f"attacking with power of {self.power}")
        
class Archer(User):
    def __init__(self, name, num_arrows, email):
        User.__init__(self, email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows: arrows left - {self.num_arrows}")
        
def player_attack(player):
    player.attack()   
wizard1 = Wizard("Merlin", 50, 'ibou@gmail.com')
archer1 = Archer("Archer", 20, 'sognu@gmail.com')
print(wizard1.email)
print(dir(archer1.email))
