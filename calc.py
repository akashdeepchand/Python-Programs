print("Operation Available : ")
print("1 for Addition")
print("2 for Subtraction")
print("3 for Multiply")
print("4 for Division")

n1 = int(input("Enter first Number : "))
n2 = int(input("Enter Second Number : "))
op = int(input("Enter Operation : "))

if(op==1):
    print(f'{n1+n2}')
elif(op==2):
    print(f'{n1-n2}')
elif(op==3):
    print(f'{n1*n2}')
elif(op==4):
    print(f'{n1/n2}')        
else:
    print("Invalid operation")
