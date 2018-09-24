#python 3.5.2

x = lambda a : a + 10
print(x(5))
print( '-'*20 )

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)

print( '-'*20 )


# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))


print(new_list)

'''
OUTPUT:

15
--------------------
[4, 6, 8, 12]
--------------------
[2, 10, 8, 12, 16, 22, 6, 24]
'''