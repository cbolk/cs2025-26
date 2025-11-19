# Solution without csv library
FNAME = "patients.csv"

def compute_bmi_from_csv(filename):
    """
    Reads a CSV file with patient data and computes BMI for each patient.
    Returns a dictionary {name: BMI}.
    """
    bmi_values = {}
    try:
        with open(filename, "r") as f:
            lines = f.readlines()

        # Skip header (first line)
        index = 1  # start from second line
        total_lines = len(lines)

        while index < total_lines:
            line = lines[index].strip()
            parts = line.split(",")

            name = parts[0].strip()
            weight = float(parts[1])
            height = float(parts[2])
            bmi = weight / (height ** 2)
            bmi_values[name] = bmi

            index += 1  # move to next line

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("Error:", e)

    return bmi_values

# ---- MAIN SCRIPT -----

bmi_values = compute_bmi_from_csv("patients.csv")

if len(bmi_values) > 0:
    # Display each BMI
    for name in bmi_values:
        print(name, "-", round(bmi_values[name], 1))

    # Compute and display average BMI
    avg_bmi = sum(bmi_values.values()) / len(bmi_values)
    print("Average BMI:", round(avg_bmi, 1))
else:
    print("No valid data found.")
    