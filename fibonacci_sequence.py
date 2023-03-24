# Fibonacci Sequence
def fibonacci(sequence_len):
    #first two values of the sequence 
    arr = [0, 1]
    x=0
    y=1
    #At each iteration of the cycle, calculate the sum of the last two numbers of the list 
    for n in range(sequence_len):
        val = arr[x+n]+arr[y+n]
        arr.append(val)
    print(arr)

sequence_len = 30 #number of values of the sequence
fibonacci(sequence_len)



