""" In this programme we are going to implement binary search tree using recursion method"""

def recursive_bs(array,target,low,high):
    while(low <= high):
        mid = (low+high )//2
        if (target == array[mid]):
            return array[mid]
        elif (target < array[mid]):
            return recursive_bs(array,target,low,mid-1)
        elif (target > array[mid]):
            return recursive_bs(array,target,mid+1, high)
    print('Element not found in the array ')
    return False

#arr = [12,14,17,18,19,22,25,28,30]
#print(recursive_bs(arr,1,0,len(arr)))
# another way to take the input from the user
num = int(input("Enter the number of elements in your list:\n"))
array = []
for i in range(num):
    array.append(int(input('Enter the element into your array:\n')))

array.sort()

target =int(input("Enter the element you are looking for:\n"))
print(recursive_bs(array,target,0,len(array)))

