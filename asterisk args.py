#python 3.5.2

'''
Python *args

As in the above example we are not sure about the number of arguments that can 
be passed to a function. Python has *args which allow us to pass the variable 
number of non keyword arguments to function.

In the function, we should use an asterisk * before the parameter name to
pass variable length arguments.The arguments are passed as a tuple and 
these passed arguments make tuple inside the function with same 
name as the parameter excluding asterisk *.
'''

def adder(*num):
    sum = 0
    
    for n in num:
        sum = sum + n

    print("Sum:",sum)

adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)

'''
OUTPUT:
Sum: 8
Sum: 22
Sum: 17
'''

