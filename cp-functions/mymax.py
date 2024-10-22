def max_of_two(m,n):
    if m>n:
        return m
    else:
        return n
    

def max_of_three(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    #elif c>a & c>b:
     #   return c
    

def listMax(l):
    a = max(l)
    b = l.index(a)
    return (a,b)


if __name__ == "__main__":
    print("you are running stand alone file")