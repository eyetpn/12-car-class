class Car:
    def __init__(self, gas_level):
        self.gas_level = gas_level

    def get_gaslevel(self):
        return self.gas_level

    def add_gas(x):
        new_gaslevel = x + gas_level
        return new_gaslevel
    
    def fill_up(y):
        if y < 13:
            new_y = 13- y
            return new_y
        else: 
            return 0

x = Car(14.0)
print (x.fill_up())
