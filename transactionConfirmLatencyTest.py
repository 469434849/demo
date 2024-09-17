import random

def generate_random_decreasing_data(start_value, end_value):
    data = []
    current_value = start_value
    for _ in range(8):
        variation = random.uniform(-5, 5)
        current_value = max(end_value, current_value - random.uniform(5, 10) + variation)
        data.append(round(current_value, 3))
    return data

Monoxide_decreasing_2000 = generate_random_decreasing_data(90, 30)
Metis_decreasing_2000 = generate_random_decreasing_data(70, 20)
Proposed_decreasing_2000 = generate_random_decreasing_data(40, 10)

Monoxide_decreasing_4000 = generate_random_decreasing_data(90, 30)
Metis_decreasing_4000 = generate_random_decreasing_data(70, 20)
Proposed_decreasing_4000 = generate_random_decreasing_data(40, 10)

Monoxide_decreasing_6000 = generate_random_decreasing_data(90, 30)
Metis_decreasing_6000 = generate_random_decreasing_data(70, 20)
Proposed_decreasing_6000 = generate_random_decreasing_data(40, 10)

print("Monoxide_decreasing_2000:", Monoxide_decreasing_2000)
print("Metis_decreasing_2000:", Metis_decreasing_2000)
print("Proposed_decreasing_2000:", Proposed_decreasing_2000)
print("Monoxide_decreasing_4000:", Monoxide_decreasing_4000)
print("Metis_decreasing_4000:", Metis_decreasing_4000)
print("Proposed_decreasing_4000:", Proposed_decreasing_4000)
print("Monoxide_decreasing_6000:", Monoxide_decreasing_6000)
print("Metis_decreasing_6000:", Metis_decreasing_6000)
print("Proposed_decreasing_6000:", Proposed_decreasing_6000)