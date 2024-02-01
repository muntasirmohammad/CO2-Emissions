import csv
import pandas as pd
import matplotlib.pyplot as plt

def is_number(s) -> bool:
    """Check if a string can be converted into a float"""
    # Try to convert string to float, if converted, return True
    try:
        x = float(s)
        return True
    # If string cannot be converted to float, return False
    except ValueError:
        return False

# Converting the csv file to a dictionary
with open("CO2 Emissions.csv", "r") as file:
    reader = csv.DictReader(file)
    data = {}
    # Go through each row
    for row in reader:
        # Go through each column in row
        # Check for Column name existence in dictionary
        # Add the values into a list as the value to the column name
        for key in row:
            if key not in data:
                if is_number(row[key]):
                    data[key] = [float(row[key])]
                else:
                    data[key] = [row[key]]
            else:
                if is_number(row[key]):
                    data[key].append(float(row[key]))
                else:
                    data[key].append(row[key])
df = pd.DataFrame(data)
selected_columns = ["Transmission", "CO2 Emissions(g/km)"]
selected_df = df[selected_columns]
grouped = selected_df.groupby('Transmission')['CO2 Emissions(g/km)'].mean()

# Create bar plot
plt.figure(figsize=(10, 6))
grouped.plot(kind='bar')
plt.title('Average CO2 Emissions by Transmission')
plt.xlabel('Transmission')
plt.ylabel('Average CO2 Emissions (g/km)')
plt.grid(True)
plt.tight_layout()
# Show the plot after we close the last plot
plt.show()
