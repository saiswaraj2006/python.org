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
import matplotlib.pyplot as plt

# Scatter plot of actual data points
plt.scatter(x, y, color="blue", label="Actual data")

# Regression line (fitted by the model)
plt.plot(x, model.predict(x), color="red", label="Regression line")


plt.scatter([7], model.predict(pd.DataFrame({"Hours_Studied":[7]})), 
            color="green", s=100, marker="o", label="Prediction (7 hrs)")

# Labels 
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Linear Regression: Hours Studied vs Exam Score")
plt.legend()
#this legend is a small box that explains what each color/marker in the plot represents
#like Blue dot="Actual Data" like that for easy understand
plt.grid(True, color="orange")
#here grid is horizontal and vertical lines across the plot at background
plt.show()



