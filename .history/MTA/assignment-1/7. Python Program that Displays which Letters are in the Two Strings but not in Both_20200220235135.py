str1 = input("enter first string:\n")
a=set(str1)
print("first string is:\t--> ",set(str1))
str2 = input("enter second string:\n")
b=set(str2)
print("second string is:\t--> ",set(str2))
print("not common",set(str1)^set(str2))