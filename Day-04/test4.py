"""
passing variables into the function, and using the variables to performed the logic and using the return
keyword instead of print in the function, while using the print function at the end by inputting the
value of the variables.

"""
def add(num1,num2):
    add = (num1+num2)
    return(add)
def sub(num1, num2):
    s = (num1-num2)
    return(s)
def mul(num1, num2):
    m = (num1*num2)
    return("value of multipliaction = " + str(m))
def div(num1, num2):
    div = (num1/num2)
    return("value of division = "  +  str(div))
print(add(input))
print(sub(input))
print(mul(input))
print(div(input))