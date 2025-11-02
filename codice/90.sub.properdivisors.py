def properdivisors(val):
	pd = []
	for i in range(1, val):
		if val % i == 0:
			pd.append(i)

	return pd
	