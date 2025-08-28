#1

# products=[]
# n=1

# while True:
#     question=f"enter product {n}: "
#     product=input(question)
#     products.append(product)
#     respose=input("will you add a product again?  (yes,no): ")
#     if respose.lower()=="yes":
#         n=n+1
#         continue
#     else:
#         break

# print("\nYour products:")
# print(products)


#2

# e_shop={}
# sign=True
# while sign:
#     product=input("enter the name of product: ")
#     price=input(f"enter the price of {product}: ")
#     e_shop[product]=float(price) #key value, product price

#     back=input("will you add a product again? (yes/no): ")
#     if back.lower()=="no":
#         sign=False

# for product, price in e_shop.items():
#     print(f"\nThe price of {product} is {price}")



#3

# orders = ['olma','anjir','uzum','qovun']
# products = {'olma':20000,
#                'shaftoli':25000,
#                'tarvuz':18000,
#                'uzum':22000}

# while orders:
#     order = orders.pop()
#     if order in products.keys():
#         price = products[order]
#         print(f"{order.title()} - {price} som")
#     else:
#         print(f"We do not have {order}")





