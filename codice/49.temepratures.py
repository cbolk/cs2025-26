def load_measurements(filename):
    """Load txt data into dictionary: {location: [(temp, date), ...]}"""
    data = {}
    
    try:
        with open(filename, 'r') as file:
            # Skip header line
            header = file.readline()
            
            # Process data lines
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    location = parts[0]
                    temperature = float(parts[1])
                    date = parts[2]
                    
                    # Populate dict
                    if location not in data:
                        data[location] = []
                    data[location].append((temperature, date))
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return {}
    
    return data

def calculate_average_per_location(data):
    """Calculate average temperature for each location"""
    averages = {}

    # compute for each key
    for location, readings in data.items():
        total = 0.0
        count = 0
        for temp, _ in readings:
            total += temp
            count += 1

        if count > 0:
            averages[location] = total / count 
        else:
            averages[location] = 0
    
    return averages

def find_extreme_readings(data):
    """Find highest and lowest temperatures across all locations"""
    # Initialisation to first value

    min_location = max_location = next(iter(data))
    readings = data[max_location]
    min_temp = max_temp = readings[0][0]
    min_date = max_date = readings[0][1]
    for temp, date in readings[1:]:
        if temp > max_temp:
            max_temp = temp
            max_date = date
        elif temp < min_temp:        
            min_temp = temp
            min_date = date
    
    for location, readings in data.items():
        for temp, date in readings:
            if temp > max_temp:
                max_temp = temp
                max_location = location
                max_date = date
            elif temp < min_temp:
                min_temp = temp
                min_location = location
                min_date = date
    
    return {
        'max': {'temp': max_temp, 'location': max_location, 'date': max_date},
        'min': {'temp': min_temp, 'location': min_location, 'date': min_date}
    }


def save_summary(averages, extremes, output_filename):
    """Save summary statistics to a text file"""
    try:
        with open(output_filename, 'w') as file:
            
            # Title
            file.write("Temperature Measurement Summary\n")
            file.write("-" * 40 + "\n")
                        
            # Extremes
            file.write(">> Extreme Readings:\n")
            file.write(f"Highest: {extremes['max']['temp']:.2f}°C at {extremes['max']['location']} on {extremes['max']['date']}\n")
            file.write(f"Lowest: {extremes['min']['temp']:.2f}°C at {extremes['min']['location']} on {extremes['min']['date']}\n")

            # Averages
            file.write(">> Average Temperatures by Location:\n")          
            for location, avg in averages.items():
                file.write(f"{location}: {avg:.2f}°C\n")

        
        print(f"Summary saved to {output_filename}")
    
    except Exception as e:
        print(f"Error saving file: {e}")


# ------Main execution example ------

data = load_measurements('measurements.txt')
averages = calculate_average_per_location(data)
extremes = find_extreme_readings(data)
save_summary(averages, extremes, 'summary.txt')
