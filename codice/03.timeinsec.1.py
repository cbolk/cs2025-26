# CONSTANT / ARBITRARY ASPECTS OF THE SOLUTION
SEC_IN_MIN = 60
MIN_IN_HR = 60
SEC_IN_HR = (SEC_IN_MIN * MIN_IN_HR)

# DATA ACQUISITION
timesec = int(input())

# COMPUTATION
num_hr = timesec // SEC_IN_HR
timerem = timesec % SEC_IN_HR
num_min = timerem // SEC_IN_MIN
num_sec = timerem % SEC_IN_MIN

# VISUALISATION
print(num_hr, num_min, num_sec)
