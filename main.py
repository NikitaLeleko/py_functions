def digital_root(n):
    sum = 0
    n = str(n)
    if len(n)>1:
        for i in range(len(n)):
            sum += int(n[i])
        sum = str(sum)
    else:
         sum = int(n)
    return sum
    if len(sum) > 1:
        digital_root(sum)
