class car:
    def show(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year
class bike(car):
    def display(self,name,speed,price):
        self.name=name
        self.speed=speed
        self.price=price
obj=bike()
obj.display("shine","ap999",94000)
obj.show("Honda","ak27",2022)
print(obj.name)
print(obj.speed)
print(obj.price)
print(obj.year)




