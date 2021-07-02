p=int(input('enter prime count '))
d=2
c=True
while d!=p:
	if p%d==0:
		c=False
	d+=1	

def gcd(a,b):
    if(b==0):
        return a
    return gcd(b, a % b)

def compare(a, b):
    sortedA = sorted(list(set(a)))
    sortedB= sorted(list(set(b)))
    return [ai for ai in sorted(a) if ai not in sorted(b)]


def pm(m):
    rs = [i for i in range(0, m) if gcd(i, m) == 1]
    res = []
    for g in range(1, m):
        ak = [g ** i % m for i in range(0, m)]
        if(len(compare(rs, ak)) == 0):
            res.append(g)
    return res

if c==True:
	z=pm(p)
	print(z)
else:
	print('error')
