print("Enter number 1 : ")
first = input()
first = int(first)
print("Enter number 2 : ")
second = input()
second = int(second)
print("Enter sign : ")
sign = input()

if sign == "+":
    print(first + second)
elif sign == "-":
    print(first - second)
elif sign == "*":
    print(first * second)
elif sign == "/":
    print(first / second)
