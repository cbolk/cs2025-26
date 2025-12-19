import pandas as pd
import matplotlib.pyplot as plt

mice = pd.read_csv("teamwork.pymaceuticals.mice.csv")
results = pd.read_csv("teamwork.pymaceuticals.studies.csv")

df = pd.merge(results, mice, on="Mouse ID")

dups = df[df.duplicated(subset=["Mouse ID", "Timepoint"], keep=False)]
print("Number of duplicate rows (Mouse ID + Timepoint):", len(dups))

# Optionally remove these duplicates
df = df.drop_duplicates(subset=["Mouse ID", "Timepoint"], keep="first")

## BARCHART
# Count measurements per drug regimen
measure_counts = df["Drug Regimen"].value_counts().sort_index()

print(measure_counts)

plt.figure(figsize=(8, 5))
plt.bar(measure_counts.index, measure_counts.values)

plt.title("Number of tumor measurements per drug regimen")
plt.xlabel("Drug regimen")
plt.ylabel("Number of measurements")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

## LINECHART

# Filter for one regimen, e.g., Capomulin
capomulin_df = df[df["Drug Regimen"] == "Capomulin"]

# Pick first mouse ID in that regimen
example_mouse_id = capomulin_df["Mouse ID"].iloc[0]
print("Example mouse:", example_mouse_id)

# Extract that mouse's data and sort by time
mouse_trend = df[df["Mouse ID"] == example_mouse_id].sort_values("Timepoint")
display(mouse_trend)
plt.figure(figsize=(8, 5))
plt.plot(mouse_trend["Timepoint"], mouse_trend["Tumor Volume (mm3)"], marker="o")

plt.title(f"Tumor volume over time for mouse {example_mouse_id} (Capomulin)")
plt.xlabel("Timepoint (days)")
plt.ylabel("Tumor volume (mm³)")
plt.tight_layout()
plt.show()


## BOXPLOT
# Compute max timepoint per mouse
final_tp = df.groupby("Mouse ID")["Timepoint"].max()

# Merge back to get only final rows
df_final = pd.merge(df, final_tp, on=["Mouse ID", "Timepoint"], how="inner")

# Choose a subset of regimens to highlight
selected = ["Capomulin", "Ramicane", "Infubinol", "Ceftamin"]

# Prepare data for boxplot: one list per regimen
box_data = [
    df_final.loc[df_final["Drug Regimen"] == regimen, "Tumor Volume (mm3)"]
    for regimen in selected
]

plt.figure(figsize=(8, 5))
plt.boxplot(box_data, labels=selected)

plt.title("Final tumor volume by drug regimen")
plt.ylabel("Tumor volume (mm³)")
plt.tight_layout()
plt.show()


## SCATTERPLOT

# Reuse df_final: final-timepoint per mouse
# Focus on Capomulin again (or any other regimen)
cap_final = df_final[df_final["Drug Regimen"] == "Capomulin"]

print("Final data for Capomulin:")
display(cap_final[["Mouse ID", "Weight (g)", "Tumor Volume (mm3)"]].head())

plt.figure(figsize=(8, 5))
plt.scatter(cap_final["Weight (g)"], cap_final["Tumor Volume (mm3)"])

plt.title("Final tumor volume vs. weight (Capomulin)")
plt.xlabel("Weight (g)")
plt.ylabel("Tumor volume (mm³)")
plt.tight_layout()
plt.show()
