a=int(input('Enter numerator  '))
while a<0:
	print('Error')
	a=int(input('Enter numerator  '))
b=int(input('Enter denominator  '))
while b==0 or b<0:
	print('Error')
	b=int(input('Enter denominator  '))
print('our fraction = ',a,'/',b)
c=[]
q=[]
p=[]
c.append(a//b)

def cep(a,b,c):
	a=abs(a)
	b=abs(b)
	if b > a:
		while a!=0:
			c.append(b//a)
			l=b
			b=a
			a=l%a
	if a > b:
		a=a%b
		while a!=0:
			c.append(b//a)
			l=b
			b=a
			a=l%a
	return c
cep=cep(a,b,c)


print('Our chain fraction: ', cep)	

for i in range(len(cep)):
	q.append(0)
	p.append(0)
p[0]=cep[0]
p[1]=cep[0]*cep[1]+1
q[0]=1
q[1]=cep[1]
for n in range(2,len(cep)):
	p[n]=cep[n]*p[n-1]+p[n-2]
	q[n]=cep[n]*q[n-1]+q[n-2]

print('Inverse transform result: ',p[-1],'/',q[-1])

