class Car:
    def start(self):
        print("Car is started.....")
    
    def stop(self):
        print("Car is stopped.....")
        
    def drive(self):
        print("Car is driving.....")


class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name


car1 = ToyotaCar("Land Cruiser")
car2 = ToyotaCar("Previous")

print(car1.name)

car1.start()
car1.drive()
car1.stop()