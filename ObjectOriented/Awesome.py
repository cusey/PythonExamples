#python 3.5.2

class lovely():
    def __init__(self):
        self._name = "Albert"

   # GETTER     
    @property
    def name(self):
        return self._name + " is awesome"

    # SETTER
    @name.setter
    def name(self, val):
        self._name = val


l = lovely()
l.name = "Gao"
print(l.name)



