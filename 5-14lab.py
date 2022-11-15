def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a+b

fibnum = list(fib(20))
print (fibnum)



"""


def fibo(N):

	Xn2 = 0; Xn1 = 1
	yield Xn2 
	if N==0: return 
	yield Xn1
	i = 1	
	while i < N: 	# N = 2 means F2
		Xn = Xn1 + Xn2
		yield Xn 
		Xn2 = Xn1
		Xn1 = Xn
		i += 1

		
def fibo2(n):
  a = 0
  b = 1
  for i in range(N+1):
    if i == 0:
      yield a
    if i == 1:
      yield b
    else:
      c = a+b
      yield c
      a = b
      b = c

def fibo1(n):
	# Xn2 = 0
	# Xn1 = 1
	fib = 0
  prev1 = 0
  prev2 = 0
  for i in range(N + 1):
    fib = prev1 + prev2
    if i == 1:
      prev1 = 1
      fib = prev1 + prev2
    else:
      prev2 = prev1
      prev1 = fib
 
    yield fib
    


n = 3
mygen = fibo(n)

print (list(mygen))

"""