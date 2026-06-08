class car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        print(f"the brand is {self.brand}, model is {self.model} and the year is {self.year}")
#objects
car1 = car("toyota","corolla",2020)
car1.display_info()