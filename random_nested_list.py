# Creation of a random nested list when n1 is the outer & n2 is the inner list

import random
lst = []
new_lst = []

n1 = int(input("Enter outer list length: "))
n2 = int(input("Enter inner list length: "))
for i in range(n1):
    for j in range(n2):
        value = random.randint(1,100)
        if len(new_lst) <= n2:
            new_lst.append(value)
            if len(new_lst) == n2:
                lst.append(new_lst.copy())
                new_lst.clear()
                
print(lst)
