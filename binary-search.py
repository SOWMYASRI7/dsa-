def bs(a,t):
    n=len(a)
    l,r=0,n-1
    while l<=r:
        mid=(l+r)//2
        if t == a[mid]:
            return mid
        elif t<a[mid]:
            r=mid-1
        else:

            l=mid+1
def solve():
    a=[2,23,34,48,55,88,99]
    t=55
    index=bs(a,t)
    print("result",index)
solve()