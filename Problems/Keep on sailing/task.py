# our class Ship
class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    # the old sail method that you need to rewrite
    def sail(self):
        return "{} has sailed!".format(self.name)

    def sail(self, city):
        print(f"The {self.name} has sailed for {city}!")


black_pearl = Ship("Black Pearl", 800)
city = input()
black_pearl.sail(city)
