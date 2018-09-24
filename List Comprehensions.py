#python 3.5.2

'''
List comprehensions provide a concise way to create lists. Common applications are to make
 new lists where each element is the result of some operations applied to each member of
another sequence or iterable, or to create a subsequence of those elements that satisfy a 
certain condition.
'''

print ( [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y] )
print(  '-'*20)

print( [i**2 for i in range(1,12) if i % 2 == 0 ] )
print(  '-'*20)

'''
OUTPUT:

[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
--------------------
[4, 16, 36, 64, 100]
--------------------
'''
