def isort(a):
    n=len(a)
    for i in range(1,n):
        target=ar[i]
        tinde=i
        sindex=i-1
        while sindex>=0 and target < a[index]:
            a[sindex+1]=a[sindex]
            sindex-=1
            tindex-=1
        if tindex!=i:
            a[tindex]=target
def solve():
    a=[2,23,48,30,55,88,99]
    index=isort(a)
    print("result",a)
solve() 