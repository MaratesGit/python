a = []
for i in range(int(input())):
    a.append(int(input()))   
x=int(input())
minel=1001
for i in a:
    if (abs(i-x))<minel:
        minel=(abs(i-x))
        elem=i
print(elem)
    
    
    
