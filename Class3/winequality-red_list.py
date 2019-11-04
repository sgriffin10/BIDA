
# Import the module to read the CSV file
import csv

# Open the CSV file and read all of the data into a Python list
with open('Class3/winequality-red.csv', 'r') as f:
    wines = list(csv.reader(f, delimiter=';'))
# Print out the first three rows
print(wines[:3])

# Remove the header row
wines = wines[1:]

# Create a new list called qualities
qualities = []
for item in wines:
    qualities.append(float(item[-1]))

# Print the average of all the elements in the list
print(sum(qualities) / len(qualities))