if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    brr = list(arr)
    num = -10000
    for i in range(len(brr)):
        if num < brr[i]:  
            num = brr[i]
    num1 = -10000
    for i in range(len(brr)):
        
        if num1 < brr[i] and brr[i] < num:  
            num1 = brr[i]
print(num1)
