# Fibonacci Sequence
def fibonacci(sequence_len):
    #first two values of the sequence 
    arr = [1, 1]
    x=0
    y=1
    #At each iteration of the cycle, calculate the sum of the last two numbers of the list 
    for i in range(sequence_len):
        val = arr[x+i]+arr[y+i]
        arr.append(val)
    return arr

  #calculate the golden section by dividing 2 consecutive terms of the fibonacci sequence      
def golden_section(arr):
    arr2 = []
    val2 = 0
    for i in range(30):
        val2 = arr[i+1] / arr[i]
        arr2.append(val2)
    return arr2


sequence_len = 30 #number of values of the sequence
arr = fibonacci(sequence_len) 
print("fibonacci sequence: ",arr)
print("")
arr2 = golden_section(arr)
print("ratio of n and n-1: ",arr2)


