
def arr_sum(arr):
     if len(arr) == 1:
        return arr[0]
     else:
        return arr[0]+ arr_sum(arr[1:])


if __name__ == "__main__":

    arr = [1, 2, 3, [5, 6, [7]], 4]
res = arr_sum(arr = [[1,2,3,4], [5,6], [7]]) #Не мога да се сетя за друг вариант.

print (arr_sum(res))
