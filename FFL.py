t = int(input())
while(t):
    t = t-1
    n,s = [int(i) for i in input().split()]
    p = [int(i) for i in input().split()]
    pos = [int(i) for i in input().split()]
    m1,m2 =  1000000,1000000
    for i in range(n):
        if p[i] < m1 and pos[i] == 0:
            m1 = p[i]
        elif p[i] < m2 and pos[i] == 1:
            m2 = p[i]
    if m2+m1+s <= 100:
        print("yes")
    else:
        print("no")
