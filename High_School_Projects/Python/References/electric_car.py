class Car():
    '''A simple attempt to represent a car.'''
    def __init__(self, make, model, year):
        '''Initialize attributes to describe a car.'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name.'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        #print a statement showing the car's mileage.
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        #set the odometer reading to the given value.
        #reject the change if it attemps to roll the odometer back.
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        #Add the amount to the odometer reading.
        self.odometer_reading += miles

class ElectricCar(Car):
    #Represent aspects of a car, specific to electric vehicles.
    def __init__(self, make, model, year):
        #initalize attributes of the parent class.
        #then initalize attributes specific to an electric car.
        super().__init__(make, model, year)
        self.battery_size = 70
    def describe_battery(self):
        #battery size
        print("This car has a " + str(self.battery_size) + "-KWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()