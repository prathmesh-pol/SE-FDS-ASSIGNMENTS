r=int(input("Enter rows : "))
c=int(input("Enter columns : "))
m=[]
x=[]
o=[]

print("Input for matrix1")

for i in range(0,r):
    l=[]
    for j in range(0,c):
        n=int(input())
        l.append(n)
    m.append(l)
print(m)

print("Input for matrix2")

for i in range(0,r):
    l1=[]
    for j in range(0,c):
        n=int(input())
        l1.append(n)
    x.append(l1)
print(x)

for i in range(0,r):
    l2=[]
    for j in range(0,c):
        n=0
        l2.append(n)
    o.append(l2)


def is_upper(m,r,c):
    for i in range(0,r):
        for j in range(0,c):
            if(j<i and m[i][j]==0):
                return True
            # else:
            #     return False
    return False

def sum_d(m,r,c):
    sum=0
    for i in range(0,r):
        for j in range(0,c):
            if (i==j):
                sum+=m[i][j]
    return sum

def tran_m(o,r,c):
    for i in range(r):
        for j in range(0,c):
            o[i][j]=m[j][i]
    return o 

def sum(o,r,c):
    for i in range(r):
        for j in range(0,c):
            o[i][j]=m[i][j]+x[i][j]
    return o  

def diff(o,r,c):
    for i in range(0,r):
        for j in range(0,c):
            o[i][j]=m[i][j]-x[i][j]
    return o  

def multi(m,x,o,r,c):
    for i in range(0,r):
        for j in range(0,c):
            for k in range(0,c):
              o[i][j] += m[i][k] * x[k][j]
    return o 

def saddle(m,r,c):
    for i in range(0,r):
        for j in range(0,c):
            if (m[i][j]==min(m[i]) and m[i][j]==max(row[j]) for row in m):
                return(i,j)
    return("doesn't exist")        
        


u=is_upper(m,r,c)
if (u==True):
    print("The given matrix1 is upper triangular.")
else:
    print("The given matrix1 is not upper triangular.")

sd=sum_d(m,r,c)
print("Sum of the diagonal elements of matrix1 is ",sd)   

t=tran_m(o,r,c)
print("Transpose of matrix1 is = ",t)

s=sum(o,r,c)
print("Sum of matrix1 and matrix2 = ",s)

d=diff(o,r,c)
print("Difference of matrix1 and matrix2 = ",d)

m=multi(m,x,o,r,c)
print("Multiplication of matrix1 and matrix2 = ",m)

sp=saddle(m,r,c)
print("Saddle point of matrix1 = ",sp)
