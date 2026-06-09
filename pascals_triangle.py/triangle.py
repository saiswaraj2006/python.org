def pascals_triangle(n):
    triangle=[]
    if n<=0:
        print("n value must be positive integer")
    else:
        for i in range(n):
            row=[1]*(i+1)
            for j in range(1,i):
                row[j]=triangle[i-1][j-1]+triangle[i-1][j]
            triangle.append(row) 
    for row in triangle:
        print(" ".join(map(str, row)))
pascals_triangle(5)
'''
output=
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
'''