import os.path
import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob

dir = 'D:\code\\njust\\block-emulator\\test\\newTest'
# 获取所有文件名
files = glob.glob(f"{dir}/*_sn_*.csv")

# 存储不同分片方式的数据
default_sharding = {}
clpa_sharding = {}
cpla_plus_sharding = {}
v = 1.0
weight = 0.0
for file in files:
    df = pd.read_csv(file)
    print(f"Reading file: {file}")
    # 提取文件中的数值部分作为标识
    fileName = os.path.basename(file)
    base_name_without_extension = os.path.splitext(fileName)[0]
    weight = float(base_name_without_extension.split('_sn_')[0])
    if weight != v:
        continue
    key = int(base_name_without_extension.split('_sn_')[1])
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

yticks_positions = [i * 0.1 for i in range(11)]

# all_txs_values = [10000, 50000, 100000, 200000, 400000, 800000, 1000000]
all_txs_values = clpa_sharding[list(clpa_sharding.keys())[0]].keys()
# 创建一个3行1列的子图布局
fig, axs = plt.subplots(nrows=len(all_txs_values), ncols=1, figsize=(8, 12), sharex=True)
# 遍历all_txs值，为每个值创建一个子图
for idx, txs in enumerate(all_txs_values):
    # 获取当前子图对象
    ax = axs[idx]

    ax.plot(sorted(clpa_sharding.keys()),
            [float(clpa_sharding[k][txs]['Cross-Shard txs Reduction Ratio']) for k in sorted(clpa_sharding.keys())],
            label='clpa_sharding')
    # 绘制曲线
    ax.plot(sorted(cpla_plus_sharding.keys()),
            [float(cpla_plus_sharding[k][txs]['Cross-Shard txs Reduction Ratio']) for k in sorted(cpla_plus_sharding.keys())],
            label='current')

    # 设置子图的标题
    ax.set_title(f'all_txs = {txs}')

    # 设置y轴标签
    # ax.set_ylabel('Cross-Shard txs Reduction Ratio')
    ax.set_yticks(yticks_positions)
    ax.legend()
    ax.grid(True)


# 设置x轴标签和标题
axs[len(all_txs_values) - 1].set_xlabel('Number of Shards')
axs[len(all_txs_values) - 1].set_ylabel('Cross-Shard txs Reduction Ratio')
fig.suptitle(f'weight = {v}')

# 显示图例
axs[len(all_txs_values) - 1].legend()
plt.xticks(sorted(default_sharding.keys()))

# plt.yticks(yticks_positions)
plt.ylim(0, 1)
plt.legend()
plt.grid(True)
# 显示图形
plt.show()
