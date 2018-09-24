#python 3.5.2

'''

Iterators are everywhere in Python. They are elegantly implemented within for loops, comprehensions, generators etc. but hidden in plain sight.

Iterator in Python is simply an object that can be iterated upon. An object which will return data, one element at a time.

Technically speaking, Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol.

An object is called iterable if we can get an iterator from it. Most of built-in containers in Python like: list, tuple, string etc. are iterables.

The iter() function (which in turn calls the __iter__() method) returns an iterator from them.
'''

# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

## iterate through it using next() 

#prints 4
print(next(my_iter))

#prints 7
print(next(my_iter))

## next(obj) is same as obj.__next__()

#prints 0
print ( next(my_iter) )

print( '-'*20 )

'''
Building Your Own Iterator in Python

Building an iterator from scratch is easy in Python. We just have to implement the methods __iter__() and __next__().

The __iter__() method returns the iterator object itself. If required, some initialization can be performed.

The __next__() method must return the next item in the sequence. On reaching the end, and in subsequent calls, it must raise StopIteration.

Here, we show an example that will give us next power of 2 in each iteration. Power exponent starts from zero up to a user set number.

'''

class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
            
            
a = PowTwo(4)
i = iter(a)
print ( next(i) )

print( '-'*20 )

'''
OUTPUT: 

4
7
0
--------------------
1
--------------------
'''






