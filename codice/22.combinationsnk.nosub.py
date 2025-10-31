# controlled acquisition n (strictly positive)
n = int(input())
while n <= 0:
	n = int(input())
# controlled acquisition k (included in interval [1, n])
k = int(input())
while k <= 0 or k > n:
	k = int(input())

# factorial n
fn = 1
for i in range(2, n+1):
	fn = fn * i
# factorial k
fk = 1
for i in range(2, k+1):
	fk = fk * i
# factorial n-k
diff = n-k
fnk = 1
for i in range(2, diff+1):
	fnk = fnk * i
# combinations
comb = fn / (fk * fnk)

print(comb)
