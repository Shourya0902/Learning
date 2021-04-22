def swap_case(s):
    t = list()
    u = list()
    
    for i in s:
        t.append(i)
    
    for i in t:
        if i.isupper() == True:
            u.append(i.lower())
            
            
        elif i.islower() == True:
            u.append(i.upper())
            
        
        else:
            u.append(i)
    
    v = ''.join(u) 
             
    return v

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
