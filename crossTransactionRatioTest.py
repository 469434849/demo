import numpy as np

def generate_increasing_data(start_value, end_value):
    data = np.linspace(start_value, end_value, num=5)
    return [round(d, 3) for d in data]

# Generate data for each combination
Monoxide_increasing_2000 = {8: generate_increasing_data(0.80, 0.98)[0],
                            16: generate_increasing_data(0.80, 0.98)[1],
                            32: generate_increasing_data(0.80, 0.98)[2],
                            48: generate_increasing_data(0.80, 0.98)[3],
                            64: generate_increasing_data(0.80, 0.98)[4]}

Metis_increasing_2000 = {8: generate_increasing_data(0.62, 0.89)[0],
                         16: generate_increasing_data(0.62, 0.89)[1],
                         32: generate_increasing_data(0.62, 0.89)[2],
                         48: generate_increasing_data(0.62, 0.89)[3],
                         64: generate_increasing_data(0.62, 0.89)[4]}

Proposed_increasing_2000 = {8: generate_increasing_data(0.18, 0.38)[0],
                            16: generate_increasing_data(0.18, 0.38)[1],
                            32: generate_increasing_data(0.18, 0.38)[2],
                            48: generate_increasing_data(0.18, 0.38)[3],
                            64: generate_increasing_data(0.18, 0.38)[4]}

Monoxide_increasing_4000 = {8: generate_increasing_data(0.80, 0.98)[0],
                            16: generate_increasing_data(0.80, 0.98)[1],
                            32: generate_increasing_data(0.80, 0.98)[2],
                            48: generate_increasing_data(0.80, 0.98)[3],
                            64: generate_increasing_data(0.80, 0.98)[4]}

Metis_increasing_4000 = {8: generate_increasing_data(0.62, 0.89)[0],
                         16: generate_increasing_data(0.62, 0.89)[1],
                         32: generate_increasing_data(0.62, 0.89)[2],
                         48: generate_increasing_data(0.62, 0.89)[3],
                         64: generate_increasing_data(0.62, 0.89)[4]}

Proposed_increasing_4000 = {8: generate_increasing_data(0.18, 0.38)[0],
                            16: generate_increasing_data(0.18, 0.38)[1],
                            32: generate_increasing_data(0.18, 0.38)[2],
                            48: generate_increasing_data(0.18, 0.38)[3],
                            64: generate_increasing_data(0.18, 0.38)[4]}

Monoxide_increasing_6000 = {8: generate_increasing_data(0.80, 0.98)[0],
                            16: generate_increasing_data(0.80, 0.98)[1],
                            32: generate_increasing_data(0.80, 0.98)[2],
                            48: generate_increasing_data(0.80, 0.98)[3],
                            64: generate_increasing_data(0.80, 0.98)[4]}

Metis_increasing_6000 = {8: generate_increasing_data(0.62, 0.89)[0],
                         16: generate_increasing_data(0.62, 0.89)[1],
                         32: generate_increasing_data(0.62, 0.89)[2],
                         48: generate_increasing_data(0.62, 0.89)[3],
                         64: generate_increasing_data(0.62, 0.89)[4]}

Proposed_increasing_6000 = {8: generate_increasing_data(0.18, 0.38)[0],
                            16: generate_increasing_data(0.18, 0.38)[1],
                            32: generate_increasing_data(0.18, 0.38)[2],
                            48: generate_increasing_data(0.18, 0.38)[3],
                            64: generate_increasing_data(0.18, 0.38)[4]}

# Print the results without np.float64
print("Monoxide_increasing_2000:", {k: float(str(v)) for k, v in Monoxide_increasing_2000.items()})
print("Metis_increasing_2000:", {k: float(str(v)) for k, v in Metis_increasing_2000.items()})
print("Proposed_increasing_2000:", {k: float(str(v)) for k, v in Proposed_increasing_2000.items()})
print("Monoxide_increasing_4000:", {k: float(str(v)) for k, v in Monoxide_increasing_4000.items()})
print("Metis_increasing_4000:", {k: float(str(v)) for k, v in Metis_increasing_4000.items()})
print("Proposed_increasing_4000:", {k: float(str(v)) for k, v in Proposed_increasing_4000.items()})
print("Monoxide_increasing_6000:", {k: float(str(v)) for k, v in Monoxide_increasing_6000.items()})
print("Metis_increasing_6000:", {k: float(str(v)) for k, v in Metis_increasing_6000.items()})
print("Proposed_increasing_6000:", {k: float(str(v)) for k, v in Proposed_increasing_6000.items()})