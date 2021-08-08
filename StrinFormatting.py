import math

def binary(n):
    a = list()
    for i in range(1000):
        if int(n / 2) > 0:
            d = int(n % 2)
            a.append(str(d))
            n = n / 2
        elif int(n / 2) == 0:
            d = int(n % 2)
            a.append(str(d))
            break
    a.reverse()
    c = ""
    b = c.join(a)        
    return b
    
def octal(n):
    a = 0
    for i in range(1,n+1):
        a = a + 1
        b = str(a)
        if i < 100:
            c = len(b) - 1
            d = len(b) - 2
            if b[c] == '8' and b[d] != '7':
                a = a + 2 
            if b[c] == '8' and b[d] == '7':
                a = a + 22        
                 
        if i >= 100:
            c = len(b) - 2 
            if b[c] == '8':
                a = a + 2 
             
    return a

def hexa(n):
    h = "ABCDEFG"
    y = 0
    d = 1
    s = 0
    t = 0
    z = list()
    for i in range(n+1):
        
        if i < 10:
            p = i
            a = p
            e = 0
            
        elif i <= 16:
            q = h[e]  
            e = e + 1
            a = q
            if a == "G":
                a = p + 1
                e = 0
                 
        if i > 16:
            m = i - (15*d) - (1*d)
            if m <= 9:
                z.append(str(d))
                z.append(str(m))
                v = ""
                f = v.join(z)
                a = str(f)
                z.clear()
                if m == 9:
                    r = int(a)
            if m > 9 and m <= 16:
                x = h[e]
                e = e + 1
                z.append(str(d))
                z.append(x)
                v = ""
                f = v.join(z)
                a = str(f)
                z.clear()
                if x == "G":
                    d = d + 1
                    e = 0
                    a = r + 1
                      
                    
    return a
                

def print_formatted(number):
    # your code goes here
    n = number
    v = binary(n)
    u = str(v)
    a = len(u) 
    
    for i in range(1,n+1):
        b = binary(i)
        o = octal(i)
        h = hexa(i)
        
        if i == 1:
            q = a
            p = a
            m = a
        
        w = len(str(i))
        m = a - w - 1
        
        x = len(str(b))
        p = a - x + 1
            
        y = len(str(o))
        q = a - y + 1
        
        z = len(str(h))
        r = a - z + 1
        
        print(" "*m,i , end = " "*q)
        print(o , end = " "*r)
        print(h , end = " "*p)
        print(b)
        
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
