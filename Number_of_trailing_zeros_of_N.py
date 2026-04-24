def zeros(n):
    zero = 0
    two = 0 
    five = 0 
    for i in range(1,n+1):
        
        while i % 10 == 0:
            
            zero +=1
            i = i/10
        
        while i % 2 == 0:
            two +=1
            i = i/2
        
        while i % 5 == 0:
            five +=1
            i = i/5
    if two < five:
        zero += two
    else:
        zero += five

    print(f"two = {two} \n five = {five} \n zero = {zero}")
    
    return zero

print(zeros(30))