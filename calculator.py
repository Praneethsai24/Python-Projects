# import operator


# num1=int(input('Enter the first number: '))
# num2=int(input('Enter the second number: '))
# operator=input('Select operator (+,  -,  *, %)')
# if operator == '+':
#     addition=num1+num2
#     print(addition)
# elif operator == '-':
#     sub=num1-num2
#     print(sub)
# elif operator == '*':
#     multi = num1*num2
#     print(multi)
# elif operator== '%':
#     div=num1%num2
#     print(div)
# else: 
#     print('Invalid Operator')


import operator

while True:
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    operator=input('select the operator(+, -, *, %) or "q" to quit: ')

    if operator=='+':
        print(num1+num2)
    elif operator=='-':
        print(num1-num2)
    elif operator=="*":
            print(num1*num2)
    elif operator.lower()=="q":
        print("Quitting..")
        break
    else:
        print("invalid operator!!")