def diamonde(n):
    if n  % 2 == 0 or n < 0:
        return None
    else:
        diamond = ""
        space = n//2
        star = 1
        for i in range(1,n+1):
            if i < n//2+1:
                for _ in range (1,space+1):
                    diamond  = diamond + " "
                space -=1
                for _ in range(star):
                    diamond  = diamond + "*"
                star +=2
                diamond = diamond + "\n"
            elif i == n//2 + 1:
                for _ in range(n):
                    diamond  = diamond + "*"
                diamond = diamond + "\n"
                space +=1
                star -=2
            else:
                for _ in range (1,space+1):
                    diamond  = diamond + " "
                space +=1
                for _ in range(star):
                    diamond  = diamond + "*"
                star -=2
                diamond = diamond + "\n"
    return diamond
print(diamonde(5))