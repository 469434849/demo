import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from mysqlTest import Connect_and_read

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
plt.figure(figsize=(7,5))
for mode, mode_data in data_by_mode.items():
    x = [item['shard_num'] for item in mode_data]
    y = [item['transaction_confirm_latency'] for item in mode_data]
    plt.plot(x, y, marker='o', label=mode)

plt.xticks(range(2, 34, 2))

ax = plt.gca()
# ax.yaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))
# ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
# ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:.0e}'))


# 添加标签、标题和图例
plt.xlabel('Number of Shards', fontsize=20)
plt.ylabel('Average Latency(sec)', fontsize=20)
# plt.title('Average TPS vs Shard Number for Different Run Modes')
plt.legend(title='')

# 显示图表
plt.show()
