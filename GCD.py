#Accepts two number as input and prompts the GCD


n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))

lst1 = []
lst2 = []

for i in range(1, n1+1):
    if n1%i==0:
        lst1.append(i)
        
for j in range(1, n2+1):
    if n2%j == 0 :
        lst2.append(j)
        
lst1.sort(reverse=True)
lst2.sort(reverse=True)

for i in lst1:
    if i in lst2:
        print("GCD is: %d" %(i))
        break

        
        



