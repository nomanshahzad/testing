# first Matrix 
a = [[3,6,3],
    [3 ,7,4],
    [2 ,4,6]]
 

 # second Matrix 
b = [[9,3,7],
    [2,5,4],
    [3,2,6]]
 
 
result = [[0,0,0],
        [0,0,0],
        [0,0,0]]


# iterate through rows
for i in range(len(a)):  
# iterate through columns
    for j in range(len(a)):
        result[i][j] = a[i][j] + b[i][j]
 
#  printing result
for r in result:
    print(r)