import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False     # 正常显示负号

dir = 'D:\\code\\njust\\block-emulator\\test\\NewTest5'
# 获取所有文件名
files = glob.glob(f"{dir}/*_sn_*.csv")

# 存储不同分片方式的数据
default_sharding = {}
clpa_sharding = {}
cpla_plus_sharding = {}

# 读取每个 CSV 文件的数据
for file in files:
    df = pd.read_csv(file)
    print(f"Reading file: {file}")
    # 提取文件中的数值部分作为标识
    fileName = os.path.basename(file)
    base_name_without_extension = os.path.splitext(fileName)[0]
    weight = float(base_name_without_extension.split('_sn_')[0])
    if weight != 0.7:
        continue
    key = int(base_name_without_extension.split('_sn_')[1])
    if key not in default_sharding:
        default_sharding[key] = {}
    if key not in clpa_sharding:
        clpa_sharding[key] = {}
    if key not in cpla_plus_sharding:
        cpla_plus_sharding[key] = {}

    for idx, row in df.iterrows():
        if row['all_txs'] not in [10000, 20000]:
            continue
        if idx % 4 == 1:
            default_sharding[key][row['all_txs']] = df.iloc[idx]
        if idx % 4 == 2:
            clpa_sharding[key][row['all_txs']] = df.iloc[idx]
        if idx % 4 == 3:
            cpla_plus_sharding[key][row['all_txs']] = df.iloc[idx]

# all_txs_values = [10000, 50000, 100000, 200000, 400000, 800000, 1000000]
all_txs_values = clpa_sharding[list(clpa_sharding.keys())[0]].keys()
# 创建一个5行2列的子图布局
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(20, 10), sharex=True)

# Flatten the axs array for easier indexing
axs = axs.flatten()

# 遍历all_txs值，为每个值创建一个子图
for idx, txs in enumerate(all_txs_values):
    ax1 = axs[idx * 2]
    ax2 = axs[idx * 2 + 1]

    # 绘制第一列的子图
    txs_data_default = [default_sharding[k][txs]['variance'] for k in sorted(default_sharding.keys())]
    txs_data_clpa = [clpa_sharding[k][txs]['variance'] for k in sorted(clpa_sharding.keys())]
    txs_data_cpla_plus = [cpla_plus_sharding[k][txs]['variance'] for k in sorted(cpla_plus_sharding.keys())]

    ax1.plot(sorted(default_sharding.keys()), txs_data_default, label='考虑节点账户关系的分片算法', marker='o')
    ax1.plot(sorted(clpa_sharding.keys()), txs_data_clpa, label='本发明', marker='>')
    # ax1.plot(sorted(cpla_plus_sharding.keys()), txs_data_cpla_plus, label='current')

    ax1.set_title(f'总交易量 = {txs}', fontsize=20)
    ax1.set_ylabel('负载因子', fontsize=20)
    ax1.set_xlabel('分片数', fontsize=20)
    ax1.legend()
    ax1.grid(True)

    # 绘制第二列的子图
    txs_ratio_default = [float(default_sharding[k][txs]['Cross-Shard txs Reduction Ratio']) for k in
                         sorted(default_sharding.keys())]
    txs_ratio_clpa = [float(clpa_sharding[k][txs]['Cross-Shard txs Reduction Ratio']) for k in
                      sorted(clpa_sharding.keys())]
    txs_ratio_cpla_plus = [float(cpla_plus_sharding[k][txs]['Cross-Shard txs Reduction Ratio']) for k in
                           sorted(cpla_plus_sharding.keys())]

    ax2.plot(sorted(default_sharding.keys()), txs_ratio_default, label='考虑节点账户关系的分片算法', marker='o')
    ax2.plot(sorted(clpa_sharding.keys()), txs_ratio_clpa, label='本发明', marker='>')
    # ax2.plot(sorted(cpla_plus_sharding.keys()), txs_ratio_cpla_plus, label='current')

    ax2.set_title(f'总交易量 = {txs}', fontsize=20)
    ax2.set_ylabel('跨分片交易减少比例', fontsize=20)
    ax2.set_xlabel('分片数', fontsize=20)
    ax2.legend()
    ax2.grid(True)

# 设置全局标题
fig.suptitle('不同的交易量下负载因子和跨分片交易减少比例与分片数的关系', fontsize=20)

# 调整布局防止重叠
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.xticks([2, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52])

# 显示图形
plt.show()
