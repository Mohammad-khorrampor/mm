def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "error:tagsim bar 0 momken nist"
    return  a / b

print("the four basic operations:")
print("1.add")
print("2.sub")
print("3.mult")
print("4.div")

choice = input("select the desired opration(1/2/3/4)")
num1 = float(input("enter the frist number : ")) 
num2 = float(input("enter the second number : "))

if choice == "1":
    result = add(num1 , num2)
    print("result:", result)
elif choice == "2":
    result = subtract(num1 , num2)
    print("result:", result)
elif choice == "3":
    result = multiply(num1 , num2)
    print("result:", result)
elif choice == "4":
    result = divide(num1 , num2)
    print("result:", result)
else:
    print("invalid opreration")