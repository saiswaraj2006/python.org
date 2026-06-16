import logic
result=logic.add(10,20)
print(result)
print(logic.sub(10,20))
print(logic.multiplication(10,20))
#now my division method has two ways 
#1. without a=0 then
print(logic.division(10,20))
#output=0.5
#now 2. using a=0 then
print(logic.division(0,20))
#output=0 
#because it goes to else block 
