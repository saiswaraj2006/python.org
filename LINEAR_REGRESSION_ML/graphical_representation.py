import matplotlib.pyplot as plt

# Scatter plot of actual data points
plt.scatter(x, y, color="blue", label="Actual data")

# Regression line (fitted by the model)
plt.plot(x, model.predict(x), color="red", label="Regression line")

# Highlight prediction for 7 hours
plt.scatter([7], model.predict(pd.DataFrame({"Hours_Studied":[7]})), 
            color="green", s=100, marker="o", label="Prediction (7 hrs)")

# Labels and legend
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Linear Regression: Hours Studied vs Exam Score")
plt.legend()
plt.grid(True)
plt.show()
