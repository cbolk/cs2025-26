import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set seed
np.random.seed(42)
random.seed(42)

# --- CONFIGURATION ---
NUM_PATIENTS = 60 
SITES = ['NY-01', 'TX-05', 'LON-05']
TESTS = ['HbA1c', 'Systolic_BP', 'LDL', 'Weight_kg']

# --- 1. CREATE TREATMENTS CATALOG (Lookup Table) ---
# This table defines what drugs exist in the study
df_treatments = pd.DataFrame({
    'TrtID': ['T01', 'T02', 'T03'],
    'DrugName': ['Metabolix', 'StandardCare', 'Placebo'],
    'StudyArm': ['Experimental', 'ActiveControl', 'PlaceboControl']
})

# --- 2. CREATE PATIENTS TABLE ---
pids = np.arange(101, 101 + NUM_PATIENTS)
ages = np.random.randint(35, 80, size=NUM_PATIENTS)
sexes = np.random.choice(['M', 'F'], size=NUM_PATIENTS)
sites = np.random.choice(SITES, size=NUM_PATIENTS)


start_date_range = datetime(2025, 1, 1)
enroll_dates = [start_date_range + timedelta(days=random.randint(0, 150)) for _ in range(NUM_PATIENTS)]

df_patients = pd.DataFrame({
    'PID': pids,
    'Age': ages,
    'Sex': sexes,
    'SiteID': sites,
    'EnrollDate': enroll_dates
})

# --- 3. CREATE PATIENT_TREATMENT TABLE (Association Table) ---
# Links Patients to the Treatment Catalog
pt_data = []

for pid, enroll_date in zip(df_patients['PID'], df_patients['EnrollDate']):
    if pid % 7 == 0 or pid % 37 == 0:
        continue
    # Randomly assign a treatment ID
    trt_id = np.random.choice(['T01', 'T02', 'T03'], p=[0.4, 0.4, 0.2])
    
    # Determine dosage based on the ID
    if trt_id == 'T03': # Placebo
        dosage = 0
    elif trt_id == 'T01': # Metabolix
        dosage = np.random.choice([20, 50])
    else: # Standard Care
        dosage = np.random.choice([10, 20])
        
    start_date = enroll_date + timedelta(days=random.randint(1, 7))
    pt_data.append([pid, trt_id, start_date, dosage])

df_patient_treatment = pd.DataFrame(pt_data, columns=['PID', 'TrtID', 'StartDate', 'Dosage_mg'])

# --- 4. CREATE RESULTS TABLE ---
lab_data = []
lab_id_counter = 1

# We need to merge to know which drug the patient is on for data simulation logic
# (Merging temporarily just to generate realistic numbers)
temp_merge = pd.merge(df_patient_treatment, df_treatments, on='TrtID')

for index, row in temp_merge.iterrows():
    pid = row['PID']
    start_date = row['StartDate']
    drug_name = row['DrugName']
    
    # Visit 1: Baseline (-2 days), Visit 2: +30 days, Visit 3: +90 days
    offsets = [-2, 30, 90]
    
    for offset in offsets:
        visit_date = start_date + timedelta(days=offset)
        
        for test in TESTS:
            val = 0.0
            # Logic to simulate drug effect
            if test == 'HbA1c':
                val = round(np.random.uniform(5.5, 9.0), 1)
                if drug_name == 'Metabolix' and offset > 0: val -= 0.6
            elif test == 'Systolic_BP':
                val = round(np.random.normal(135, 15), 0)
            elif test == 'LDL':
                val = round(np.random.normal(120, 25), 0)
            elif test == 'Weight_kg':
                val = round(np.random.normal(85, 15), 1)
            
            lab_data.append([lab_id_counter, pid, visit_date, test, val])
            lab_id_counter += 1

df_results = pd.DataFrame(lab_data, columns=['LabID', 'PID', 'VisitDate', 'TestName', 'Value'])

# --- EXPORT & CLEANUP ---
# Format dates
df_patients['EnrollDate'] = df_patients['EnrollDate'].dt.strftime('%Y-%m-%d')
df_patient_treatment['StartDate'] = df_patient_treatment['StartDate'].dt.strftime('%Y-%m-%d')
df_results['VisitDate'] = df_results['VisitDate'].dt.strftime('%Y-%m-%d')

# Save
df_patients.to_csv('../codice/files/pd.trials.patients.csv', index=False)
df_treatments.to_csv('../codice/files/pd.trials.treatments.csv', index=False)
df_patient_treatment.to_csv('../codice/files/pd.trials.patient_treatment.csv', index=False)
df_results.to_csv('../codice/files/pd.trials.results.csv', index=False)
