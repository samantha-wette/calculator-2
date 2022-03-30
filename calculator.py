"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
#take user input
user_equation = input("Please enter your equation. Start with the operator followed by a space and number(s).")
#tokenize input
tokens = user_equation.split(' ')

#go through the first value in the list, check with a conditional 
    # to know which function to use
token = tokens[0]
while token != "q":
 #   for token in tokens:
    num1 = int(tokens[1])
    if len(tokens) == 3:
        num2 = int(tokens[2])

    if token == "+": #add
        print(add(num1, num2))

    elif token == "-": #sub
        print(subtract(num1, num2))

    elif token == "*": #multiply
        print(multiply(num1, num2))

    elif token =="/":
        print(divide(num1,num2))

    elif token == "square": #square
        print(square(num1))

    elif token == "cube": #cubed
        print(cube(num1))

    elif token == "pow": #power
        print(power(num1, num2))

    elif token == "mod": #modulo/remainder
        print(mod(num1, num2))
    
    user_equation = input("Please enter your equation. Start with the operator followed by a space and number(s).")
    tokens = user_equation.split(' ')
    token = tokens[0]