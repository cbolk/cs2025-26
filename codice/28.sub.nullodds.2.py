def nullodds(values):
    size = len(values)
    for i in range(1, size, 2):	# check only odd elements
        # if the element's value is odd
        if values[i] % 2 != 0:
            values[i] = 0
            