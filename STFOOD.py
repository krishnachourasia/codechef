t = int(input())
while t:
    n = int(input())
    arr = []
    for i in range(n):
        s,p,v = input().split()
        s = int(s)+1
        p = int(p)
        v = int(v)
        val = (p//s)*v
        arr.append(val)
    print(max(arr))
    t = t-1
