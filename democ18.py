L = []
def f1(a):
    if(a > 30):
        return a+100

    for var in [10,20,30,40,50,60]:
        r = f1(var)
        L.append(r)
    print (L[:3])
    
