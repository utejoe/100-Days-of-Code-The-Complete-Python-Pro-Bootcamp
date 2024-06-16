import pandas as pd
import os

# Get the absolute path to the CSV file
current_dir = os.path.dirname(__file__)
csv_path = os.path.join(current_dir, 'weather_data.csv')

try:
    # Read the CSV file
    data = pd.read_csv(csv_path)
except FileNotFoundError as e:
    print(f"Error: {e}")
    print(f"Ensure the file 'weather_data.csv' exists in the directory: {current_dir}")
    exit(1)

# Check the type of the data object returned by Pandas
print(type(data))  # This should print: <class 'pandas.core.frame.DataFrame'>

# DataFrame and Series
# Extract the 'temp' column and check its type
temp_series = data['temp']
print(type(temp_series))  # This should print: <class 'pandas.core.series.Series'>

# Convert DataFrame to dictionary
data_dict = data.to_dict()
print("DataFrame as dictionary:", data_dict)

# Convert Series to list
temp_list = temp_series.to_list()
print("Temperature list:", temp_list)

# Calculate the average temperature using the list of temperatures
average_temp = sum(temp_list) / len(temp_list)
print("Average Temperature:", average_temp)

# Calculate the average temperature using Pandas' built-in method
average_temp_pandas = data['temp'].mean()
print("Average Temperature (Pandas):", average_temp_pandas)

# Find the maximum temperature
max_temp = data['temp'].max()
print("Maximum Temperature:", max_temp)

# Access specific columns in the DataFrame
print("Conditions (Method 1):", data['condition'])
print("Conditions (Method 2):", data.condition)

# Filter rows to get the row where the temperature is the maximum
max_temp_row = data[data['temp'] == data['temp'].max()]
print("Row with maximum temperature:", max_temp_row)

# Get Monday's temperature
monday_temp = data[data['day'] == 'Monday']['temp'].iloc[0]
print("Monday's Temperature:", monday_temp)

# Convert Monday's temperature from Celsius to Fahrenheit
monday_temp_F = monday_temp * 9/5 + 32
print("Monday's Temperature in Fahrenheit:", monday_temp_F)

# Create a DataFrame from scratch and save it to a CSV file
data_dict_new = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
new_data = pd.DataFrame(data_dict_new)
new_data.to_csv('new_data.csv', index=False)
print("New DataFrame created and saved to new_data.csv")
