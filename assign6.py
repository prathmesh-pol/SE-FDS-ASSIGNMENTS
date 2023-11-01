n=int(input("Enter no. of students :"))
Roll=[]
for i in range(n):
    r=int(input())
    Roll.append(r)
f=int(input("Enter the roll no. of student found : "))
Roll.sort()

def linear_s(Roll,f):
    for i in Roll:
        if (i==f):
            return True
    return False

def sentinel_s(Roll,n,f):
    Roll.append(f)
    i=0
    while(Roll[i]!=f):
        i+=1
    if(i!=len(Roll)-1):
        return True
    else:
        return False    


def binary_s(Roll,f,le,he):
    
    c=(le+he)//2
    if(he<le):
        return False
    if(f==Roll[c]):
        return True
    elif(f<Roll[c]):
        return binary_s(Roll,f,le,c)
    elif(f>Roll[c]):
        return binary_s(Roll,f,c,he)
    return False

def fibonacci_s(Roll,f,n):
    offset=0
    f0=0
    f1=1
    f2=1
    while(f2<n):
        f0=f1
        f1=f2
        f2=f1+f0

    while(f2>1):
        i=min(offset+f0,n-1)
        if Roll[i]<f:
            f2=f1
            f1=f0
            f0=f2-f1
            offset=i
        elif Roll[i]>f:
            f2=f0
            f1=f1-f0
            f0=f2-f1
        else:
            return True
    return False

print("\nLinear Search :")
l=linear_s(Roll,f)
print(l)

print("\nSentinel Search :")
s=sentinel_s(Roll,n,f)
print(s)

print("\nBinary Search :")
b=binary_s(Roll,f,0,n-1)
print(b)

print("\nFibonacci Search :")
f=fibonacci_s(Roll,f,n)
print(f)


    

