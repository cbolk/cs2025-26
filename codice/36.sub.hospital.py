EXITMENU = "quit"

# Initialize the patient database
patients = {}

def insert_metric(patient_id, metric, value):
    if patient_id not in patients:
        patients[patient_id] = {}
    if metric not in patients[patient_id]:
        patients[patient_id][metric] = []
    patients[patient_id][metric].append(value)

def delete_patient(patient_id):
    if patient_id in patients:
        patients.pop(patient_id)
        return True
    return False

def compute_average(patient_id, metric):
    if patient_id in patients and metric in patients[patient_id]:
        values = patients[patient_id][metric]
        return sum(values) / len(values)
    return None

def print_summary(patient_id):
    if patient_id in patients:
        print(f"Data for patient {patient_id}:")
        for metric, values in patients[patient_id].items():
            print(f"  {metric}: {values}")
    else:
        print("Patient not found.")

def is_at_risk(patient_id):
    if patient_id not in patients:
        return None
    data = patients[patient_id]  # data is dict(metric: [values])
    risk_factors = []
    if "blood_pressure" in data and max(data["blood_pressure"]) > 140:
        return True
    if "glucose" in data and max(data["glucose"]) > 125:
        return True
    return False

# ------ MAIN SCRIPT --------

action = input("\nChoose action (insert, average, delete, risk, summary, quit): ").strip().lower()

while action != EXITMENU:     
    if action == "insert":
        in_input = input("Enter: <patientID, metric, value>").split(",").strip()
        pid = in_input[0].strip()
        metric = in_input[1].strip()
        value = float(in_input[2].strip())
        insert_metric(patient_id=pid, metric=metric, value=value)
    
    elif action == "delete":
        pid = input("Enter patientID to delete: ")
        delete_patient(pid)

    elif action == "average":
        in_input = input("Enter: <patientID, metric>").split(",").strip()
        pid = in_input[0].strip()
        metric = in_input[1].strip()
        avg = compute_average(pid,metric)
        if avg is not None:
            print(f"Average: {avg:.2f}")
        else:
            print("Patient or metric not found.")

    elif action == "summary":
        pid = input("Enter patientID: ").strip()
        print_summary(pid)

    elif action == "risk":
        pid = input("Enter patientID: ").strip()
        risk = is_at_risk(pid)
        if risk is None:
            print("Patient not found.")
        elif risk:
            print("Patient is at risk!")
        else:
            print("Patient is not at risk")        
    else:
        print("Invalid action. Try again.")

    action = input("\nChoose action (insert, average, delete, risk, summary, quit): ").strip().lower()
print("Exiting program.")
