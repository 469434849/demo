import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

dir = './NewTest5'
files = glob.glob(f"{dir}/*_sn_*.csv")

default_sharding = {}
clpa_sharding = {}
cpla_plus_sharding = {}

for file in files:
    df = pd.read_csv(file)
    print(f"Reading file: {file}")
    fileName = os.path.basename(file)
    base_name_without_extension = os.path.splitext(fileName)[0]
    weight = float(base_name_without_extension.split('_sn_')[0])
    if weight != 0.7:
        continue
    key = int(base_name_without_extension.split('_sn_')[1])

    for shard_type, shard_dict in zip(['default', 'clpa', 'cpla_plus'],
                                      [default_sharding, clpa_sharding, cpla_plus_sharding]):
        if key not in shard_dict:
            shard_dict[key] = {}

    for idx, row in df.iterrows():
        if row['all_txs'] not in [10000, 20000]:
            continue
        if idx % 4 == 1:
            default_sharding[key][row['all_txs']] = df.iloc[idx]
        elif idx % 4 == 2:
            clpa_sharding[key][row['all_txs']] = df.iloc[idx]
        elif idx % 4 == 3:
            cpla_plus_sharding[key][row['all_txs']] = df.iloc[idx]

all_txs_values = clpa_sharding[list(clpa_sharding.keys())[0]].keys()

# 分别绘制负载因子和跨分片交易减少比例的图表
for idx, txs in enumerate(all_txs_values):
    # 绘制负载因子的图表
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    txs_data_default = [default_sharding[k][txs]['variance'] for k in sorted(default_sharding.keys())]
    txs_data_clpa = [clpa_sharding[k][txs]['variance'] for k in sorted(clpa_sharding.keys())]

    ax1.plot(sorted(default_sharding.keys()), txs_data_default, label='考虑节点账户关系的分片算法', marker='o')
    ax1.plot(sorted(clpa_sharding.keys()), txs_data_clpa, label='本发明', marker='>')
    ax1.set_title(f'总交易量 = {txs}, 负载因子', fontsize=20)
    ax1.set_ylabel('负载因子', fontsize=20)
    ax1.set_xlabel('分片数', fontsize=20)
    ax1.legend()
    ax1.grid(True)
    plt.show()

    # 绘制跨分片交易减少比例的图表
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    txs_ratio_default = [float(default_sharding[k][txs]['Cross-Shard txs Reduction Ratio']) for k in
                         sorted(default_sharding.keys())]
    txs_ratio_clpa = [float(clpa_sharding[k][txs]['Cross-Shard txs Reduction Ratio']) for k in
                      sorted(clpa_sharding.keys())]

    ax2.plot(sorted(default_sharding.keys()), txs_ratio_default, label='考虑节点账户关系的分片算法', marker='o')
    ax2.plot(sorted(clpa_sharding.keys()), txs_ratio_clpa, label='本发明', marker='>')
    ax2.set_title(f'总交易量 = {txs}, 跨分片交易减少比例', fontsize=20)
    ax2.set_ylabel('跨分片交易减少比例', fontsize=20)
    ax2.set_xlabel('分片数', fontsize=20)
    ax2.legend()
    ax2.grid(True)
    plt.show()
