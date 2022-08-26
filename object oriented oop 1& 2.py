# object oriented programming

class PlayerCharactor:
    #class object attribute
    membership = True
    def __init__(self,name,age):
        self.name = name   #attributes
        self.age = age

    def run(self):
        print("run")
        return "done"

    @classmethod                             #no need  instantiat class
    def adding_things(cls, num1 ,num2):
        return num1 + num2

    @staticmethod
    def adding_things(num1, num2):
        return num1 + num2




#player = PlayerCharactor("vinayak", 21)

print(PlayerCharactor.adding_things(1,5))


# 4 pillors of oop
# 1. encapsulation
 # 2. abstractio
 # 3. inharatance
 #4. polymorphism

#private vs public
class PlayerCharactor:
    #class object attribute
    membership = True
    def __init__(self,name,age):
        self._name = name   #convention of making privae by _
        self._age = age

    def run(self):
        print("run")
        return "done"



    @classmethod                             #no need  instantiat class
    def adding_things(cls, num1 ,num2):
        return num1 + num2

    @staticmethod
    def adding_things(num1, num2):
        return num1 + num2


#inharatance
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
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrow - left {self.num_arrows}")

wizard1 = wizard("vinayak", 50)
Archer = Archer("ram", 100)
wizard1.attack()
Archer.attack()

wizard1 = wizard("vinayak", 40)
print(isinstance(wizard1, wizard))
print(isinstance(wizard1, user))
print(isinstance(wizard1, object))


#polymorphism
#for char in [wizard, Archer]
#    char.attack()

#super
#user.__init__(self,email)
# or
#super().__init__( email)

#introspection
print(dir(wizard1))


#dunder  method

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name' : 'yoyo',
            'has_pets' : False

        }
    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __del__(self):
        return print("deleted")

    def __call__(self):
        return("yess")

    def __getitem__(self, i):
        return


action_figure = Toy("red", 10)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())   # call fucnction
print(action_figure['name'])
del action_figure



class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList();


print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(SuperList, list))





