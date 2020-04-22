t = int(input())
while(t):
    t = t-1
    n,q = input().split(" ")
    n,q = int(n), int(q)
    floors = 0
    curr = 0
    while(q):
        q = q - 1
        s,d = input().split(" ")
        s,d = int(s),int(d)
        floors += (abs(s-curr) + abs(d-s))
        curr = d
    print(floors)
