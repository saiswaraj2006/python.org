#instead of '+' i can use '__add__()'
#using len() method is same as __len__()
t1=[32222,42,1.0,4,3,2]
print(t1.__len__())
#6

#__str__()->used for the user_friendly output
class car:
    def __init__(self,color,tyres):
        self.color=color
        self.tyres=tyres
    def __repr__(self):
        return f"car=(color={self.color},tyres={self.tyres})"
    def __str__(self):
        return f"{self.color} {self.tyres}"
#now creating new car object
my_car=car('Blue',4)
print(my_car.color)#Blue
print(my_car.tyres)#4
print(str(my_car))#Blue 4
print(repr(my_car))#car=(color=Blue,tyres=4)
#__repr()__
#the representation method used for developer_friendly output in debugging

#and without typing the __str__ i can use direct typing like
print(my_car)
#Blue 4
#because print() calls __str__
print(end="")

#Arithmetic operators
class Items:
    def __init__(self,name,value):
        self.name=name
        self.value=value
    def __sub__(self, other):
        if isinstance(other,Items) and self.name==other.name:
            return Items(self.name,self.value - other.value)
        raise ValueError("cannot sub items of different types")
    def __add__(self,other):
        if isinstance(other,Items) and self.name==other.name:
            return Items(self.name,self.value + other.value)
        raise ValueError("cannot add items of different types")
    def __gt__(self, other):
        if isinstance(other,Items) and self.name==other.name:
            return self.value > other.value
        else:
            return ValueError("cannot compare the items of different types.")
    def __lt__(self, other):
        if isinstance(other,Items) and self.name==other.name:
            return self.value < other.value
        else:
            return ValueError("cannot compare the items of different types.")
    def __repr__(self):
        return f"Items(name='{self.name}', value={self.value})"
my_Items1=Items(name="Toyota",value=50) 
my_Items2=Items(name="Tata",value=55) 
my_Items3=Items(name="Tesla",value=70)
my_Items4=Items(name="Toyota",value=64)
my_Items5=Items(name="Tata",value=34)
#comparing the which item will be greater 
print(my_Items1 < my_Items4)#True
#if i tried with different items
print(my_Items1 < my_Items2)
#it returns value error
#output:
#cannot compare the items of different types.
sum=my_Items2 + my_Items5
print(sum)
#Items(name='Tata', value=89)
print(my_Items2 - my_Items5)
#Items(name='Tata', value=21)
  


 

 