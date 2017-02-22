def tri():
	b=[1]
	while True:
		yield b
		b.insert(0,0)
		b.append(0)
		for x in range(len(b)-1):
			b[x]=b[x]+b[x+1]
		b.pop()
n=0 
for t in tri():
	print(t)
	n=n+1
	if n==10:
		break
