def addition(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

print("Select operation:")
print("1. +")
print("2. -")
print("3. *")
print("4. /")

def cal():
    choice = input("Enter choice : ")
    tuple_num = ('1', '2', '3', '4')

    if choice in tuple_num:
        number_1 = float(input("Please insert your first number: "))
        number_2 = float(input("Please insert your second number: "))

        if choice == '1':
            print(f"{number_1} + {number_2} = {addition(number_1, number_2)}")

        elif choice == '2':
            print(f"{number_1} - {number_2} = {subtract(number_1, number_2)}")

        elif choice == '3':
            print(f"{number_1} * {number_2} = {multiply(number_1, number_2)}")

        elif choice == '4':
            result = divide(number_1, number_2)
            print(f"{number_1} / {number_2} = {result}")

    else:
        print("Invalid input. Please enter a valid choice.")

cal()
