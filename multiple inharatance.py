#multipal inharatnce

class user():
    def sign_in(self):
        print("logged in")

class wizard(user):
    def __init__(self, name , power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking enemy with {self.power}")


class Archer(user):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def chack_arrows(self):
        print(f" {self.arrows}")

    def run(self):
        print("run really fast")

class HybridBorg(wizard,Archer):
    def __init__(self, name , power , arrows):
        Archer.__init__(self, name, arrows)
        wizard.__init__(self, name, power)

hb1 = HybridBorg('vinayak', 50, 100)
print(hb1.run())
print(hb1.chack_arrows())
print(hb1.attack())
