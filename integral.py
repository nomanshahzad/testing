def f(x):
    return (2.178**(x**2))
a=int(input("Enter Lower Limit: "))    
b=int(input("Enter Upper limit: "))    
n=int(input("Enter Number Of intervals: "))    
width=(b-a)/n
i=0
Area=0
while(i<=n+1):
    Area=f(a+(width*i))*width+Area
    i=i+1
print(Area)