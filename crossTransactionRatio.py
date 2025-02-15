import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from mysqlTest import Connect_and_read

plt.rcParams['font.family'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False

# 示例数据
query = "SELECT * FROM emulator_copy1"
data = Connect_and_read(query)

target_modes = ['Monoxide', 'Metis', 'Proposed']
target_shardNumbers = [2, 8, 16, 24, 32]

# 数据预处理
data_by_mode = {mode: [] for mode in target_modes}
for item in data:
    if item['run_mod'] in target_modes and item['shard_num'] in target_shardNumbers:
        data_by_mode[item['run_mod']].append(item)

# 绘制柱状图
width = 0.2  # 柱子的宽度
x = target_shardNumbers
x_pos = range(len(x))  # x轴上的位置

fig_ctx_ratio = plt.figure(figsize=(7, 5))

# 按照target_modes的顺序绘制柱子
for i, mode in enumerate(target_modes):
    mode_data = data_by_mode[mode]
    y = [item['cross_transaction_ratio'] for item in mode_data]
    plt.bar([p + width * i for p in x_pos], y, width, label=mode)

# 设置x轴的刻度和刻度标签

plt.xticks([p - width / 2 + width * len(target_modes) / 2 for p in x_pos], x)

ax = plt.gca()

# 添加标签、标题和图例
plt.xlabel('Number of Shards', fontsize=18)
plt.ylabel('Cross Transaction Ratio', fontsize=18)
plt.legend(title='')

# 显示图表
plt.show()
fig.savefig('ctx_ratio_plot.pdf', format='pdf')