income = int(input("Enter amount: "))

if income<=10000:
    print("Taxable income = 0 USD")

if income>=20000:
    tx_inc = (10000*0.1)+((income-20000)*0.2)
    print("Taxable income: %d" %(tx_inc))

if income>10000 and income<20000:
    tx_inc = ((income-10000)*0.1)
    print("Taxable income: %d" %(tx_inc))