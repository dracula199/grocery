#!/bin/python3
product=["oil","biscuits","juice"]
catagory=[{"sunflower":50,"refine":40,"fortune":60},{"marie gold":20,"parlage":30,"good day":50},{"cocola": 65, "maza": 60, "fizz": 75}]
cart=[]
price=[]
while(1):
  x=input("press y to enter items into cart or press x to exit")
  if x=="x":
    break
  if x=="y":
    print("Available products are :")
    for i in product:
      print(i)
    p=input("Enter the product name")
    indx=product.index(p)
    for i,j in catagory[indx].items():
      print(i,":",j)
    item=input("enter the catagory name")
    qnty=int(input("How many??"))
    cart.append(item)
    price.append(catagory[indx][item]*qnty)
print(cart,price)