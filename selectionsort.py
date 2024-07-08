def ssort(a):
    n=len(a)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if a[j]<a[min]:
                min=j
        if min !=i:
            a[i],a[min]=a[min],a[i]
def solve():
    a=[2,23,48,30,55,88,99]
    index=ssort(a)
    print("result",a)
solve()         
