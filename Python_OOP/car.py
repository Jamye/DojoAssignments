class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0

    def displayInfo(self):
        print "Price: ", self.price
        print "Speed: ", self.speed, "mph"
        print "Fuel: ", self.fuel
        print "Mileage: ", self.mileage, "mpg"
        if self.price > 10000:
            print "Tax: 0.15"
        else:
            print "Tax: 0.12"
        return

car1 = Car(2000, 35, "Full", 15)
car2 = Car(2000, 5, "Not full", 105)
car3 = Car(2000, 15, "Kind of full",95)
car4 = Car(2000, 25, "Full", 25)
car5 = Car(2000, 45, "Empty", 25)
car6 = Car(20000000, 35, "Empty", 15)


car1.displayInfo()
car2.displayInfo()
car3.displayInfo()
car4.displayInfo()
car5.displayInfo()
car6.displayInfo()
