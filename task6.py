from collections import Counter
p=int(input(''))
d=2
n=p-1
pro=[]
mo=[]
ot=[]
while d!=p:
	if p%d==0:
		print('error')
		break
	d+=1
def kan(n):
	pr=[]
	d=2
	while d*d<=n:
		if n%d==0:
			pr.append(d)
			n//=d
		else:
			d+=1
	if n>1:
		pr.append(n)
	return pr

pro=kan(n)

x=Counter(pro)	

pr=list(set(pro))

print(pr,x)

for j in range(2,p):
	for i in range(len(pr)):
		if ((j**(n//pr[i])-1))%p!=0:
			ot.append(j)
ot=sorted(list(set(ot)))
print(ot, end=' ')
