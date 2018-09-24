#python 3.5.2

def first():
    x = 'Hello World'
    
    def second():
        print(x)
        
    return second
    
func = first()
    
func()

'''
OUTPUT:

Hello World

'''
    
    
    