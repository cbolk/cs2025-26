import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Caricamento (assumendo il file nella stessa cartella)
df = pd.read_csv('noshow.csv')

# Pulizia preliminare nomi colonne
df.rename(columns={'Hipertension': 'Hypertension', 'Handcap': 'Handicap'}, inplace=True)

# Conversione date (Per Studente A)
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])

# Esempio Visualizzazione (Per Studente B)
sns.countplot(x='No-show', data=df)
plt.title('Distribuzione Assenze vs Presenze')
plt.show()
