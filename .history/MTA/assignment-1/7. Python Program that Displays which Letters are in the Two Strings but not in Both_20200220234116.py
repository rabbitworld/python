str1 = input("enter first string:\n")
a=list(str1)
print("first string is:\t--> ",set(str1))
str2 = input("enter second string:\n")
b=list(str2)
print("second string is:\t--> ",set(str2))

for i,j in a,b:
    if a[i] != b[j]:
        print(a[i],b[j])
        

              