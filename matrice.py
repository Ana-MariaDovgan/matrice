A=[[1,3,7,90,123],
   [112,34,56,78,91],
   [8,71,60,39,556],
   [16,96,58,73,700],
   [18,45,54,65,83]]
print(A)
l1=A[0]
l2=A[1]
l3=A[2]
l4=A[3]
l5=A[4]
s1=[]
s2=[]
s3=[]
s4=[]
s5=[]
for i in A:
    s1.append(i[0])
    s2.append(i[1])
    s3.append(i[2])
    s4.append(i[3])
    s5.append(i[4])
print('suma elementelor din linia 1:',sum(l1))
print('suma elementelor din linia 2:',sum(l2))
print('suma elementelor din linia 3:',sum(l3))
print('suma elementelor din linia 4:',sum(l4))
print('suma elementelor din linia 5:',sum(l5))
print('suma elementelor din coloana 1:',sum(s1))
print('suma elementelor din coloana 2:',sum(s2))
print('suma elementelor din coloana 3:',sum(s3))
print('suma elementelor din coloana 4:',sum(s4))
print('suma elementelor din coloana 5:',sum(s5))
dp=[]
ds=[]
for i in range(len(A)):
    dp.append(A[i][i])
    for j in range(len(A[0])):
        if j+i==4:
            ds.append(A[i][j])
print('diagonala principala:',dp)
print('diagonala secundara:',ds)