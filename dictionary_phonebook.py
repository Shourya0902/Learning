n = int(input())

reg = dict()

for i in range(n):
    name, number = list(input().split())
    reg[name] = number
    
while True:  
    try:
        query = str(input()) 
        if query in reg:
            print(query+'='+reg.get(query))
        else:
            print("Not found")
    except:
        break
    
