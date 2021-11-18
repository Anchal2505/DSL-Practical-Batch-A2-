import array as a
students=a.array("i",{})
n=int(input("Enter the number of students in class"))

print("Enter the marks of students and enter'-1' if absent")
for i in range(n):
  print("Enter marks of students for roll no {i}",end=" ")
  x=int(input())
  students.append(x)

for i in range(n):
  print(students[i])

   
#highest marks

def highest_in_array():
  z=students[0]
  for i in students:
    if(z<students[i]):
      z=students[i]
  print("highest marks=",z)
highest_in_array()


#lowest marks
def lowest_in_array():
  i=0
  l=students[0]
  for i in range(n):
    if(l>students[i]):
      if(students[i]!=-1):
        l=students[i]    
  print("lowest marks",l)
lowest_in_array()
  
#no. of absent students
def absent():
  abs=0
  for i in range(n):
    if(students[i]== -1):
      abs=abs+1
  print("number of absent students",abs)
absent()

#frequency
fr = [None]*n
visited=-1
for i in range(n):
  count = 1
  for j in range(i+1,n):
    if(students[i]==students[j]):
      count=count+1
      fr[j]=visited
  if(fr[i]!=visited):
    fr[i]=count
print("Element|Frequency")
for i in range(0,len(fr)):
  if(fr[i]!= visited):
    print(" "+str(students[i])+" | "+str(fr[i]))

def highest_fre_ele():
  z=fr[0]
  for i in fr:
    if(z<fr[i]):
      z=fr[i]
  print()
highest_fre_ele()

#average of marks  
def average():
  sum=0
  m=0
  for i in range(n):
    if(students[i]!= -1):
      sum=sum+students[i]
      m=m+1
  average=sum/m
  
  print(average)
average()
