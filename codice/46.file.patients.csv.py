import csv

FNAME = "patients.csv"

def compute_bmi_from_csv(filename):
    """
    Reads a CSV file with patient data and computes BMI for each patient.
    Returns a dictionary {name: BMI}.
    """
    bmi_values = {}
    try:
        with open(filename, newline='') as f:
            reader = csv.reader(f)

            # Read header
            header = next(reader)

            # Process rows
            for row in reader:
                name = row[0].strip()
                weight = float(row[1])
                height = float(row[2])
                bmi = weight / (height ** 2)
                bmi_values[name] = bmi

    except FileNotFoundError:
        print("Error: File not found.")

    except Exception as e:
        print("Error:", e)

    return bmi_values


# ---- MAIN SCRIPT -----

bmi_values = compute_bmi_from_csv(FNAME)

if len(bmi_values) > 0:
    # Display each BMI
    for name in bmi_values:
        print(name, "-", round(bmi_values[name], 1))

    # Compute and display average BMI
    avg_bmi = sum(bmi_values.values()) / len(bmi_values)
    print("Average BMI:", round(avg_bmi, 1))
else:
    print("No valid data found.")
