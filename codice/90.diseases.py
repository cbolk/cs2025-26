SEVERITY = 5

FNAME_D = "./sourcefile/files/pd.disease.csv"
FNAME_S = "./sourcefile/files/pd.symptom.csv"
FNAME_DP = "./sourcefile/files/pd.disease_precaution.csv"
FNAME_DS = "./sourcefile/files/pd.disease_symptom.csv"

# Q1

dfd = pd.csv_read(FNAME_D)
dfs = pd.csv_read(FNAME_S)
dfdp = pd.csv_read(FNAME_DP)
dfds = pd.csv_read(FNAME_DS)

# Q2

df.info()

print(df.describe())

dfs_sev = dfs[dfs.Weight >= 5]
dfs_sev = dfs_sev.reset_index()
dfs_sev = dfs_sev.drop(columns=['index'])

# Q3

dfs_sev = dfs[dfs.Weight >= 5]
dfs_sev = dfs_sev.reset_index(drop=True)
```

# Q4 Create a tidy dataframe for the diseases and symptoms.

dfd_t = pd.melt(dfds,
                var_name='SymptomNum',
                value_name='Symptom',
                id_vars='Disease')
