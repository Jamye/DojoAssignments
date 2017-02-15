# class Human(object):
#     def __init__(self, clan=None):
#       print "New Human!!!"     # when we create a new human, we'll get self as an output
#                                # initialize the clan instance variable by passing in a value
#       self.clan = clan
#       # initialize more attributes that will be the same for all humans
#       self.health = 100
#       self.strength = 3
#       self.intelligence = 3
#       self.stealth = 3
#     def taunt(self):
#       print "You want a piece of me?"
# # create an instance of a human, pass in a clan name
# michael = Human('CodingDojo')
# jimmy = Human('CodingNinjas')


# class Test(object):
#   def __init__(self, phrase='Nothing was passed'):     # set the default value for 'phrase' parameter
#     print "This string was passed in: " + phrase
#     self.phrase = phrase
#
#     test1 = Test('Hello, World!')
#     test2 = Test()
#     print "Test 1 has phrase: '" + test1.phrase + "'"
#     print "Test 2 has phrase, '" + test2.phrase + "'"

# OOP Bike

# define the Bike class
class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print 'Price is: $' + str(self.price)
        print 'Max speed: ' + str(self.max_speed) + 'mph'
        print 'Total miles: ' + str(self.miles) + ' miles'

    def drive(self):
        print 'Driving'
        self.miles += 10

    def reverse(self):
        print 'Reversing'
        # prevent negative miles
        if self.miles >= 5:
            self.miles -= 5

# create instances and run methods
bike1 = Bike(99.99, 12)
bike1.drive()
bike1.drive()
bike1.drive()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike(139.99, 20)
bike2.drive()
bike2.drive()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()
