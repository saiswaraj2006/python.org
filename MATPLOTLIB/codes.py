#importing package 
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]# X-axis values
y = [2, 4, 6, 8, 10]# Y-axis values
#adding labels
plt.plot(x, y,marker="o",color="blue",linestyle='--')# Create a line plot
plt.title("Simple Line Plot")

plt.xlabel("X values")
plt.ylabel("Y Values")
#plt.show()
#now adding labels and title

#now BAR CHART
#categories=["Valid Rows","Invalid Rows"]
#counts=[7,3]
#plt.bar(categories,counts,color=["green","red"])
#plt.title("Validation Results")
#plt.ylabel("Row Count")
#plt.show()

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
plt.show()
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
plt.show()#it prints piechart and bar chart 

import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data (like ages)
ages = np.random.randint(18, 60, 100)  # 100 random ages between 18 and 60

# Create histogram
plt.hist(ages, bins=10, color="skyblue", edgecolor="black")

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

