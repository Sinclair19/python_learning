class Restaurant:
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"The restaurant'name is {self.name}. The restaurant'type is {self.type}." )
    
    def open_restaurant(self):
        print("The restaurant is opening")
    
    def set_number_served(self,newnum):
        self.number_served = newnum
    
    def increment_number_served(self,increase):
        self.number_served += increase

restaurant_a = Restaurant('rost','french')
print(restaurant_a.name)
print(restaurant_a.type)
restaurant_a.describe_restaurant()
restaurant_a.open_restaurant()

restaurant_a.set_number_served(500)
print(restaurant_a.number_served)
restaurant_a.increment_number_served(50)
print(restaurant_a.number_served)