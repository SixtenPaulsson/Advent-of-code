def transpose(matrix = []):
    a = [[y for y in x] for x in matrix]


    print(a)
    #for height
    transposed = []
    for height in range(len(matrix)):
        for width in range(len(matrix[0])):
            if (len(transposed)==width): transposed.append([])
            transposed[width].append(matrix[height][width])
    print("\n".join(["".join(x) for x in transposed]))
    return transposed


with open("2024/day25/day25.txt") as File:
    kns = [x.split() for x in File.read().split("\n\n")]
    is_lock = lambda x: x[0]=="#####" and x[-1]=="....."
    is_key = lambda x: x[0]=="....." and x[-1]=="#####"
    locks=[x[1:-1] for x in list(filter(is_lock,kns))]
    keys =[x[1:-1] for x in list(filter(is_key,kns))]

    pins = lambda x: ["".join(y).count("#") for y in transpose(x)]

    #print((transpose(keys[0])))
    print("\n".join(keys[0]),pins(keys[0]))
    #print([len(x) for x in locks])
    transpose(keys[0])