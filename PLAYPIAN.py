import sys
t = int(input())

while t >0:
    x = input()
    n=0
    c=0
    for i in range(0,int(len(x)/2)):

        if(x[n]==x[n+1]):
            print("no")
            sys.stdout.flush()
            c=1
            break
        n = n+2
    if(c==0):
        print("yes")
        sys.stdout.flush()
    t = t-1
