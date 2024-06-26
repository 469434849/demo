import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 示例数据
data = [10000, 20, 30, 40, 50]

# 将数据转换为NumPy数组
data = np.array(data)

# 归一化处理
min_val = np.min(data)
max_val = np.max(data)
normalized_data = (data - min_val) / (max_val - min_val)

# 计算归一化数据的方差
normalized_variance = np.var(normalized_data)

print("原始数据：", data)
print("归一化后的数据：", normalized_data)
print("归一化数据的方差：", normalized_variance)

# 绘制原始数据和归一化数据的图表
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(data, label='Original Data', marker='o')
plt.title('Original Data')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(normalized_data, label='Normalized Data', marker='o')
plt.title('Normalized Data')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()

plt.tight_layout()
plt.show()
