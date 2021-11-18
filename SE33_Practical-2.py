a=input("first and last name of the student:")
#To display name with the longest length
c=[]
c=a.split()
x=0
for i in range(len(c)):
  if x<len(c[i]):
    x=len(c[i])
    y=c[i]
print(f"{x} for {y}")

#To determines the frequency of occurrence of particular character in the string
b=input('enter the character:')
count=0
for i in a:
  if i==b:
    count=count+1

    
print(count)

#To check given string is palindrome or not
q=a
p=input("another string")
r=" "
for i in range(len(p)-1,-1,-1):
  r=r+p[i]
if(q==p):
  print("the string is palindrome=")
else: 
  print("it is not a palingdrone=")



#To display index of first substring
z=input("enter the substring")
e=0
for i in range(len(a)-1):  # "a" is from top line
  if (a[i]==z[e]):
    e=e+1
    if(e==len(z)):
      break
  if len(z)==0:
    break

if(e<len(z)):
    print("not present")
else:
   k=i-e+1
   print(f'{z} is present at position {k}')


#To count the occurrences of each word in string
g=input(" enter the word")
count=0
for i in c:
  if i==g:
    count=count+1
print(count)