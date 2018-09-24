#python 3.5.2
'''
Sometimes we only want part of a Python list. Maybe we only want the first few elements; 
maybe we only want the last few. Maybe we want every other element!

List slicing allows us to access elements of a list in a concise manner. The syntax 
looks like this:

[start:end:stride]

Where  start  describes where the slice starts (inclusive),  end  is where it ends 
(exclusive), and  stride  describes the space between items in the sliced list.
 For example, a stride of 2 would select every other item from the original list 
 to place in the sliced list.(Refer to the index).
'''

to_five = ['A', 'B', 'C', 'D', 'E']

print ('1', to_five[3:] )

print ('2', to_five[:2] )

print ('3', to_five[::2] )

print ('4',  to_five[::-1] )


'''
OUTPUT:

1 ['D', 'E']
2 ['A', 'B']
3 ['A', 'C', 'E']
4 ['E', 'D', 'C', 'B', 'A']


'''

