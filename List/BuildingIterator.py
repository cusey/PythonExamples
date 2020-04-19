class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        print("1) n:" + str(self.n) + " max:" + str(self.max))
        if self.n <= self.max:
            result = 2 ** self.n
            print("2) result:" + str(result) )

            self.n += 1
            print("3) n:" + str(self.n))
            return result
        else:
            raise StopIteration


a = PowTwo(4)
i = iter(a)
print(next(i))
