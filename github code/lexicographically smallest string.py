d = raw_input()
a=[0]*len(d)
b=[0]*len(d)
for i in range(1,len(d)):
	for num in range(0,i-1):
		if(d[i]==d[num]):
			a[i]=1
			break
		a[i]=0
	
print ''.join(str(e) for e in a)

for i in range(0,len(d)):
	for num in range(i+1,len(d)):
		if(d[i]==d[num]):
			b[i]=1
			break
		b[i]=0
print ''.join(str(e) for e in b)
