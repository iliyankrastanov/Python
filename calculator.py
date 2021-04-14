def Add():
    return "Addition"

def Sub():
    return "Substraction"

def Mult():
    return "Multiplication"

def Div():
    return "Division"

def FloorDiv():
    return "Floor Division"

def Quit():
    return "Quit"
    quit()


if __name__ == "__main__":

    operations = {
        'a': Add,
        's': Sub,
        'm': Mult,
        'd': Div,
        'f': FloorDiv,
        'q': Quit
    }

    operation = input("Operation (a-Addition, s-Substraction, m-Multiplication, d-Division, f-Floor Division, q-Quit):")

    while operation not in ['q']:   
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))


        if operation in 'a':
            print(num1 + num2)

        elif operation in 's':
            print(num1 - num2)

        elif operation in 'm':
            print(num1 * num2)

        elif operation in 'd':
            print(num1 / num2)
        
        elif operation in 'f':
            print(num1 // num2)
            
        else:
            print("Invalid Operation, choose a valid one!")

        operation = input("Select operation you would like to perform: ")

    else: 
            print("Calculator off!")




  
