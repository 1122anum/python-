
num1 = int(input("enter your first value: "))
operator: int=(input("select operator:( + , - , / , *)  :  "))
num2 = int(input("enter your second value: "))



def calculator( num1, operator, num2):
    if operator == "+":
        return(num1 + num2)
    elif operator == "-" :
        return(num1 - num2)
    elif operator == "/":
        return(num1 / num2)
    elif operator == "*":
        return(num1 * num2)
    else:
        return("invalid operator")

result = calculator(int (num1), operator, int(num2))
print(result)



