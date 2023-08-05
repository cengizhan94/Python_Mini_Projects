def sum(x, y):
    return x+y


def extract(x, y):
    return x-y


def multiple(x, y):
    return x*y


def division(x, y):
    return x/y 
  
       


print("Please choice your point")

print("1- Sum two numbers")
print("2- extract two numbers")
print("3- multiple two numbers")
print("4- divide two numbers")

choice = input("Your Choice: (1,2,3,4)")

num1 = float(input("First number: "))
num2 = float(input("Second Number: "))

if choice == "1":
    print(f"{num1} + {num2} = {sum(num1,num2)}")
elif choice == "2":
    print(f'{num1} - {num2} = {extract(num1, num2)}')
elif choice == "3":
    print(f'{num1} x {num2} = {multiple(num1,num2)}')
elif choice == "4":
    if(num2 == 0):
        print("A number is not divisible by zero")
    else:
        print(f'{num1} / {num2} = {division(num1,num2)}')

else:
    print("Invalid choice!")
