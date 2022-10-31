string = input().split()
string2 = input()
for i in string:
	if i.lower().find(string2) != -1:
		print(i)
