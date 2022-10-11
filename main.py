def multiplication_of_matrix(lst1: list, lst2: list):
    result = []
    for i in range(len(lst1)):
        buff = []
        for j in range(len(lst1[i])):
            buff.append(lst1[i][j] * lst2[i][j])
        result.append(buff)
    print(result)
