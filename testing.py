from itertools import product

def multiply(res):
    output = []
    for i in res:
        output.append(bin(int(i[0], 2) * int(i[1], 2))[2:].zfill(n * 2))
    return output

val_x = []
val_y = []

if __name__ == "__main__":

    filename = "rom_{0}x{1}.dat"

    while True:
        try:
            n = int(input('Enter n = '))       
            
            name = filename.format(f'{2**(2*n)}', f'{2*n}')
            fileobject = open(name,'w')

            for x in range(n ** 2):
                arr = 0
                for y in range(n ** 2):            
                    if y == 0:
                        arr += 1
                if arr == 1:
                    val_x.append(bin(x)[2:].zfill(n))
                    val_y.append(bin(x)[2:].zfill(n))

            res_xy = list(product(val_x, val_y))

            res_z = (multiply(res_xy))
            for index in range(len(res_z)):
                value = res_z[index]
                print(value)
                fileobject.write(f'{value}')

        except (ValueError, KeyError,NameError) as e:
            print(f'Invalid value or action ({e})')
            print("Please enter valid integer value")

        fileobject.close()