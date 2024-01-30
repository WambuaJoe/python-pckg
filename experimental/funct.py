# import os

# print("Current directory: ", os.getcwd())

# inheritance in python

class Car():
    """ attempt to represent a car """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odo_reading = 0
        
    def name_desc(self):
        long_name = f"{str(self.year)} {self.make} {self.model}"
        return long_name.title()
    
    def read_odo(self):
        print(f"Car has {str(self.odo_reading)} miles on it")
        
    def update_odo(self, mileage):
        if mileage >= self.odo_reading:
            self.odo_reading = mileage
        else:
            print("Odometer cannot be rolled back")
    
    def incr_odo(self, miiles):
        self.odo_reading += miiles