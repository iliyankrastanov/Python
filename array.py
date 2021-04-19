if __name__ == "__main__":
    z = 12
    m = [1, 4, 6, 8, 9, 23]
    #m = [1, 4, 6, 8, 9, 3, 12, 24, 23, 2, 11]   

def printPairs(arr, arr_size, sum):
    s=set()
    for i in range(0, arr_size):
        temp = sum-arr[i]
        if (temp in s):
            print("The result is:", (arr[i]), "+" , (temp))
        s.add(arr[i])
            
printPairs(m, len(m), z)