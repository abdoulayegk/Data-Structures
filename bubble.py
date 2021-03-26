""" In this program we are going to implement bublle sort algorithm in python"""

arr = []
n= int(input("Enter the number of elements you wish to enter:"))
for i in range(n):
    arr.append(int(input("Enter an element into your list:")))

print("The resultant list is:\n",arr)
#
def bubble(arr):
    length = len(arr)
    for i in range(length):
        for j  in range(length-i-1):
            if(arr[j]> arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
bubble(arr)
print(arr)
