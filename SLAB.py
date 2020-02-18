t = int(input())
while(t):
    t = t-1
    income = int(input())
    inc = 250000
    tax = 0
    per = 0.05
    slab = 250000
    while(inc < income):
        slab = slab + 250000
        if(income < slab):
            tax = tax + per*(income - inc)
        else:
            tax = tax + per*(slab - inc)
        inc = inc + 250000
        per = per + 0.05
        if(per > 0.25):
            tax = tax + 0.30*(income - 1500000)
            break
    print(int(income-tax))

