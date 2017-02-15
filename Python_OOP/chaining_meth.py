class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print self.price, self.max_speed, self.miles
        return self
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0;
        return self

mountain_bike = Bike(800, "30mph")
bmx_bike = Bike(770, "25mph")
road_bike = Bike(9990, "45mph")

mountain_bike.ride().ride().ride().reverse().displayInfo()
