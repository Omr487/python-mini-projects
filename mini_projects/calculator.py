num1 = float(input("enter your first number: "))
num2 = float(input("enter your second number: "))
operator = input("enter your operator (+ - * / ): ")
if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(round(num1/num2,3))
else:
    print(f"{operator} is not valid")




