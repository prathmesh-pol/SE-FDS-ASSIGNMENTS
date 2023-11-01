print("Input of matrix 1 - ")
r=int(input("Enter no. of rows : "))
c=int(input("Enter no. of columns : "))
m=[]
list=[]

for i in range(0,r):
    l=[]
    for j in range(0,c):
        n=int(input())
        if (n!=0):
            list.append([i,j,n])
            
        l.append(n)
    m.append(l)
#print(m)
print("\nSparse matrix1 - ")
# print(list)
list.insert(0,[r,c,len(list)])
for i in list:
    print(i[0],i[1],i[2])   

print("\nSimple Transpose of sparse matrix1 - ")
# for i in list:
#     print(i[1],i[0],i[2])          
x=[]
z=[]
z.append(c)
z.append(r)
z.append(len(m))
x.append(z)
for i in range(c):
    for k in range(1,len(m)+1):
        z=[]
        if(list[k][1]==i):
            z.append(list[k][1])
            z.append(list[k][0])
            z.append(list[k][2])
            x.append(z)

for i in range(len(m)+1):
    print(x[i])

print("\nFast Transpose of sparse matrix1 - ")
c=list[0][1]
A=[0]*c
for i in range(1,len(m)+1):
    A[list[i][1]]+=1

B=[0]*c
B[0]=1
for i in range(1,c):
    B[i]=B[i-1]+ A[i-1]

ftran=[0]*(len(m)+1)
ftran[0]=[list[0][1],list[0][0],list[0][2]]

for i in range(1,len(m)+1):
    x=list[i][1]
    y=B[x]
    ftran[y]=[list[i][1],list[i][0],list[i][2]]
    B[x]+=1
for i in range(len(m)+1):
    print(ftran[i])    
                

print("Input of matrix 2 - ")
r1=int(input("Enter no. of rows : "))
c1=int(input("Enter no. of columns : "))
n=[]
list1=[]

for i in range(0,r):
    l=[]
    for j in range(0,c):
        f=int(input())
        if (f!=0):
            list1.append([i,j,f])
            
        l.append(f)
    n.append(l)
#print(n)
#print(list1)
print("\nSparse matrix2 - ")
list1.insert(0,[r1,c1,len(list1)])
# print(list)
for j in list1:
    print(j[0],j[1],j[2])

print("\nAddition of sparse matrix1 and matrix2 - ")
for i in list:
    for j in list1:
      
      if(i[0]==j[0] and i[1]==j[1]):
          j[2]=i[2]+j[2]
          break
      elif(i[0]!=j[0] and i[1]==j[1]):
          list1.append([i[0],i[1],i[2]])
          break
      elif(i[0]==j[0] and i[1]!=j[1]):
           list1.append([i[0],i[1],i[2]])
           break
      elif(i[0]!=j[0] and i[1]!=j[1]):
           list1.append([i[0],i[1],i[2]])   
           break     
      
              

for j in list1:
    print(j[0],j[1],j[2])          
        #   print([i[0],j[1],i[2]+j[2]])
    
    #       print([i[0],j[0],])  
  