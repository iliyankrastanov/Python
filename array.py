if __name__ == "__main__":
    z = 12
    #m = [1, 4, 6, 9, 23, 8]
    m = [1, 4, 3, 2, 2, 5, 3, 23, 2, 11, 1, 5, 8 ,15, 8]   

def printPairs(arr, arr_size, sum):
    s=set()
    for i in range(0, arr_size):
        temp = sum-arr[i]
        if (temp in s):
            print("The result is:", (arr[i]), "+" , (temp))
        s.add(arr[i])
            
printPairs(m, len(m), z)