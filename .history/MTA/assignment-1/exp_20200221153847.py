n=int(input("enter no. of elements"))
l=[int(input()) for num in range(n)]
for num in range(n):
    print((lambda: (list(int(num))), lambda: (list(int(num))))[(n%2) == 0]())
#print(x,"\n",y)




    #x.append(int(input()))
    #print ("a" if n%2 == 0 else "b" if n%2 != 0 else "c")