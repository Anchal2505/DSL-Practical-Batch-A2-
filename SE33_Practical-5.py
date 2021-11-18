n=int(input("Enter total number of students: "))
s=[]
for i in range(n):
    r=int(input(f"Enter roll number: "))
    s.append(r)
def shellsort(arr,n):
    gap=n//2
    while gap>0:
        for i in range(gap,n):
            temp=arr[i]
            j=i
            while(j>=gap and arr[j-gap]>temp):
                arr[j]=arr[j-gap]
                j=j-gap
            arr[j]=temp
        gap=gap//2
shellsort(s,len(s))
print("sorted numbers are: ",s)

def insertion_sort(sort_list):
    for i in range(1, len(sort_list)):
        key = sort_list[i]
        j = i - 1
        while j >= 0 and key < sort_list[j]:
            sort_list[j + 1] = sort_list[j]
            j -= 1
        sort_list[j + 1] = key
    print('\nThe sorted list:', sort_list)
lst = []
size = int(input("\nEnter size of the list:"))
for i in range(size):
    elements = int(input("Enter the element:"))
    lst.append(elements)
insertion_sort(lst)