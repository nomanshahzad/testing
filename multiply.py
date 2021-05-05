a = [[2, 5, 7],
    [4, 5, 6],
    [2, 3, 5]]
  
# take a 3x4 matrix    
b = [[3, 2, 4],
    [3, 3, 9],
    [4, 4, 2]]
      
result = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
  
# iterating by row of A
for i in range(len(a)):
  
    # iterating by coloum by B 
    for j in range(len(b[0])):
  
        # iterating by rows of B
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]
  
for r in result:
    print(r)