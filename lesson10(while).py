# while
# 1

# q="enter any favorite book"
# q+=" (If you done, please enter 'STOP'):".lower()

# while True:
#     book=input(q)
#     if book.lower()=="stop":
#         break

# print("Thank you!")



# #2

# question="How old are you"
# question+="(If you done, enter 'quit' or 'exit'):"

# while True:
#     age=input(question)
#     if age.lower()=="exit" or age.lower()=="quit":
#         break
#     a=int(age)
    
#     if a<7:
#         print("the price ticket is 2000 som")
#     elif a<=18:
#         print("the price ticket is 3000 som")
#     elif a<=65:
#         print("the price ticket is 10000 som")
#     else:
#         print("ticket is free for you")


#3
#with flag

# question="How old are you"
# question+="(If you done, enter 'quit' or 'exit'):"
# sign=True
# while sign:
#     age=input(question)
#     if age.lower()=="exit" or age.lower()=="quit":
#         sign=False
#     a=int(age)
#     21
#     if a<7:
#         print("the price ticket is 2000 som")
#     elif a<=18:
#         print("the price ticket is 3000 som")
#     elif a<=65:
#         print("the price ticket is 10000 som")
#     else:
#         print("ticket is free for you")


#4

question="How old are you"
question+="(If you done, enter 'quit' or 'exit'):"
value=''

while value.lower()!="exit" or value.lower()!="quit":
    value=input(question)
    
    if value.lower()!="exit" or value.lower()!="quit":
        a=int(value)

        if a<7:
            print("the price ticket is 2000 som")
        elif a<=18:
            print("the price ticket is 3000 som")
        elif a<=65:
            print("the price ticket is 10000 som")
        else:
            print("ticket is free for you")






