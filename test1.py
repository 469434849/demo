import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob

dir = 'D:\code\\njust\\block-emulator\\test'
# 获取所有文件名
files = glob.glob(f"{dir}/0.70_sn_*.csv")

# 存储不同分片方式的数据
default_sharding = {}
clpa_sharding = {}
cpla_plus_sharding = {}

# 读取每个 CSV 文件的数据
for file in files:
    df = pd.read_csv(file)
    print(f"Reading file: {file}")
    # 提取文件中的数值部分作为标识
    key = int(file.split('_')[-1].split('.')[0])
    if key not in default_sharding:
        default_sharding[key] = {}
    if key not in clpa_sharding:
        clpa_sharding[key] = {}
    if key not in cpla_plus_sharding:
        cpla_plus_sharding[key] = {}

    for idx, row in df.iterrows():
        # print(f"Row index: {idx}, Data: {row}\n")
        if idx % 3 == 0:
            default_sharding[key][row['all_txs']] = df.iloc[idx]
        if idx % 3 == 1:
            clpa_sharding[key][row['all_txs']] = df.iloc[idx]
        if idx % 3 == 2:
            cpla_plus_sharding[key][row['all_txs']] = df.iloc[idx]
print(default_sharding)
print(clpa_sharding)
print(cpla_plus_sharding)
# 创建绘图
plt.figure(figsize=(12, 8))

# 选择一列数据进行绘图，这里假设有一个列名为 'variance' (根据实际列名调整)
# plt.plot(sorted(default_sharding.keys()),
#          [default_sharding[k][10000]['variance'] for k in sorted(default_sharding.keys())],
#          label='Default Sharding')
plt.plot(sorted(clpa_sharding.keys()), [clpa_sharding[k][10000]['variance'] for k in sorted(clpa_sharding.keys())],
         label='CLPA Sharding')
plt.plot(sorted(cpla_plus_sharding.keys()),
         [cpla_plus_sharding[k][10000]['variance'] for k in sorted(cpla_plus_sharding.keys())],
         label='CPLA_PLUS Sharding')

plt.xticks(sorted(default_sharding.keys()))
plt.xlabel('Number of Shards')
plt.ylabel('variance')
plt.title('Throughput Comparison for Different Sharding Methods')
plt.legend()
plt.grid(True)
plt.show()
