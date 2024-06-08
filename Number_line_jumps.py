#You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).
#The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
#The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
#You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.

import itertools

def kangaroo(x1, v1, x2, v2):
    d1=0
    d2=0
    for i in itertools.count():
        if i==0: i+=1
        d1=x1+(v1*i)
        d2=x2+(v2*i)
        if d1==d2:
            return "YES"
        if i>=10000:
            return "NO"
          
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])
    result = kangaroo(x1, v1, x2, v2)
    print(result)
