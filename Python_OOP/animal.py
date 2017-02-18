

class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = 100

    def walk(self):
        print "Name: " + self.name
        self.health -= 1
        print "Health: " + str(self.health)
        return

    def run(self):
        print "Name: " + self.name
        self.health -= 5
        print "Health: " + str(self.health)
        return

    def displayHealth(self):
        print "Name: " + self.name
        print "Health: " + str(self.health)

        return
animal1 = Animal("Penelo", 100)

# animal1.walk()
# animal1.walk()
# animal1.walk()
# animal1.run()
# animal1.run()
# animal1.displayHealth()


class Dog(Animal):
    def __init__(self, name, health):
        self.name = name
        self.health = 150

    def pet(self):
        print "Name: " + self.name
        self.health += 5
        print "Health: " + str(self.health)
        return

dog1 = Dog("Lucky", 150)

# dog1.walk()
# dog1.walk()
# dog1.walk()
# dog1.run()
# dog1.run()
# dog1.pet()
# dog1.displayHealth

class Dragon(Animal):
    def __init__ (self, name, health):
        self.name = name
        self.health = 170

    def fly(self):
        print "Name: " + self.name
        self.health -= 10
        print "Health: " + str(self.health)
        return

dragon1 = Dragon("Fuegur", 170)

dragon1.walk()
dragon1.walk()
dragon1.walk()
dragon1.run()
dragon1.fly()
dragon1.fly()


#     from human import Human
# class Wizard(Human):
#   def heal(self):
#     self.health += 10
# class Ninja(Human):
#   def steal(self):
#     self.stealth += 5
# class Samurai(Human):
#   def sacrifice(self):
#     self.health -= 5
