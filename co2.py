import numpy as np
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

df["decade"] = (df["year"] // 10) * 10
# For each decade, compute a least-squares fit line and plot
for decade, group_df in df.groupby("decade"):
    # For regression, use the "decimal_date" column (e.g. 1958.2877) as x
    x = group_df["decimal_date"].values
    y = group_df["monthly_avg"].values
    # Skip if there's too little data
    if len(x) < 2:
        continue
    # Fit a first-degree polynomial (linear fit): slope, intercept
    slope, intercept = np.polyfit(x, y, 1)
    # Generate a smooth x-range from min to max of the decade's decimal dates
    x_fit = np.array([x.min(), x.max()+1])
    # Corresponding y-values based on the linear fit
    y_fit = slope * x_fit + intercept
    # Convert this x_fit back to a "float year" → approximate Date
    # (Only for the legend labeling we will use the decade in the text.)
    # Plot the fit line
    plt.plot(
        pd.to_datetime(x_fit, format="%Y"),  # Approximates creating a datetime from a float year,
        y_fit,
        linestyle='-',
        label=f"Linear fit {decade}s: {slope:.1f}x + {intercept:.0f}"
    )

plt.xlabel("Date")
plt.ylabel("CO₂ Concentration (ppm)")
plt.title("Mauna Loa CO₂ Concentration")
plt.grid(True)
plt.legend()

plt.show()
