a=int(input('Enter a= '))
b=int(input('Enter b= '))
m=int(input('Enter m= '))
while m<=0:
	print('errror, repit input m')
	m=int(input('Enter m= '))
c=[]
c.append(m//a)
q=[]
def gcd(a,m):
	a=abs(a)
	m=abs(m)
	while a != 0 and m != 0:
		if a > m:
			a = a % m
		else:
			m = m % a
	g=a+m
	return g

def eler(m):
	result=m
	for i in range(2,m):
		if m%i==0:
			while m%i==0:
				m//=i
			result-=result//i
	if m>1:
		result-=result//m
	return result

def qwer(a, m): 
	x = 1 
	x1 = 0
	while m != 0:
		q = a// m
		r = a % m
		x2 = x - q * x1
		a, m = m, r
		x, x1 = x1, x2
	return x
	
def cep(a,m,c):
	a=abs(a)
	if m > a:
		while a!=0:
			c.append(m//a)
			l=m
			m=a
			a=l%a
	if a > m:
		a=a%m
		while a!=0:
			c.append(m//a)
			l=m
			m=a
			a=l%a
	return c
	
cep=cep(a,m,c)	

for i in range(len(cep)):
	q.append(0)
q[0]=1
q[1]=cep[1]
for n in range(2,len(cep)-1):
	q[n]=cep[n]*q[n-1]+q[n-2]
	
d=gcd(a,m)
fi=eler(m)
s=qwer(a,m)


if d>=1:
	if (b%d)!=0:
		print('no solution')
	elif (b%d)==0:
		b//=d
		a//=d
		m//=d
		print('we have ',d, 'solution')
		
		n=len(cep)
		x2=(s*b)%m
		print('euclidean algorithm')
		for k in range(d):
			print('comparison has solution, x<=> ',x2+m*k ,'mod ',m*d)
		x1=(q[n-2] * b)%m*(-1)**(n-2)
		if x1<0:
			x1+=m
		x0=(b*a**(fi-1))%m
		print('euler function')
		for k in range(d):
			print('comparison has solution, x<=> ',x0+m*k ,'mod ',m*d)
		print('chain fraction')
		for k in range(d):
			print('comparison has solution, x<=> ',x1+m*k ,'mod ',m*d)
else:
	print('no solution')
