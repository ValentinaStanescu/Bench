def john(n):
    jhon = []
    jhon.append(0)
    anna = ann(n)
    print(f"n={n}")
    print(f"ana = {anna}")
    for i in range (1, n):
        #print(f"jhon[i-1]: {jhon[i-1]}")
        #print(f"anna[jhon[i-1]]: {anna[jhon[i-1]]}")
        #print(f"i-anna[jhon[i-1]: {i-anna[jhon[i-1]]}")
        #print("\n")
        jhon.append(i-anna[jhon[i-1]])
    print(f"jhon = {jhon}")
    return jhon
    
def ann(n):
    ann_l=[]
    for i in range(1, n+1):
        if i%2==0:
            ann_l.append(i//2)
        else:
            ann_l.append(i//2+1)
    return ann_l
    
def sum_john(n):
    return sum(john(n))
    
def sum_ann(n):
    return sum(ann(n))