# Enter your code here. Read input from STDIN. Print output to STDOUT
m, n = input().split()

i = 1
width = int(n)
for i in range(int(m)):
    string = ".|."
    if i % 2 == 1:
        print((string*(i)).center(width,'-'))
        
print( "WELCOME".center(width,'-'))

for i in reversed(range(int(m))):
    string = ".|."
    if i % 2 == 1:
        print((string*(i)).center(width,'-'))
