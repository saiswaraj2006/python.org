import Module1
import Module2
#result=repeat_x(3)
#here the module functions name is same in both when im imported with their functions
#are namespaced so i get error when i run the above line
print(Module1.repeat_x(3))
print(Module2.repeat_x(3))

