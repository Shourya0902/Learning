def print_rangoli(size):
    # your code goes here
    al = "abcdefghijklmnopqrstuvwxyz"
    width = (4 * size) - 3
    
    a = list()
    a.append(al[size-1])
    cen = '-'.join(a)
    print(cen.center(width,'-'))
    
    for i in range(2,size+1):
        b = len(a)
        c = int((b+1) / 2)
        a.insert(c,al[size-i])
        d = size + 1 - i
        a.insert(c+1,al[d])
        cen = '-'.join(a)
        print(cen.center(width,'-'))
        
    for i in range(2,size+1):
        b = len(a)
        c = int((b-1) / 2)
        a.pop(c)
        a.pop(c)
        cen = '-'.join(a)
        print(cen.center(width,'-'))        
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
