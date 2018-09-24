#python 3.5.2

from string import Template

def Main():

    print ("** TEMPLATES **")
    
    cart = []
    cart.append(dict(item='Coke', price=8, qty=2 ))
    cart.append(dict(item='Cake', price=12, qty=1 ))
    cart.append(dict(item='Fish', price=32, qty=4 ))
    
    t = Template('$qty x $item = $price')
    total = 0
    print('Cart:')
    
    for data in cart:
        print(t.substitute(data))
        total += data['price']
        
    print('Total: ' + str(total) )
   
    
if __name__ == '__main__':
    Main()
    
'''
OUTPUT:

** TEMPLATES **
Cart:
2 x Coke = 8
1 x Cake = 12
4 x Fish = 32
Total: 52

'''
