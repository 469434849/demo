import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from mysqlTest import Connect_and_read

plt.rcParams['font.family'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False
# 示例数据
query = "SELECT * FROM emulator_copy1"
data = Connect_and_read(query)
# print("数据列表:")
# for row in data:
#     print(row)

target_modes = {'Monoxide', 'Metis', 'Proposed'}
modes = {item['run_mod'] for item in data if item['run_mod'] in target_modes}
data_by_mode = {mode: [] for mode in modes}

for item in data:
    if item['run_mod'] in target_modes:
        data_by_mode[item['run_mod']].append(item)

# 绘图
fig_tps = plt.figure(figsize=(7, 5))
for mode, mode_data in data_by_mode.items():
    x = [item['shard_num'] for item in mode_data]
    y = [item['average_tps'] for item in mode_data]
    plt.plot(x, y, marker='o', label=mode)

plt.xticks(range(2, 34, 2))

ax = plt.gca()
# ax.yaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))
# ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
# ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:.0e}'))


# 添加标签、标题和图例
plt.xlabel('Number of Shards', fontsize=18)
plt.ylabel('Throughput(TPS)', fontsize=18)
# plt.title('Average TPS vs Shard Number for Different Run Modes')
plt.legend(title='')

# 显示图表
plt.show()
# fig_tps.savefig('tps_plot.pdf', format='pdf')