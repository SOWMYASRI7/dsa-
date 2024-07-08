def ls(ar,t):
    n=len(ar)
    for i in range(n):
        if ar[i]==t:
            return i
        return -1

def solve():
    ar=[7,4,5,2,6,8,10,3,6]
    t=7
    index=ls(ar,t)
    print("result",index)
solve()