# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.
 
# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
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
result = binary_search(data, 0, len(data)-1, user_input)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
