def nullodds(values):
    size = len(values)
    for i in range(size):
        if i % 2 == 0:  # it is in odd position
            # if the element's value is odd
            if values[i] % 2 != 0:
                values[i] = 0
