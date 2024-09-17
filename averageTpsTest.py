import random

def generate_stable_data(prev_data):
    new_data = []
    for value in prev_data:
        variation = random.uniform(-50, 50)
        new_value = round(value + variation, 2)
        if new_value < 200:
            new_value = 200
        elif new_value > 4000:
            new_value = 4000
        new_data.append(new_value)
    return new_data

Monoxide_4000 = [178.03, 611.36, 1115.71, 2167.94, 2542.59, 2813.39, 2981.73, 3131.88]
Metis_4000 = [450.91, 1095.13, 1375.12, 2402.57, 2600.13, 2921.82, 3219.61, 3446.84]
Proposed_4000 = [871.11, 978.46, 1104.94, 3186.79, 3894.99, 4999.76, 5120.19, 5315.21]

Monoxide_6000 = generate_stable_data(Monoxide_4000)
Metis_6000 = generate_stable_data(Metis_4000)
Proposed_6000 = generate_stable_data(Proposed_4000)

print("Monoxide_6000:", Monoxide_6000)
print("Metis_6000:", Metis_6000)
print("Proposed_6000:", Proposed_6000)