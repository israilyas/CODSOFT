print("----Simple Calculator----")

def askToConti():
    ask = input("Do you want to continue.. (yes/no): ")
    if ask == "yes":
        return True
    else:
        return False

def sum(num1, num2):
    result = num1 + num2
    print(f"The result is {result}")
    return askToConti()

def sub(num1, num2):
    result = num1 - num2
    print(f"The result is {result}")
    return askToConti()

def multiply(num1, num2):
    result = num1 * num2
    print(f"The result is {result}")
    return askToConti()

def divide(num1, num2):
    result = num1 / num2
    print(f"The result is {result}")
    return askToConti()

while True:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    opr = input("Enter operation (+ - * /): ")

    if opr == "+":
       if not sum(num1, num2):
           break
    elif opr == "-":
       if not sub(num1, num2):
           break
    elif opr == "*":
       if not multiply(num1, num2):
           break
    elif opr == "/":
       if not divide(num1, num2):
           break
    else:
        print("Please enter a valid operation!") 
