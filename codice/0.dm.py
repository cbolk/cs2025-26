import pandas as pd

'''
pip install pandas
pip3 install pandas

for those who get the message "pip does not exist", use:
python -m pip install pandas

'''

### loading data from files

PAT_FILE = "./files/pd.trials.patient.csv"
TREA_FILE = "./files/pd.trials.treatment.csv"
PT_FILE = "./files/pd.trials.patient_treatment.csv"
LAB_FILE = "./files/pd.trials.lab_result.csv"

dfp = pd.read_csv(PAT_FILE) 
# patients = pd.read_csv(PAT_FILE)
dft = pd.read_csv(TREA_FILE)
# treatements = pd.read_csv(TREA_FILE)
dfpt = pd.read_csv(PT_FILE)
dfout = pd.read_csv(LAB_FILE)

# align/fix data types
dfp['EnrollDate'] = pd.to_datetime(dfp['EnrollDate'])
dfpt['StartDate'] = pd.to_datetime(dfpt['StartDate'])
dfout['VisitDate'] = pd.to_datetime(dfout['VisitDate'])

# Q. Find all patients age higher or equal to 40
df_res = dfp[dfp.Age >= 40]
# alternative writing style
df_res = dfp[dfp["Age"] >= 40]
# alternative use of a variable
filter_criteria = (dfp.Age >= 40)
df_res = dfp[filter_criteria]

# selecting a subset of the available information for all entries
dfp[['PID', 'Age', 'Sex']]

# Q. Find all IDs of patients age higher or equal to 40
df_res = dfp[dfp.Age >= 40][['PID']]

# Q. Find all *female* patients age higher or equal to 40
df_res = dfp[(dfp.Age >= 40) & (dfp.Sex == 'F')] ## not and

# Q. Find all patients age 40 or age 55
df_res = dfp[(dfp.Age == 40) | (dfp.Age == 55)] ## not or



# combine patients and treatments
dfpattreat = pd.merge(dfp, dfpt, on='PID', how='left')

# combine patients with a treatment
# dfpatwithtreat = pd.merge(dfp, dfpt, on='PID', how='inner')

dfpattreatdrug = pd.merge(dfpattreat, dft, on='TrtID', how='left')

# Q. average age of Males and Females

dfp.groupby(['Sex'])['Age'].mean().reset_index()














# saves on a file a dataframe content
dfp.to_csv("./files/result.csv", index=False)













