class Car:
    max_speed=120 #max speed set to 120 km/hr
    def __init__(self,make,model ,color, speed):
        self.make=make
        self.model=model
        self.color=color
        self.speed=speed
    def accelerate(self, acceleration):
        if self.speed + acceleration<=Car.max_speed:
            self.speed=self.speed +acceleration
        else:
            self.speed=Car.max_speed
    def get_speed(self):
        return self.speed
car1=Car("Toyota","Hyryder","White",0)
car2=Car("Mahindra","Thar","Black",0)
car1.accelerate(100)
car2.accelerate(80)
print(f"{car1.make} {car1.model} is currently at {car1.get_speed()} km/h.")
print(f"{car2.make} {car2.model} is currently at {car2.get_speed()} km/h.")