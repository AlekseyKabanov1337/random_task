a=int(input('Enter value a= '))
sta=[]
c=0
for i in range(1,a+1):
	if a%i==0:
		c+=1
		sta.append(i)
print('function t(a)= ',c)
print('all dividers -', sta,',function s(a)=', sum(sta))

def eler(a):
	result=a
	for i in range(2,a):
		if a%i==0:
			while a%i==0:
				a//=i
			result-=result//i
	if a>1:
		result-=result//a
	return result
fi=eler(a)
print('Euler function fi(a)=',fi)
