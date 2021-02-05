def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    if b!=0:
        return a/b
    else:
        return "Error"
def app():
    a1=input("Please enter a: ")
    b1=input("Please enter b: ")
    if a1.isdigit() and b1.isdigit():
        a=float(a1)
        b=float(b1)
        print("Addition: ",add(a,b))
        print("Subtraction: ",sub(a,b))
        print("Multiplication: ",multi(a,b))
        print("Division: ",div(a,b))
    else:
        print("Error, Please enter numbers")
app()