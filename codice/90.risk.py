def risk(tmap):    
    rows = len(tmap)
    cols = len(tmap[0])
    
    # the first element is the one with the highest risk
    max_diff = 0
    maxposi = 0
    maxposj = 0
    
    # Iterate through each point in the map
    for i in range(rows):
        for j in range(cols):
            current_altitude = tmap[i][j]
            # Check all adjacent points (including diagonals)
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:                    
                    # Calculate neighbor coordinates
                    ni = i + di
                    nj = j + dj
                    # Check if neighbor is within bounds
                    if 0 <= ni < rows and 0 <= nj < cols:
                        neighbor_altitude = tmap[ni][nj]
                        diff = abs(current_altitude - neighbor_altitude)
                        # Update maximum if this difference is larger
                        if diff > max_diff:
                            max_diff = diff
                            maxposi = i
                            maxposj = j
    
    return max_position, max_diff


# Test with the example map
terrain = [
    [90.63, 37.81, 31.08, 66.97, 72.15, 14.50, 89.89, 84.26, 84.60, 21.83],
    [90.41, 65.41, 77.28, 42.58, 36.68, 24.04, 67.79, 89.28, 90.34, 69.86],
    [24.98, 10.92, 83.42, 5.52, 28.58, 75.20, 83.78, 88.33, 32.92, 80.16],
    [39.19, 23.55, 17.98, 70.28, 90.52, 90.13, 84.78, 80.41, 74.39, 69.38],
    [45.02, 85.73, 4.82, 28.45, 91.25, 33.40, 3.65, 75.03, 21.20, 36.57],
    [55.20, 60.92, 60.12, 73.17, 31.20, 50.64, 63.30, 15.98, 31.05, 37.69],
    [85.36, 33.29, 2.49, 20.15, 12.81, 9.87, 91.63, 16.37, 85.03, 52.39],
    [10.27, 30.06, 38.12, 15.09, 58.50, 29.37, 48.48, 62.15, 4.40, 70.21],
    [98.72, 59.60, 31.12, 58.84, 32.77, 62.32, 9.48, 96.07, 78.30, 40.53]
]

posi, posj, difference = pericolo(terrain)
print(f"Position: {posi},{posj}")
print(f"Difference: {difference:.2f}")
print(f"Altitude: {terrain[posi][posj]:.2f}")
