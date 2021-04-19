if __name__ == '__main__':
    arr = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name,score])
    
    low = float(0)
    for i in range(len(arr)):
        if low == 0:
            low = arr[i][1]
        elif low > arr[i][1]:
            low = arr[i][1]
            
            
    low1 = float(1000000)
    for i in range(len(arr)):
        if low1 > arr[i][1] and arr[i][1] > low:
            low1 = arr[i][1]  
            
    
            
    brr = list()
        
    for i in range (len(arr)):
        if arr[i][1] == low1:
            brr.append(arr[i][0])
        
    brr.sort()
    for i in range(len(brr)):
        print(brr[i])
