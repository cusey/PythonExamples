#python 3.5.2

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