""" Exponent """
 
base = int(input("Enter Base of Exponent: "))
exp = int(input("Enter Power of Exponent: "))
mult = base

for i in range(1, exp):
    n_mult = mult * base
    mult = n_mult
        
print("Result: %d" %(mult))
