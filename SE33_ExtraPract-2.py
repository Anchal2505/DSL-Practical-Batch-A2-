#players in SE class
import array as a
s=a.array("u",{})
n=int(input("Enter no. of players in SE class"))

for u in range(n):
  print("Enter name of players in SE class")
  x=input()
  s.append(x)

for u in range(n):
  print(s[u])

#cricket players
import array as g
a=g.array("u",{})
m=int(input("Enter number of cricket players"))

for u in range(m):
  print("Enter name of cricket players")
  y=input()
  a.append(y)

for u in range(m):
  print(a[u])

#badminton players
import array as d
b=d.array("u",{})
t=int(input("Enter number of badminton players"))

for u in range(t):
  print("Enter name of badminton players")
  z=input()
  b.append(z)

for u in range(t):
  print(b[u])

#football players
import array as h
c=h.array("u",{})
l=int(input("Enter no. of football players"))

for i in range(l):
  print("name of football players")
  u=input()
  c.append(u)

for u in range(l):
  print(c[u])

#list of students who play both cricket and badminton
a_and_b = []
for k in a:
  if k in b:
    a_and_b.append(k)
print("a_and_b=",a_and_b)

#list of student who plays either cricket or badminton but not both

a_or_b = []
for j in s:
  if j not in a_and_b:
    a_or_b.append(j)
for j in b:
  if j not in a_and_b:
    a_or_b.append(j)
print("a_or_b=",a_or_b)

#number of students who neither play cricket nor badminton

a_nor_b=[]
for p in s:
  if(p not in a) and (p not in b):
    a_nor_b.append(p)
print("a_nor_b",a_nor_b)
print("number of students who neither play cricket nor badminton=",len(a_nor_b))

#number of students who play cricket and football but not badminton

a_and_c = []

for o in a:
  if o not in b:
    a_and_c.append(o)
for o in c:
  if(o not in b) and (o not in a_and_c):
    a_and_c.append(o)
print("a_and_c=",a_and_c)
print("number of students who play cricket and football but not badminton=",len(a_and_c))