"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


user_equation = input("Please enter your equation. Start with the operator followed by a space and number(s).")

#tokenize input

tokens = user_equation.split(' ')

for token in tokens:
    if token == "q":
        break
    if token == "+":
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        print(add(num1, num2))



#go through the first value in the list, check with a conditional 
# to know which function to use
#if the first token is q, then we quit

while tokens[0] != "q":
    num1 = int(tokens[1])
    num2 = int(tokens[2])
    

#add
    if tokens[0] == "+":
        print(add(num1, num2))
        user_equation = input("Please enter your equation. Start with the operator followed by a space and number(s).")
        tokens = user_equation.split(' ')
#subtract
    if tokens[0] == "-":
        print(subtract(num1, num2))

#multiply
    if tokens[0] == "*":
        print(multiply(num1, num2))

#divide
    if tokens[0] == "/":
        print(divide(num1, num2))

#square

#cube

#power

#mod

#loop input forever if not broken by q
user_equation = input("Please enter your equation. Start with the operator followed by a space and number(s).")
tokens = user_equation.split(' ')
##