num1 = int(input("1st number "))
num2 = int(input("2nd number "))
sign = input("which sign(+,-,/,x or *)")

if sign == "+":
    print(num1+num2)
elif sign == "-":
    print(num1-num2)
elif sign == "/":
    print(num1/num2)
elif sign == "x" or sign == "X":
    print(num1*num2)
else:
    print("wrong input please try again")
