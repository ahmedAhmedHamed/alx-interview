def pascal_triangle(n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        return []
    ret = [[1]]
    n -= 1
    i = 1
    # checking if n was bigger than one to not have the if inside the loop
    if n:
        n -= 1
        ret.append([1, 1])
    while n:
        new_value = ret[i][:]
        new_value.append(1)
        for j in range(len(new_value)):
            if j != 0 and j != len(new_value) - 1:
                new_value[j] = ret[i][j] + ret[i][j - 1]
        ret.append(new_value)
        i += 1
        n -= 1
    return ret
