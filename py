class Car:
    def start(self):
        print("Car is started.....")
    
    def stop(self):
        print("Car is stopped.....")
        
    def drive(self):
        print("Car is driving.....")


class ToyotaCar(Car):
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand


car = ToyotaCar("Land Cruiser", "Toyota")
car = ToyotaCar("Previous", "Toyota")

print(car.name)
print(car.brand)

car.start()
car.drive()
car.stop()

           