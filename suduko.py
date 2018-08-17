def construct(i):
    global a
    if (a[i]==0):
        print(i)
        for t in range(1,10):
            if (check(t,i) & check1(t,i)):
                a[i]=t
                print(i,t)
                if (i==80):
                    return True
                p=i+1
                if (construct(p)):
                    return True
        a[i]=0
        return False
    elif (i==80):
        return True
    else:
        p=i+1
        return construct(p)
def check(t,i):
    global a
    for j in range(0,9):
        if (a[(i//9)*9+j]==t):
            return False
        if (a[(9*j)+(i%9)]==t):
            return False
    return True
def check1(t,i):
    global a
    col=((i//9)//3)*3
    row=(((i)%9)//3)
    for l in range(0,3):
        for m in range(0,3):
            if (a[9*(col+l)+((3*row)+m)]==t):
                return False
    return True
def due(p):
    global a
    a=p
    construct(0)
    return a