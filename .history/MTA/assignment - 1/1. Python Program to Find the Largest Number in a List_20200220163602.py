#method 1:
n=int(input("enter no. of elements:\t"))
print("enter the elements:")
list=[int(input()) for num in range(n)]
print("list is ",list)
print("largest no. in the list is ",max(list))


#method 2:
''' n=int(input("enter number of elements:\t"))
a=[]
print("enter the elements:")
for num in range(n):
    a.append(int(input()))
print(a)
print(type(a))
max=list[0]
for x in list:
    if x>max:
        max=x
print(max) '''