n=int(input("Enter no. of students :"))
P=[]
for i in range(n):
    r=int(input())
    P.append(r)

def slsort(P,n):
    for i in range(n):
        min_i=i
        for j in range(i+1,n):
            if P[min_i]>P[j]:
                min_i=j
        P[i],P[min_i]=P[min_i],P[i]
    return P 

def insort(P,n):
    n=len(P)
    for i in range(1,n):
        temp=P[i]
        j=i-1
        while(j>=0 and temp<P[j]):
           P[j+1]=P[j]
           j-=1
           P[j+1]=temp
    return P

def bublesort(P,n):
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if(P[j]>P[j+1]):
                k=P[j]
                P[j]=P[j+1]
                P[j+1]=k       
    return P 

def shellsort(P,n):
    gap=n/2
    k=int(gap)

    while(k>0):
        for i in range(k,n):
            temp=P[i]
            j=i
            while(j>=k and P[j-k]>temp):
                P[j]=P[j-k]
                j-=k
                P[j]=temp
        k=int(k/2)
    return P                     

m=int(input("\n1 : Selection sort\n2 : Insertion sort\n3 : Bubble sort\n4 : Shell sort\n\nENTER YOUR CHOICE : "))

if(m==1):
  s=slsort(P,n) 
  print(s)  

elif(m==2):
  ins=insort(P,n)
  print(ins)

elif(m==3):
  b=bublesort(P,n)
  print(b)

elif(m==4):
  sh=shellsort(P,n)
  print(sh)