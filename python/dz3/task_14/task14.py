import os
from pathlib import Path


def get_popular_name_from_file(filename):
    list_of_names = []
    dic = {}
    max_freq = 0
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            list_of_names.append(((line.strip().split('\n'))[0].split(' '))[0])
    for i in list_of_names:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in dic:
        if dic[i] > max:
            max = dic[i]
        else:continue
    list_of_max = []
    for i in dic:
        if dic[i] == max:
            list_of_max.append(i)
    return ', '.join(sorted(list_of_max, key = lambda c: c[0][0].lower()))
if __name__ == '__main__':
    print(get_popular_name_from_file('names.txt'))
