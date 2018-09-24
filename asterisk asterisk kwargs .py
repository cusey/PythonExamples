#python 3.5.2

'''
Python **kwargs

Python passes variable length non keyword argument to function 
using *args but we cannot use this to pass keyword argument. 
For this problem Python has got a solution called **kwargs, 
it allows us to pass the variable length of keyword arguments 
to the function.

In the function, we use the double asterisk ** before the 
parameter name to denote this type of argument. The arguments
 are passed as a dictionary and these arguments make a 
 dictionary inside function with name same as the parameter 
 excluding double asterisk **.
 '''
 
 
def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)


'''
OUTPUT:

Data type of argument: <class 'dict'>
Lastname is Sharma
Age is 22
Firstname is Sita
Phone is 1234567890

Data type of argument: <class 'dict'>
Email is johnwood@nomail.com
Country is Wakanda
Lastname is Wood
Age is 25
Firstname is John
Phone is 9876543210

'''