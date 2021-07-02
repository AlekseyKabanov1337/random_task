n=int(input('How many equations? '))
b=[]
m=[]
mi=[]
c=[]
cel=[]
yi=[]
x0=0
C=0
M=1
for i in range(1,n+1):
	print('Enter b',i,'= ',end="")
	b.append(int(input()))
	print('Enter m',i,'= ',end="")
	m.append(int(input()))
print('Our system: ')
for i in range(n):
	print('x<=>',b[i],'(mod',m[i],')')
	
def gcd(k,l):
	a=abs(k)
	m=abs(l)
	while k != 0 and l != 0:
		if k > l:
			k = k % l
		else:
			l = l % k
	g=k+l
	return g

for j in range(len(m)): 
	for i in range(len(m)):
		if m[j]!=m[i]:
			g=gcd(m[j],m[i])
			if g==1:
				c.append(1)
			else:
				c.append(0)
		else:
			continue
	
for i in range(len(c)):
	if c[i]==0:
		C+=1

if C!=0:
	print('system take any solution')
else:
	for i in range(0,n):
		M*=m[i]
	for i in range(0,n):
		mi.append(M//m[i])
	for j in range(0,n):
		for i in range(1,m[j]):
			cel.append(i)
		for s in range (len(cel)):
			if ((mi[j]*cel[s]-1)%m[j])==0:
				yi.append(cel[s])
		cel.clear()
	for i in range(0,n):	
		x0+=mi[i]*yi[i]*b[i]
	print('Our equation has only one solution x=',x0%M,'(mod',M,')')	
	
