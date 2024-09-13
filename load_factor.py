
import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# dir = 'D:\\code\\njust\\block-emulator\\test\\NewTest5'
dir = './NewTest5'
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
    if weight!= 0.7:
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

all_txs_values = clpa_sharding[list(clpa_sharding.keys())[0]].keys()
all_txs_values = [20000]

# 绘制方差子图
fig_variance = plt.figure(figsize=(7, 5))
for idx, txs in enumerate(all_txs_values):
    txs_data_default = [default_sharding[k][txs]['variance'] for k in sorted(default_sharding.keys())]
    txs_data_clpa = [clpa_sharding[k][txs]['variance'] for k in sorted(clpa_sharding.keys())]
    txs_data_cpla_plus = [cpla_plus_sharding[k][txs]['variance'] for k in sorted(cpla_plus_sharding.keys())]

    plt.plot(sorted(default_sharding.keys()), txs_data_default, label='CLPA', marker='o')
    plt.plot(sorted(clpa_sharding.keys()), txs_data_clpa, label='Proposed', marker='>')
    # plt.plot(sorted(cpla_plus_sharding.keys()), txs_data_cpla_plus, label='current')

    plt.title(f'All Txs = {txs} - Variance', fontsize=18)
    plt.ylabel('load factor', fontsize=18)
    plt.xlabel('Number of Shards', fontsize=18)
    plt.legend()
    # plt.grid(True)
    plt.xticks([2, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52])

# 绘制跨片交易减少比率子图
fig_ratio = plt.figure(figsize=(7, 5))
for idx, txs in enumerate(all_txs_values):
    txs_ratio_default = [float(default_sharding[k][txs]['Cross-Shard txs Reduction Ratio']) for k in
                         sorted(default_sharding.keys())]
    txs_ratio_clpa = [float(clpa_sharding[k][txs]['Cross-Shard txs Reduction Ratio']) for k in
                      sorted(clpa_sharding.keys())]
    txs_ratio_cpla_plus = [float(cpla_plus_sharding[k][txs]['Cross-Shard txs Reduction Ratio']) for k in
                           sorted(cpla_plus_sharding.keys())]

    plt.plot(sorted(default_sharding.keys()), txs_ratio_default, label='CLPA', marker='o')
    plt.plot(sorted(clpa_sharding.keys()), txs_ratio_clpa, label='Proposed', marker='>')
    # plt.plot(sorted(cpla_plus_sharding.keys()), txs_ratio_cpla_plus, label='current')

    plt.title(f'All Txs = {txs} - Cross-Shard txs Reduction Ratio', fontsize=18)
    plt.ylabel('ctxs reduction ratio', fontsize=18)
    plt.xlabel('Number of Shards', fontsize=18)
    plt.legend()
    # plt.grid(True)
    plt.xticks([2, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52])

# 调整布局防止重叠
plt.tight_layout()

# 保存为 PDF 和 SVG 格式
fig_variance.savefig('variance_plot.pdf', format='pdf')
# fig_variance.savefig('variance_plot.svg', format='svg')
fig_ratio.savefig('ctx_reduce_ratio_plot.pdf', format='pdf')
# fig_ratio.savefig('ratio_plot.svg', format='svg')

# 显示图形（可选）
plt.show()
