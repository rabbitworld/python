n=int(input("enter no. of elements\n"))
list=[int(input()) for num in range(n)]
print(list)

x=max(list)
list.remove(max(list))
y=max(list)
print("second largest no. is ",y)
list.append(x)

print(list)