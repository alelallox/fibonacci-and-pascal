#Pascal's triangle
def Pascal(n):
    # initializes the first line of the triangle
    riga = [1]
    # Calculate the next line 
    for i in range(n):
        print(' '.join(str(x).center(2) for x in riga).center(n*5))
        riga = [1] + [riga[j] + riga[j+1] for j in range(len(riga)-1)] + [1]

n = 10 #number of lines in the triangle
Pascal(n)
