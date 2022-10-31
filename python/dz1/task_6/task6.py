lst = []
for i in range(5):
    lst.append(int(input()))
lst = sorted(lst, reverse=True)
for i in range(len(lst)):
    print(lst[i])
