#logistic regression 
#it just classifies pass/fail 
#regression means finding the relationship between input(x) and output(y) to predict
#numbers
import pandas as pd
from sklearn.linear_model import LogisticRegression
data=pd.DataFrame({
    "Hours_Studied":[1,2,3,4,5,6],
    "Pass":[0,0,0,1,1,1] 
    #here 0=Fail,1=Pass
})
x=data[["Hours_Studied"]]
y=data["Pass"]
model=LogisticRegression()
model.fit(x,y)
print("Prediction for 2 hours:",model.predict(pd.DataFrame({"Hours_Studied":[2]}))[0])
print("Prediction for 5 hours:",model.predict(pd.DataFrame({"Hours_Studied":[5]}))[0])