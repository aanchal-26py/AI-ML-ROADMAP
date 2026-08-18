class car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def display(self):
        print("brand=",self.brand)
        print("model=",self.model)
        print("year=",self.year)
a1=car("maruti",2026,15)
a2=car("audi",23,2022)
a1.display()
a2.display()
