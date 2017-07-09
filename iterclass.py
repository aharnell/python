#!python
from datetime import datetime
now = datetime.now

class mything(object):
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            self.k = v
#        self.one = 1
#        self.two = 2
#        self.three = 3
#        self.four = 4
        self.time = now()
        self._index = 0
#        self._iteritems = 

    def __iter__(self):
        return self

    def __next__(self):
        items = tuple(z for y, z in self.__dict__.items() if not y.startswith("_"))
#        for x in [y for y in self.__dict__.keys() if not y.startswith("_")]:
#            yield x
        try:
          result = items[self._index]
        except IndexError:
            self._index = 0
            raise StopIteration
        self._index += 1
        return result
        
if __name__ == '__main__':
    thing = mything(one=1, two=2, three=3)
    s = 1
    while s:
        for x in thing:
            print(x)
        s = bool(input('> '))
