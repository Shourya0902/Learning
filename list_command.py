    for i in range(N):
        inp = input()
        if inp == "print" or inp == "sort" or inp == "pop" or inp == "reverse":
            funct.append(inp)
            a = 0
            no.append(a)
        else:
            f, *a = inp.split()
            no.append(a)
            funct.append(f)    
               
    p = 0
    q = 0
    r = 0
    
    for i in range(N):
        if funct[i] == "insert":
            p = int(no[i][0])
            q = int(no[i][1])
            arr.insert(p,q)
        elif funct[i] == "print":
            print(arr)
        elif funct[i] == "append":
            arr.append(int(no[i][0]))
        elif funct[i] == "sort":
            arr.sort()
        elif funct[i] == "pop":
            arr.pop()
        elif funct[i] == "reverse":
            arr.reverse()
        elif funct[i] == "remove":
            arr.remove(int(no[i][0]))
