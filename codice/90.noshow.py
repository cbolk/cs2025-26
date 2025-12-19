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


# Convertiamo le stringhe in oggetti datetime
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay']).dt.normalize()
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay']).dt.normalize()

# Creiamo la nuova feature: Giorni di Attesa
# (Data Visita - Data Prenotazione)
df['WaitingDays'] = (df['AppointmentDay'] - df['ScheduledDay']).dt.days

# Gestione minima: Rimuoviamo eventuali attese negative (errori di inserimento)
df = df[df['WaitingDays'] >= 0]

# --- 3. ANALISI VISUALE E STATISTICA ---

# A. ANALISI GLOBALE (Baseline)
plt.figure(figsize=(6, 4))
ax = sns.countplot(x='No-show', data=df, palette='viridis')
plt.title("Distribuzione Totale: Chi si presenta vs No-Show")
# Calcolo percentuali
total = len(df)
for p in ax.patches:
    percentage = '{:.1f}%'.format(100 * p.get_height()/total)
    x = p.get_x() + p.get_width() / 2 - 0.05
    y = p.get_height()
    ax.annotate(percentage, (x, y), ha='center')
plt.show()

# B. THE "COLD FEET" THEORY (Impatto del Tempo di Attesa)
# Usiamo un Boxplot per vedere se chi non si presenta ha attese più lunghe
plt.figure(figsize=(10, 6))
# Limitiamo a 60 giorni per evitare che gli outlier schiaccino il grafico
sns.boxplot(x='No-show', y='WaitingDays', data=df[df['WaitingDays'] < 60], palette="Set2")
plt.title("The Cold Feet Theory: Giorni di Attesa vs Assenza")
plt.ylabel("Giorni tra Prenotazione e Visita")
plt.show()

print("\n--- INSIGHT 1: TEMPI DI ATTESA ---")
print(df.groupby('No-show')['WaitingDays'].mean())


# C. THE SMS FACTOR (Impatto degli SMS)
# Creiamo un grafico a barre normalizzato per vedere le proporzioni
plt.figure(figsize=(8, 5))
# Tabella incrociata normalizzata
sms_prop = pd.crosstab(df['SMS_received'], df['No-show'], normalize='index')
sms_prop.plot(kind='bar', stacked=True, color=['green', 'red'], alpha=0.7)
plt.title("Efficacia degli SMS: Tasso di No-Show con e senza SMS")
plt.xlabel("SMS Ricevuto (0=No, 1=Sì)")
plt.ylabel("Proporzione")
plt.legend(title='No-show', loc='upper right')
plt.show()


# D. DEMOGRAFIA E PATOLOGIE (Età e Condizioni)
# 1. Distribuzione Età
plt.figure(figsize=(10, 5))
sns.kdeplot(data=df, x="Age", hue="No-show", fill=True, common_norm=False, palette="crest")
plt.title("Distribuzione dell'Età per Presenze vs Assenze")
plt.xlim(0, 100)
plt.show()

# 2. Correlazione Patologie (Diabete)
plt.figure(figsize=(6, 4))
sns.barplot(x='Diabetes', y='WaitingDays', hue='No-show', data=df, estimator=lambda x: len(x) / len(df) * 100)
# Nota: Questo grafico sopra è complesso, semplifichiamo con un catplot semplice
sns.catplot(x="Diabetes", hue="No-show", kind="count", data=df, height=5, aspect=1.5, palette="pastel")
plt.title("Assenze tra Pazienti Diabetici vs Non Diabetici")
plt.show()

# --- 4. EXECUTIVE SUMMARY (Output Console) ---
print("\n--- EXECUTIVE SUMMARY PER IL DIRETTORE ---")
total_noshow = df[df['No-show'] == 'Yes'].shape[0]
rate_noshow = (total_noshow / total) * 100
print(f"1. Tasso Globale di No-Show: {rate_noshow:.2f}%")
print(f"2. Attesa Media: {df[df['No-show']=='Yes']['WaitingDays'].mean():.1f} giorni (Assenti) vs {df[df['No-show']=='No']['WaitingDays'].mean():.1f} giorni (Presenti).")
print("3. Analisi completata. Grafici generati.")