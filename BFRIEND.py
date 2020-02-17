t = int(input())
while t:
    t = t-1
    arr = []
    n,a,b,c = input().split()
    n,a,b,c = int(n),int(a),int(b),int(c)
    flats = input().split()
    for i in flats:
        val = abs(a-int(i)) + abs(int(i)-b) + c
        arr.append(val)
    print(min(arr))
    
