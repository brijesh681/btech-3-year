# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1
 
 
# Test array
input_string = input('Enter elements of a Sort list separated by space  :  \n')
data = input_string.split()
# convert each item to int type
for i in range(len(data)):
    # convert each item to int type
    data[i] = int(data[i])
print('Array: ', data)
user_input= int(input('Search Element: '))
 
# Function call
result = binary_search(data, user_input)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
