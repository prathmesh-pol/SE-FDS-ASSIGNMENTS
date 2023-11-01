def intersection(l1,l2):
    return[value for value in l1 if value in l2]

def difference(l1,l2):
    return[value for value in l1 if value not in l2]

def count_c_and_f_not_badminton(l_a,l_b,l_c):
    count=0
    for student in l_a:
        if student in l_c and student not in l_b:
            count+=1
    return count

def count_neither(l1,total_students):
    return total_students-len(l1)   

def no_games(l1,total_students):
    return total_students-len(l1)

def all_games(l_a,l_b,l_c):
    return intersection(intersection(l_a,l_b),l_c)

def atleast_one(l_a,l_b,l_c):
    return l_a+l_b+l_c    

n=int(input("Enter total no. of students : "))
G_a=[]  #cricket
G_b=[]  #badminton
G_c=[]  #football
G_d=[]  #don't play any game

a=int(input("Enter no. of students who play cricket : "))
for i in range(0,a):

    x=int(input("Enter students who play cricket : "))
    G_a.append(x)

b=int(input("Enter no. of students who play badminton : "))
for i in range(0,b):    

    y=int(input("Enter students who play badminton : "))
    G_b.append(y)

c=int(input("Enter no. of students who play football : "))
for i in range(0,c):

    z=int(input("Enter students who play football : "))
    G_c.append(z)

for i in range(1,n+1):
    if((i not in G_a) and (i not in G_b) and (i not in G_c)):
        G_d.append(i)

c_and_b = intersection(G_a,G_b) 
print("Students who play cricket and badminton : ",c_and_b)

c_or_b_not_both = difference(G_a+G_b,c_and_b)
print("Students who play cricket or badminton but not both : ",c_or_b_not_both)

neither_c_nor_b=G_c+G_d
print("Students who play neither cricket nor badminton : ",neither_c_nor_b)

c_and_f_not_b = count_c_and_f_not_badminton(G_a,G_b,G_c)
print("No. of students who play cricket and football not badminton : ",c_and_f_not_b)

no_game=G_d
print("Students who do not play any game : ",no_game)

atleast_onegame=atleast_one(G_a,G_b,G_c)
print("Students who play atleast one game : ",atleast_onegame)

all_gamesplay=atleast_one(G_a,G_b,G_c)
print("Students who play all games : ",all_gamesplay)




    


    

                               


