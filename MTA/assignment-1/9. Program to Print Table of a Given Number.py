n = int(input("enter a no. to print table:\t"))
m = int(input("enter the no. of times to multiply n:\t"))
print("table of",n,"is:")
for i in range(1,m+1):
    print(n,"*",i,"=",n*i)