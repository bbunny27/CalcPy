x = input("Enter your first number: ")
y = input("Enter your Second Number: ")
print("1 = Add")
print("2 = Subtract")
print("3 = Multiply")
print("4 = Divide")
z = input("Enter your Function Number: ")

x = int(x)
y = int(y)
z = int(z)

def calc(x,y,z):
    answer = 0
    if z == 1:
        answer = x + y
    elif z == 2:
        answer = x - y
    elif z == 3:
        answer = x * y
    else:
        answer = x / y
    return answer

print("Your Answer is:", calc(x,y,z))
