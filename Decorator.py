#python 3.5.2


def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b
    
    
print ( divide(2,5) )
print( '-'*20 )

print ( divide(2,0) )
print( '-'*20 )


'''
OUTPUT:

I am going to divide 2 and 5
0.4
--------------------
I am going to divide 2 and 0
Whoops! cannot divide
None
--------------------

'''