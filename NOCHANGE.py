t = int(input())
while(t):
    t = t-1
    n,p = input().split()
    n,p = int(n),int(p)
    denoms = list(map(int, input().split()))
    d = dict()
    dele = []
    for i in range(len(denoms)):
            if  p%denoms[i] == 0:
                d[denoms[i]] = 0
                dele.append(denoms[i])
    for i in dele:
        if i in denoms:
            denoms.remove(i)
    if len(denoms) == 0:
        print("NO", end = '\n')
    else:
        for i in range(len(denoms)-1,-1,-1):
            d[denoms[i]] = p//denoms[i]
            p = p%denoms[i]
        d[denoms[0]] = d[denoms[0]] + 1
        
        print("YES", end = " ")
        for key in sorted(d):
            print(d[key], end = " ")
        print(end = "\n")
