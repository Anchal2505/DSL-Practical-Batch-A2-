import array as arr
a=arr.array("i",{})
n=int(input("Enter size of array"))

for i in range(n):
  print("Enter roll no. of students")
  x=int(input())
  a.append(x)

for i in range(n):
  print(a[i])

l=int(input("Enter roll no to be searched"))

print("1-linear search")
print("2-sentinal search")
print("3-binary search(non-recurssive)")
print("4-binary search (recurssive)")

option = int(input("Enter your choice"))

#linear search

if option == 1:
  print("#linear search#")
  for i in range(n):
    if((l==a[i] and l!=0)):
      print(l,"is present at index",i)
    else:
      print("not found")
  if l == 0:
    print("absent")

#sentinel search -- for reducing number of comparisions

elif option == 2:
  print("#sentinel search#")
  def sentinel(a,l):
    lastele=a[-1]
    a[-1]=l
    i=0
    while (a[i]!=l):
      i=i+1
      a[-1]=lastele
      length=n
      if ((i<n-1) or a[n-1]==l):
        return i
      else:
        return 1
  sentinel(a,l)
  if l!=a[i]:
    print("not found")
  elif l == 0:
    print("absent")
  else:
    print(l,"is present")

#binary search -- non recurssive

elif option == 3:
  print("#binary search non recurssive#")
  def binary_non_recurssive(a,l):
    low = 0
    high = n-1
    mid = 0
    while (low<=high):
      mid=(high+low)//2
      if(a[mid]<l):
        low=mid+1
      elif(a[mid]>l):
        high=mid-1
      else:
        return mid
    return -1

  my_res = binary_non_recurssive(a,l)

  if my_res!=-1:
    print(l,"is found at index",str(my_res))
  else:
    print("Element not found")

#binary search -- recurssive

elif option == 4:
  print("#binary search recuerssive#")
  def binary_search(a, low, high, l):
	  if high >= low:

		  mid = (high + low) // 2
		  if a[mid] == l:
		  	return mid
		  elif a[mid] > l:
			  return binary_search(a, low, mid - 1, l)
		  else:
			  return binary_search(a, mid + 1, high, l)

	  else:
		  return -1

  result = binary_search(a, 0, n-1, l)

  if result != -1:
    print(l,"Element is present at index", str(result))
  else:
	  print("Element is not present in array")

else:
  print("Invalid choice")