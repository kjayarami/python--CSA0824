a=int(input("enter a number"))
for i in range (2,a):
    if(a%i==0):
        print("composite number")
        break
else:
        print("prime number")
