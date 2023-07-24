# My simple calculator

def add(x, y):
    return x + y


def minus(x, y):
    return x - y


def div(x, y):
    return x / y


def multiply(x, y):
    return x * y


print("\n This is a calculator.")

# How to use 
print("1. Plus (+) ")
print("2. Minus (-) ")
print("3. Divide (/) ")
print("4. Multiplication (*) ")
# print("5. Close/Exit ")

while True:
    print("\nWhat calculation would you like to perform?")
    calc = input("Enter choice(1/2/3/4): ")

    if calc in ('1', '2', '3', '4', '5'):
        try:
            a = float(input("\nEnter a number: "))
            b = float(input("Enter another number: "))
        except ValueError:
            print("Invalid Input. Try again.")
            continue

        if calc == '1':
            print(a, "+", b, "=", add(a, b))
        elif calc == '2':
            print(a, "-", b, "=", minus(a, b))
        elif calc == '3':
            print(a, "/", b, "=", div(a, b))
        elif calc == '4':
            print(a, "*", b, "=", multiply(a, b))

        nxt_calc = input("Do you want to continue? (y/n): ")
        if nxt_calc == 'no':
            break
        else:
            print("\nInvalid entry. Try again.")


# if ch == 1:
#     sum = add(a, b)
#     print(a, "+", b, "=", str(sum))
# elif calc == 2:
#     min = minus(a, b)
#     print(a, "+", b, "=", str(min))
# elif calc == 3:
#     sum = div(a, b)
#     print(a, "+", b, "=", str(sum))
# elif calc == 4:
#     sum = multiply(a, b)
#     print(a, "+", b, "=", str(sum))
# elif calc == 5:
#     print("Invalid operator, Please try again.")
#     exit()
