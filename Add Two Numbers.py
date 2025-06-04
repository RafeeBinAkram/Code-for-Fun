#Two lists were taken & their values have been added and printed as list at output.

lst1 = [2,3,4,6,5,7]
lst2 = [5,6,7,8,7,5]
lst3 = []

a=str(0)
for x in lst1:
    a = a+str(x)
num1 = int(a)

b=str(0)
for y in lst2:
    b = b+str(y)
num2 = int(b)

num = str(num1+num2)

for x in num:
    lst3.append(int(x))

print(lst3)
