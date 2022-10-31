string = input().split(', ')
dic = {}
for i in string:
    dic[i] = 0
for i in string:
    dic[i] += 1
mylist = [i for i in dic.items()]

mylist = sorted(mylist, key = lambda x: x[1],reverse= True)
#print(mylist)
if len(mylist) < 3:
    for i in range(len(mylist)):
        print(f'{mylist[i][0]}: {mylist[i][1]}')
else:
    for i in range(3):
        print(f'{mylist[i][0]}: {mylist[i][1]}')
