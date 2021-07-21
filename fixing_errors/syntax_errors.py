#syntax errors
print(1)
int(9)
# int 9 # syntax error, requires the 9 to be inside brackets otherwise it doesnt know its an argument
print(2)
# print 3  same issue, this time it explicitly states you need to use print(3) instead
# a = [a, 2, 3 ) closing paarenthesis error, will point exactly to the bracket that doesnt match

#two main types of errors, syntax and exception

#runtime errors
a = 2
b = "2"
print(int(2.5))
# print[a + b) will throw a syntax error without recognising the typeerror because the intepreter checks for syntax errors first
# print(a + b) type error because int and string cannt be type coerced together
print(str(a) + b)
print(a + int(b))
# either of these will workbecause the types match, but they produce different outcomes
print()

#making the code handle the errors
def divide(x, y):
    return x / y

print(divide(1, 2)) #no error
# print(divide(1, 0))  error and will crash program

def handle_divide(x, y):
    try:
        return x / y
    except:
        print("You can't divide by zero")

print(handle_divide(1, 0)) # this doesnt throw an error because you have used try and except to handle errors within the function
print(handle_divide("what is this", "bob")) #throws the same error cause it is not specific

def specific_divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("You can't divide by zero")

print(specific_divide(1, 0))
print(specific_divide("what is this", "bob")) #this time you dont get the zero error, but a general type error, because you are handling correctly
