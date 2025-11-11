def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32
    
# --- MAIN SCRIPT ------

# Ask the user for input
input_str = input("Enter temperatures in Celsius, separated by commas: ")

# Split the input string into a list
celsius_values = input_str.split(",")

# Convert each value and print the result
print("Fahrenheit equivalents:")
for value in celsius_values:
    c = float(value)
    f = celsius_to_fahrenheit(c)
    print(f"{c}°C is {f}°F")
