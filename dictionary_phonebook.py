n = int(input())

reg = dict()

for i in range(n):
    name_number = str(input())
    for i in name_number:
        if i == ' ' :
            a = name_number.index(' ')
            name = name_number[:a]
            number = name_number[a+1:]
            break
    reg[name] = number
    
for i in range(n):
    
    query = str(input())
    try: 
        print(query+'='+reg.get(query))
    except:
        print("Not found")
    
