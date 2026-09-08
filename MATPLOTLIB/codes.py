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
'''
import matplotlib.pyplot as plt

categories = ["Valid", "Invalid", "Missing"]
values = [50, 30,16]

plt.bar(categories, values, color=["green", "red" ,"lightblue"], edgecolor="black")

plt.title("Bar Chart Example")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()'''
'''
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
'''
'''
import matplotlib.pyplot as plt
import numpy as np

# Generate random exam scores
scores = np.random.randint(40, 100, 50)

plt.hist(scores, bins=10, color="skyblue", edgecolor="blue")
plt.title("Day 3: Histogram of Exam Scores")
plt.xlabel("Score Range")
plt.ylabel("Number of Students")
plt.show()
#here above bins=10 means divides scores into 10 ranges
#edgecolor="blue" means outlines bars for clarity
# Example: Study hours vs exam marks
study_hours = [2, 3, 4, 5, 6, 7, 8]
marks = [50, 55, 60, 65, 70, 80, 85]

plt.scatter(study_hours, marks, color="red", marker="o", label="Data Points")
plt.title("Day 3: Scatter Plot - Study vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.legend()
plt.show()'''
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
# Create 2 subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot(x, y1, color="blue")
ax1.set_title("Sine Wave")
ax2.plot(x, y2, color="red")
ax2.set_title("Cosine Wave")
fig, axs = plt.subplots(2, 2, figsize=(8, 6))

axs[0, 0].plot(x, y1, color="blue")
axs[0, 0].set_title("Sine")

axs[0, 1].plot(x, y2, color="red")
axs[0, 1].set_title("Cosine")

axs[1, 0].bar([1,2,3], [3,5,7], color="green")
axs[1, 0].set_title("Bar Chart")

axs[1, 1].pie([40,30,30], labels=["A","B","C"], autopct="%1.1f%%")
axs[1, 1].set_title("Pie Chart")



plt.tight_layout()
plt.show()#the plot has two subplots ax1 has sine and ax2 has cosine waves it will be shown aas output
'''
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

# Define data first
x = np.linspace(0, 10, 100)#100 points between 0 and 10
y1 =np.sin(x)# sine values
y2 =np.cos(x)#cosine values

# Create figure with GridSpec
fig = plt.figure(figsize=(8, 6))
gs = gridspec.GridSpec(2, 2)

ax1 = fig.add_subplot(gs[0, :])#top row full width
ax2 = fig.add_subplot(gs[1, 0])#bottom left
ax3 = fig.add_subplot(gs[1, 1])#bottom right
#Plot data
ax1.plot(x, y1, color="blue", label="sin(x)")
ax1.set_title("Wide Sine Plot")
ax1.legend()
ax2.scatter(x, y1, color="purple", marker="o")
ax2.set_title("Scatter")
ax3.hist(y1, bins=20, color="orange", edgecolor="black")
ax3.set_title("Histogram")
#Add shared title
fig.suptitle("Day 4: GridSpec Dashboard", fontsize=14, fontweight="bold")
plt.tight_layout(rect=[0, 0, 1, 0.95])#leave space for suptitle
plt.show()


