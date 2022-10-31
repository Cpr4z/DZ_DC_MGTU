def lists_sum(*args, unique=False):
    #print(args)
    sum = 0
    max = 0
    dic = {}
    if unique:#ищем сумму только уникальных элементов
        for i in args:
            for j in i:
                if j > max:
                    max = j
                else:
                    continue
        #print(max)
        for i in range(max+1):
            dic[str(i)] = 0
        #print(dic)
        for i in args:
            for j in i:
                dic[str(j)] += 1
        for i in dic:
            if dic[i] > 0:
                sum += int(i)
    else:#ищем сумму всех элементов
        for i in args:
            for j in i:
                sum += j
    #print(sum)
    return sum
