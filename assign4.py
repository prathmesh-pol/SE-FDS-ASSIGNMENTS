x=int(input("Enter the no. of terms of p1 : "))
A=[]

for i in range (x):
    x1=[]
    m1=int(input("Enter the coeff. of p1 : "))
    m2=int(input("Enter the power of p1 : "))
    x1.append(m1)
    x1.append(m2)
    A.append(x1)
for i in range (len(A)):
    x1=A[i]
    if(i<(len(A)-1)):
        print(x1[0],"x^",x1[1],"+",end=" ")
    else:
        print(x1[0],"x^",x1[1])  

y=int(input("Enter the no. of terms of p2 : "))
B=[]         

for i in range (y):
    x2=[]
    n1=int(input("Enter the coeff. of p2 : "))
    n2=int(input("Enter the power of p2 : "))
    x2.append(n1)
    x2.append(n2)
    B.append(x2)
for i in range (len(B)):
    x2=B[i]
    if(i<(len(B)-1)):
        print(x2[0],"x^",x2[1],"+",end=" ")
    else:
        print(x2[0],"x^",x2[1])   

def eval(A):
    sum=0
    x=int(input("Enter the value of x : "))
    for i in range(len(A)):
        x1=A[i]
        val=pow(x,x1[1])
        sum+=x1[0]*val
    return sum 

def sum(A,B):
    for i in range(len(A)):
        x1=A[i]
        for j in range(len(B)):
            x2=B[i]
            if(x1[1]>x2[1]):
                B.insert(j,[x1[0],x2[1]])
                break
            elif(x1[1]==x2[1]):
                x2[0]+=x1[0]
                break
    return B        
             
def multi(A,B):
    c=[0]*(x+y-1) 
    for i in range(len(A)):
        for j in range(len(B)):
            z=A[i][0]*B[j][0]
            ex=A[i][1]+B[j][1]
            print(z," ",ex,end=" ")
            c[ex]+=z
    return c


                
e=eval(A)  
print("The value of p1 at x : ",e) 

s=sum(A,B)
print("Sum of p1 and p2 : ")
for i in range (len(B)):
        x2=B[i]
        if(i<(len(B)-1)):
            print(x2[0],"x^",x2[1],"+",end=" ")
        else:
            print(x2[0],"x^",x2[1])

m=multi(A,B)
print("Product of p1 and p2 : ",m)