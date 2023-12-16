print("Welcome to SBI atm")
totalamount=80000
print("banking")
print("withdraw")
print("support")
n=str(input("enter the value of n"))
if n=='banking':
    print ("contact SBI bank for passowrd change")
if n=='withdraw':
    amount=int(input("enter the value of amount"))
    if (amount<totalamount) or (amount>2000):
        print("kindly enter you pin")
    if (amount>totalamount) or (amount<2000):
        print("Kindly enter the amount greaterthan 2000 and lessthan 80000")
if n=='support':
    print ("contact SBI bank for support")
z=totalamount-amount
print ('enter the remaing balance',z)
print("thankyou visit again")