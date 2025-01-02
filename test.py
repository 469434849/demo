import numpy as np

# Data input as rows
# Updated data with corrected values (each row adjusted as per user input)
updated_data = [
    [0.84, 0.78, 0.74, 0.76, 0.67],
    [78.90, 219.90, 1328.9, 2567.9, 3192.3],
    [0.81, 0.72, 0.68, 0.7, 0.58],
    [122.35, 275.68, 2300.1, 3925.7, 4352.4],
    [0.73, 0.68, 0.64, 0.55, 0.52],
    [230.12, 718.90, 4668.9, 7122.4, 9150.1],
    [0.92, 0.82, 0.77, 0.79, 0.69],
    [1.02, 8.68, 16.35, 23.90, 28.23],
    [0.87, 0.77, 0.72, 0.77, 0.62],
    [10.35, 31.02, 47.68, 220.46, 290.89],
    [0.82, 0.7, 0.66, 0.55, 0.53],
    [122.01, 331.35, 611.23, 840.99, 982.35]
]

# Recalculating averages for corrected data
updated_averages = [round(np.mean(row), 2) for row in updated_data]
updated_averages


# Display results
print(updated_averages)
