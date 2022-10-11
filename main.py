def transposing_matrix(lst: list):
    result = []
    for i in range(len(lst[0])):
        bufflist = []
        for j in range(len(lst)):
            bufflist.append(lst[j][i])
        result.append(bufflist)
    return result
