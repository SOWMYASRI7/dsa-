def tsearch(a,t,l,r):
    if l>r:
        return -1
    mid1=l+((r-l)//3)
    mid2=r-((r-l)//3)
    if t==a[mid1]:
        return mid1
    elif t==a[mid2]:
        return mid2
    else:
        if t<a[mid1]:
            return tsearch(a,t,l,mid1-1)
        elif t<a[mid2]:
            return tsearch(a,t,mid2+1,r)
        else:
            return tsearch(a,t,l,r)
def solve():
    a=[2,23,34,48,55,88,99]
    t=55
    index=tsearch(a,t,0,len(a)-1)
    print("result",index)
solve()