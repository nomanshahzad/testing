a = [[3,6,3],
    [3 ,7,4],
    [2 ,4,6]]

trace = 0
 
for i in range(len(a)):
    trace += a[i][i] 

print(trace)