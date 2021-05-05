# Program to transpose a matrix using a nested loop

a = [[7,7],
    [5 ,5],
    [8 ,8]]


rows, cols = (len(a[0]),len(a) )
result = [[0]*cols]*rows
print(result)


for i in range(len(a)):
   # iterate through columns
    for j in range(len(a[0])):
        result[j][i] = a[i][j]


print(result)
    
