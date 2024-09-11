# Python program to find Maximum and minimum of an array using ittrative method
def max_min_element(data):
        max=data[0]
        min=data[0]
        for i in range(1,n):
            if data[i]>max:
                max=data[i]
            if data[i]<min:
                min=data[i]
        #The number of comparison in Naive method is 2n - 2.
        return(max,min)
    
# Driver code
if __name__ == "__main__":
    # Test array
    input_string = input('Enter elements of a Sort list separated by space  :  \n')
    data = input_string.split()
    # convert each item to int type
    for i in range(len(data)):
        # convert each item to int type
        data[i] = int(data[i])
    print('Array: ', data)
    n = len(data)
    min,max=max_min_element(data)
    print("Minimum element is:", min)
    print("Maximum element is:",max)
