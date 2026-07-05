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
    def __str__(self,color,tyres):
        return f"car=(color={self.color},tyres={self.tyres})"
#now creating new car object
my_car=car(color="Blue",tyres=4)
print(my_car.color)#Blue
print(my_car.tyres)#4

