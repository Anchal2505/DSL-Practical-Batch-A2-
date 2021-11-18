import array as b
rows=int(input("Enter number of rows"))
column=int(input("Enter number of columns"))

matrix1=[]
for i in range(rows):
  a=b.array("i",[])
  for j in range(column):
    a.append(int(input("enter elements of 1st matrix")))
  matrix1.append(a)

print("1st matrix")
for i in range(rows):
  for j in range(column):
    print(matrix1[i][j],end=' ')
  print(end= '\n')


matrix2=[]
for i in range(rows):
  c=b.array("i",[])
  for j in range(column):
    c.append(int(input("Emter elements of 2nd matrix")))
  matrix2.append(c)

print("2nd matrix")
for i in range(rows):
  for j in range(column):
    print(matrix2[i][j],end=' ')

  print(end='\n')

# addition of matrix1 and matrix2
result=[]
for i in range(rows):
  d=b.array("i",[])
  for j in range(column):
    d.append(int(input("enter zeros for initializing result matrix")))
  result.append(d)

print("result")
for i in range(rows):
  for j in range(column):
    print(result[i][j],end=' ')
  print(end='\n')

print("Addition of m1 and m2")
for i in range(len(matrix1)):
  for j in range(len(matrix2)):
    result[i][j]=matrix1[i][j]+matrix2[i][j]
for r in result:
  print(r)
  
#subtraction of matrix1 and matrix2
print("subtraction of m1 and m2")
for i in range(len(matrix1)):
  for j in range(len(matrix2)):
    result[i][j]=matrix1[i][j]-matrix2[i][j]
for r in result:
  print(r)

#Transpose of matrix1 and matrix2
for i in range(len(matrix1)):
  for j in range(len(matrix2[0])):
    result[j][i]=matrix1[i][j]

print("transpose of matrix1")

for r in result:
  print(r)

for i in range(len(matrix2)):
  for j in range(len(matrix2[0])):
    result[j][i]=matrix2[i][j]

print("Tranpose of matrix 2")
for r in result:
  print(r) 

#multiplication
print("Multiplication")
for i in range(len(matrix1)):
  for j in range(len(matrix2[0])):
    for k in range(len(matrix2)):
      result[i][j] +=matrix1[i][k]*matrix2[k][j]

for r in result:
  print(r)
