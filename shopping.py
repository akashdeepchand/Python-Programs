print()
print("--------------Welcome to Relience Fresh--------------")
print()
list=['oil','toothpaste','cream']
print("Stock item")
print()

for i in list:
    print("-",i)
print()
item=input("What would you like to choose?....... ")

if(list.__contains__(item)):
    print(f'item bought : {item}')
    print()
    list.remove(item)
else:
    print("sorry for inconvenience")

print('Available Items : ')
for i in list: 
    print('-',i)
print()
print("-----Thank you-----")
print("Have a nice Day!")
print()
