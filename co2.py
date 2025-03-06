import pandas as pd
import matplotlib.pyplot as plt

# The file is provided in the repository as a backup as well
filename = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.txt"

df = pd.read_csv(
    filename,
    comment="#",
    delim_whitespace=True,
    header=None,
    names=["year", "month", "decimal_date", "monthly_avg",
           "de_seasonalized", "days", "stdev", "uncertainty"]
)

# Create a Date column (arbitrarily using day=15 for each month)
df["Date"] = pd.to_datetime(
    df["year"].astype(int).astype(str) + "-" +
    df["month"].astype(int).astype(str) + "-15"
)

plt.figure(figsize=(10, 6))

plt.plot(df["Date"], df["monthly_avg"], 'k-')

plt.xlabel("Date")
plt.ylabel("CO₂ Concentration (ppm)")
plt.title("Mauna Loa CO₂ Concentration")
plt.grid(True)

plt.show()
