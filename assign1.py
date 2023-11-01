n=int(input("Enter total no. of students : "))
L=[]
sum=0
x=0 #no of absent students
p=0
f=0

for i in range(0,n):

    m=int(input("Enter marks : "))
    if (m>=0):
        sum+=m
        L.append(m)
    if(m<0):
        x=x+1
avg=sum/(n-x)

for i in range(0,n-x):
    if(L[i]>=45):
        p=p+1
    else:
        f=f+1

print("Enter the avg of marks : ")
print(avg)
max=L[0]
min=L[0]
for i in range(0,n-x):
    if(L[i]>max):
        max=L[i]

    if(L[i]<min):
        min=L[i]
print("Maximum = ",max)
print("Minimum = ",min)
print("Total no. of absent students :",x)

pp=p*100/(n-x)
fp=f*100/(n-x)
print("Passing percentage :",pp)
print("Failing percentage :",fp)

L.sort()
print("Top three highest scores : ")
print(L[-1])
print(L[-2])
print(L[-3])

print(L)

freq=0
m=L[0]
for i in L:
    if(L.count(i)>freq):
        m=i
        freq=L.count(i)
print(m)        
