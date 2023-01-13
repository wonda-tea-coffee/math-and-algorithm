from copy import deepcopy

MOD = 1000000007

# 2×2 行列 A, B の積を返す関数
def multiply(A, B, MOD):
	C = [ [ 0, 0 ], [ 0, 0 ] ]
	for i in range(2):
		for j in range(2):
			for k in range(2):
				C[i][j] += A[i][k] * B[k][j]
				C[i][j] %= MOD
	return C

# A^n(mod MOD)
def power(A, n, MOD):
	P = deepcopy(A)
	Q = [ [ 0, 0 ], [ 0, 0 ] ]
	flag = False
	for i in range(60):
		if (n & (1 << i)) != 0:
			if flag == False:
				Q = deepcopy(P)
				flag = True
			else:
				Q = deepcopy(multiply(Q, P, MOD))
		P = deepcopy(multiply(P, P, MOD))
	return Q

N = int(input())
A = [ [ 2, 1 ], [ 1, 0 ] ]
B = power(A, N - 1, MOD)

print((B[1][0] + B[1][1]) % MOD)
