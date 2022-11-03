from math import sqrt
def isPrime(N):
	k = int(sqrt(N)) + 1
	for i in range(2, k, 1):
		if (N % i == 0):
			return False
	return True
def getDifference(N):
	if (N == 0):
		return 2
	elif (N == 1):
		return 1
	elif (isPrime(N)):
		return 0
	aboveN = -1
	belowN = -1
	n1 = N + 1
	while (True):
		if (isPrime(n1)):
			aboveN = n1
			break
		else:
			n1 += 1
	n1 = N - 1
	while (True):
		if (isPrime(n1)):
			belowN = n1
			break
		else:
			n1 -= 1
	diff1 = aboveN - N
	diff2 = N - belowN
	return min(diff1, diff2)
if __name__ == '__main__':
	N = int(input())
	print(getDifference(N))
