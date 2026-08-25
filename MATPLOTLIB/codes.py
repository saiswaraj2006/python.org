#importing package 
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]# X-axis values
y = [2, 4, 6, 8, 10]# Y-axis values

plt.plot(x, y)# Create a line plot
plt.savefig("simplelinegraph.svg")
plt.show()# Displays the plot
