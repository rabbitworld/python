n = int(input("enter no. to print table:\t"))
m = int(input("enter the no. times to multiply n:\t"))
a = [n*(i+1) for i in range(n)]
print(a)