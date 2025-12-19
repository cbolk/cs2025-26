############################################################
# PD Trials – Data analysis examples in R (dplyr / tidyverse)
############################################################

library(dplyr)
library(lubridate)

setwd("~/OneDrive - Politecnico di Milano/Misc/didattica/202526.cs/github/codice/")

WDIR = "~/OneDrive - Politecnico di Milano/Misc/didattica/202526.cs/github/codice/"

# File paths (same as in the Python example)
PATIENTS_FILE   <- file.path(WDIR, "files/pd.trials.patient.csv")
TREATMENTS_FILE <- file.path(WDIR, "files/pd.trials.treatment.csv")
PAT_TREA_FILE   <- file.path(WDIR, "files/pd.trials.patient_treatment.csv")
RESULTS_FILE    <- file.path(WDIR, "files/pd.trials.lab_result.csv")

# Load data --------------------------------------------------------------

dfp   <- read.csv(PATIENTS_FILE,   stringsAsFactors = FALSE)
dft   <- read.csv(TREATMENTS_FILE, stringsAsFactors = FALSE)
dfpt  <- read.csv(PAT_TREA_FILE,   stringsAsFactors = FALSE)
dfout <- read.csv(RESULTS_FILE,    stringsAsFactors = FALSE)

# Set dates with appropriate type
dfp$EnrollDate    <- as.Date(dfp$EnrollDate)
dfpt$StartDate    <- as.Date(dfpt$StartDate)
dfout$VisitDate   <- as.Date(dfout$VisitDate)

############################################################
# Q. List the last 10 patients who enrolled in the trial
############################################################

last_10_patients <- dfp %>%
  arrange(desc(EnrollDate)) %>%   # newest first
  head(10)

# or using slice_max:
# last_10_patients <- dfp %>% slice_max(order_by = EnrollDate, n = 10)


############################################################
# Q. Trials started in March, sorted by StartDate
#    (show TrtID and StartDate)
############################################################

trials_march <- dfpt %>%
  filter(month(StartDate) == 3) %>%
  arrange(StartDate) %>%
  select(TrtID, StartDate)


############################################################
# Q. List all enrolled patients with their ID, Sex, and DrugName
############################################################

# Combine patients and their trial information
dfptreat <- dfp %>%
  inner_join(dfpt, by = "PID")

# Add treatment info
dffull <- dfptreat %>%
  inner_join(dft, by = "TrtID")

result_pat_drug <- dffull %>%
  select(PID, Sex, DrugName)


############################################################
# Q. Patients over 60 on Metabolix: report ID and Age
############################################################

over60_metabolix <- dffull %>%
  filter(Age > 60, DrugName == "Metabolix") %>%
  select(PID, Age)


############################################################
# Q. Prescriptions at New York (NY-01):
#    list patient, drug, and dosage
############################################################

ny_prescriptions <- dffull %>%
  filter(SiteID == "NY-01") %>%
  select(PID, DrugName, Dosage_mg)


############################################################
# Q. Randomization check for Placebo group:
#    number of females and males
############################################################

# Get gender distribution in Placebo group
numPlaMF <- dffull %>%
  filter(DrugName == "Placebo") %>%
  count(Sex)

# Extract single numbers if you want variables
numPlaM <- numPlaMF$num[numPlaMF$Sex == "M"]
numPlaF <- numPlaMF$num[numPlaMF$Sex == "F"]


############################################################
# Q. Average Systolic Blood Pressure (Systolic_BP)
#    across entire population
############################################################

avgBloodPressure <- dfout %>%
  filter(TestName == "Systolic_BP") %>%
  summarise(avgBP = mean(Value, na.rm = TRUE)) %>%
  pull(avgBP)


############################################################
# Prepare combined table with treatments and lab results
#   (used in several questions below)
############################################################

dftpout <- dfpt %>%
  inner_join(dfout, by = "PID") %>%
  inner_join(dft, by = "TrtID")


############################################################
# Q. Compare study arms: average HbA1c by DrugName
############################################################

df_hba1c <- dftpout %>%
  filter(TestName == "HbA1c")

dfres_hba1c <- df_hba1c %>%
  group_by(DrugName) %>%
  summarise(avgHbA1c = mean(Value, na.rm = TRUE), .groups = "drop")


############################################################
# Q. Highest LDL value for any patient in Experimental arm
############################################################

protocol <- "Experimental"

highest_ldl <- dftpout %>%
  filter(TestName == "LDL", StudyArm == protocol) %>%
  summarise(max_LDL = max(Value, na.rm = TRUE)) %>%
  pull(max_LDL)


############################################################
# Q. Baseline data: lab results before StartDate
#    (list LabID, TestName, Value, VisitDate, StartDate)
############################################################

baseline_data <- dftpout %>%
  filter(VisitDate < StartDate) %>%
  select(LabID, TestName, Value, VisitDate, StartDate)


############################################################
# Q. Average days between Enrollment Date and Start Date
#    by SiteID
############################################################

dffull_delta <- dffull %>%
  mutate(
    deltaDays = as.integer(StartDate - EnrollDate)
  )

dfDeltaDays <- dffull_delta %>%
  group_by(SiteID) %>%
  summarise(avgDeltaDays = mean(deltaDays, na.rm = TRUE),
            .groups = "drop")


############################################################
# Q. For Metabolix users: difference in average Weight_kg
#    between Male and Female
############################################################

# Join to get Sex information
dfall <- dftpout %>%
  inner_join(dfp, by = "PID")

metabolix_weight <- dfall %>%
  filter(DrugName == "Metabolix", TestName == "Weight_kg")

avgWeight_by_sex <- metabolix_weight %>%
  group_by(Sex) %>%
  summarise(avgWeight = mean(Value, na.rm = TRUE),
            .groups = "drop")


############################################################
# Q. List PIDs with Systolic BP > 160 OR LDL > 150
############################################################

highRisk <- dftpout %>%
  filter(
    (TestName == "Systolic_BP" & Value > 160) |
      (TestName == "LDL" & Value > 150)
  )

highRisk_pids <- unique(highRisk$PID)

############################################################
# End of R example file
############################################################
