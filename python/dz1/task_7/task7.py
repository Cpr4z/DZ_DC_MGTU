string = input().lower().split(', ')
st = set()
for i in string:
	st.add(i)
st = sorted(st)
print(', '.join(st))
