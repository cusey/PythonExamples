#python 3.5.2

'''
You will learn about Python @property; pythonic way to use getters and setters.
'''

class lovelypython():
    def __init__(self):
        self._myname = "Albert"

    @property
    def myname(self):
        return self._myname + " is awesome"

    @myname.setter
    def myname(self, val):
        self._myname = val



lp = lovelypython()
lp.myname = "Gao"
print(lp.myname)


'''
OUTPUT:

Gao is awesome
'''