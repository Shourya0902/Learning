def solve(s):
    a = list()
    for i in s:
        a.append(i)
    a[0] = a[0].upper()
    for i in range(len(a)):
        if a[i] == ' ':
            a[i+1] = a[i+1].upper()
    b = ''.join(a)
    return b
    
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
