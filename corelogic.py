#!/usr/bin/env python


class Counting():
    i = 3
    def __init__(self,*args):
        self.x=args[0]

        return

    def methodcalc(self):
        print (self)
        return


if __name__=="__main__":
    tes = Counting(2)
    print (tes.x)
    print (Counting.i)
    Counting.__dict__[i]