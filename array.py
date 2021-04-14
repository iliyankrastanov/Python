if __name__ == "__main__":
    z = 12
    m = [1, 4, 6, 8, 9, 23]    

def printPairs(arr, arr_size, sum):
    s=set()
    for i in range(0, arr_size):
        temp = sum-arr[i]
        if (temp in s):
            print("Result:", (arr[i]), "+" , (temp))
        s.add(arr[i])
            
printPairs(m, len(m), z)