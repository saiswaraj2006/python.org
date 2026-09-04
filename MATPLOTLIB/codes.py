#importing package 
import matplotlib.pyplot as plt
'''
x = [1, 2, 3, 4, 5]# X-axis values
y = [2, 4, 6, 8, 10]# Y-axis values
#adding labels
plt.plot(x, y,marker="o",color="blue",linestyle='--')# Create a line plot
plt.title("Simple Line Plot")

plt.xlabel("X values")
plt.ylabel("Y Values")
#plt.show()'''
#now adding labels and title

#now BAR CHART
#categories=["Valid Rows","Invalid Rows"]
#counts=[7,3]
#plt.bar(categories,counts,color=["green","red"])
#plt.title("Validation Results")
#plt.ylabel("Row Count")
#plt.show()
'''
#PIE CHART
labels=["Valid","Invalid"]
sizes=[7,3]
colors=["yellow","brown"]
plt.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%',wedgeprops={"edgecolor":"black"})#wedge props means border
#the parameter autopct='%1.1f%%' controls how the percentage labels are displayed on each slice
# autopct=automatic percentage
# to print percentage value on each slice
# '%=placeholder for a value
# 1.1f means one digit before the decimal, ex=25.0% like that
# %%= prints a literal percentage sign  
plt.title("Validation Results")
plt.show()'''
'''
A pie chart with percentages (autopct)

Black outlines around each slice

A legend outside the chart so labels don't overlap'''
import matplotlib.pyplot as plt

# Data
sizes = [7, 3]
labels = ["Valid Rows", "Invalid Rows"]
colors = ["green", "red"]

# Pie chart with borders
#plt.pie(
#   sizes,
#    labels=None,  # hide labels inside
#    colors=colors,
#   autopct='%1.1f%%',
#    wedgeprops={"edgecolor": "black", "linewidth": 2}  # black borders
#)

# Add legend outside
#plt.legend(labels, loc="upper right", bbox_to_anchor=(1.2, 1))
#plt.title("Validation Results")
#plt.show()

'''
import matplotlib.pyplot as plt

# Data
sizes = [7, 3]
labels = ["Valid Rows", "Invalid Rows"]
colors = ["green", "red"]

# Create a figure with 1 row, 2 columns
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Pie chart on the left
axes[0].pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    wedgeprops={"edgecolor": "black", "linewidth": 2}
)
axes[0].set_title("Validation Results (Pie)")

# Bar chart on the right
axes[1].bar(labels, sizes, color=colors, edgecolor="black")
axes[1].set_title("Validation Results (Bar)")
axes[1].set_ylabel("Row Count")

plt.tight_layout()
plt.show()#it prints piechart and bar chart '''
'''
import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data (like ages)
ages = np.random.randint(18, 60, 100)  # 100 random ages between 18 and 60

# Create histogram
plt.hist(ages, bins=10, color="skyblue", edgecolor="black")#the bin divides the  data
#into 10 intervals (so that i can increase/decrease for more/less )

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()#HISTOGRAM
#above histogram is reveals distributions (normal, skewed, uniform, etc.)
#also essential for data cleaning (spotting outliers)'''


#Scatter plots 
#this plots are perfect for showing relationships between two variables , which is super 
#important in ML 
#eg. : age vs exam score ,feature correlations.
import matplotlib.pyplot as plt
import numpy as np

# Sample data: age vs exam score
#ages = np.random.randint(18, 60, 50)#50 random ages
#scores = np.random.randint(40, 100, 50)#50 random exam scores

#plt.scatter(ages, scores, color="purple", edgecolor="black")

#plt.title("Age vs Exam Score")
#plt.xlabel("Age")
#plt.ylabel("Score")
#plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Sample data: age vs exam score
#ages = np.random.randint(18, 60, 50)        # 50 random ages
#scores = np.random.randint(40, 100, 50)     # 50 random exam scores

# Scatter plot
#plt.scatter(ages, scores, color="purple", edgecolor="black", label="Data Points")

# Fit a simple linear regression line
#m, b = np.polyfit(ages, scores, 1)  # slope (m) and intercept (b)
#plt.plot(ages, m*ages + b, color="orange", linewidth=2, label="Trend Line")
#polyfit means simple linear regression line
#plt.title("Age vs Exam Score with Trend Line")
#plt.xlabel("Age")
#plt.ylabel("Score")
#plt.legend()
#plt.show()
'''
import matplotlib.pyplot as plt
import numpy as np
valid_count=7
invalid_count=3
sizes=[valid_count,invalid_count]
labels=["valid","invalid"]
colors=["yellow","pink"]
ages=np.random.randint(18,60,100)
scores=np.random.randint(40,100,100)
#for 2*2 layout
fig,axes=plt.subplots(2,2,figsize=(10,8))
#for pie chart
axes[0,0].pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    wedgeprops={"edgecolor":"black"}
)
axes[0,0].set_title("Validation Results (pie)")
#for Bar chart
axes[0,1].bar(labels,sizes,color=colors,edgecolor="black")
axes[0, 1].set_title("Validation Results (Bar)")
axes[0, 1].set_ylabel("Row Count")

# Histogram
axes[1, 0].hist(ages, bins=10, color="skyblue", edgecolor="black")
axes[1, 0].set_title("Age Distribution")
axes[1, 0].set_xlabel("Age")
axes[1, 0].set_ylabel("Frequency")

# Scatter plot
axes[1, 1].scatter(ages, scores, color="purple", edgecolor="black")
axes[1, 1].set_title("Age vs Score")
axes[1, 1].set_xlabel("Age")
axes[1, 1].set_ylabel("Score")

plt.tight_layout()
plt.savefig("mini dashboard.svg")
plt.show()'''


'''
import turtle
#the turtle library is used for graphics and drawing

screen = turtle.Screen()
screen.bgcolor("BEIGE")

pen = turtle.Turtle()
pen.color("BROWN")
pen.pensize(3)       # thicker, smoother lines
pen.speed(5)         # visible animation (1 slow → 10 fast, 0 instant)

for i in range(36):
    pen.circle(100)#draws a circle with radius 100
    pen.left(10)#rotates the pen 10 degrees left after each circle

screen.mainloop()
'''
'''
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# Plot
plt.plot(x, y, color="blue", marker="D", linestyle="--", label="Data Line")
#marker="D" -> draws diamond shapes at each point on the line 
#label="Data line" means it is used in the legend box to show the line and understood to the user or viewers
#color="blue" use to line connecting the points will be blue 
# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title(" Simple Line Plot")
# Show legend
plt.legend()
# Display
plt.show()
'''

import matplotlib.pyplot as plt

categories = ["Valid", "Invalid", "Missing"]
values = [50, 30,16]

plt.bar(categories, values, color=["green", "red" ,"lightblue"], edgecolor="black")

plt.title("Bar Chart Example")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

#pie chart
import matplotlib.pyplot as plt
labels=["Pass","Fail","Absent"]
numbers=[87,9,4]
colors=["lightgreen","Red","Brown"]
plt.pie(
    numbers,
    labels=labels,
    labeldistance=1.1, #moves labels printing distance to backwards 
    colors=colors,
    autopct="%1.1f%%",
     #shows the percentage automatically
    pctdistance=0.85, #places labels outward
    startangle=90,#starts with 90 degrees angle
    wedgeprops={"edgecolor":"black"}#outline for slices is black
)
plt.legend(loc="lower right",fontsize=12,title="exam results",bbox_to_anchor=(1.3,0.8))
plt.title("Pie chart")
plt.show()
