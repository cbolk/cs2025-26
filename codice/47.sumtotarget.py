def find_pairs_sum(numbers, target):
    size = len(numbers)
    pairs = []
    
    # Iterate through all possible pairs
    for i in range(size):
        for j in range(i + 1, size):
            # Check if pair sums to target
            if numbers[i] + numbers[j] == target:
                # Sort the pair to maintain consistency and avoid duplicates
                # pair = sorted([numbers[i], numbers[j]])
                if numbers[i] <= numbers[j]:
                    pair = list(numbers[i], numbers[j])
                else:
                    pair = list(numbers[j], numbers[i])
                # Add only if not already in list
                if pair not in pairs:
                    pairs.append(pair)
    
    return pairs


# Test --------
numbers = [2, 7, 11, 15, 3, 6, 8]
target = 10
result = find_pairs_sum(numbers, target)
print(result)  # [[2, 8], [3, 7]]
