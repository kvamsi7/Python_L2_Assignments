''' iterator class that iterators over a sequence of values in the reverse direction '''

class IterReverse:
    def __init__(self,seq):
        self.seq = seq
        self.pos = len(seq)
    def __next__(self):
        if self.pos == 0:
            raise StopIteration
        self.pos -= 1
        return self.seq[self.pos]


data = [i for i in range(11)]
itr = IterReverse(data)
while True:
    try:
        print(itr.__next__(), end =", ")
    except StopIteration:
        break