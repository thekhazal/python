#
# Example file for working with functions
#

# define a basic function
def func1():
    print("I am a function")
    return "haci"

# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " test ", arg2)
    

# function that returns a value
def func3():
    return "abok"

# function with default value for an argument
def power(num,x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result



#function with variable number of arguments
def multiAdd(*args):
    result = 0
    for x in args:
        result = result + x
    return result


func1()
print (func1())
print(func1)

a="andra"
b="tredje"
func2("första",a )
print (func2(a,b))
print (func2)

print (power(2))
print (power(2,3))
print (power(x=3, num=2))

print (multiAdd(2,3,4,5,6,7))