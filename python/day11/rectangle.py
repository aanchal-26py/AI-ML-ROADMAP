class rectangle:
    def perimeter(self,l,b):
        self.peri=2*(l+b)
        print("perimeter=",self.peri)
    def area(self,l,b):
        self.area=l*b
        print("Area=",self.area)
l=int(input("Enter length="))
b=int(input("Enter breadth="))
a=rectangle()
a.perimeter(l,b)
a.area(l,b)