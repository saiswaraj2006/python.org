import pandas as pd
from sklearn.linear_model import LinearRegression
#giving the example dataset:
data=pd.DataFrame({
    "Hours_Studied":[1,2,3,4,5,6],
    "Exam_Score":[56.5,59.6,66.9,74.6,74.3,79.3]
})
x=data[["Hours_Studied"]]
y=data["Exam_Score"]
model=LinearRegression()
model.fit(x,y)
#for prediction of 7 hours of study
print("predicted score:",model.predict(pd.DataFrame({"Hours_Studied":[7]}))[0])
#output=predicted score: 85.11333333333334


