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
# target_speeds = [2000, 4000, 6000]
target_speeds = [2000]

data_by_speed_and_mode = {speed: {mode: [] for mode in target_modes} for speed in target_speeds}

for item in data:
    if item['run_mod'] in target_modes and item['inject_speed'] in target_speeds:
        data_by_speed_and_mode[item['inject_speed']][item['run_mod']].append(item)

# 绘图
fig_tps = plt.figure(figsize=(8,8))
for speed in target_speeds:
    for mode, mode_data in data_by_speed_and_mode[speed].items():
        x = [item['shard_num'] for item in mode_data]
        y = [item['average_tps'] for item in mode_data]
        plt.plot(x, y, marker='o', label=f"{mode}")
    # 添加标题放在横坐标下方，使用 speed 变量
    plt.title(f"(a) Injection Speeds: {speed}", y=-0.15, fontsize=20)

plt.xticks(range(8, 65, 8))

ax = plt.gca()


# 添加标签、标题和图例
plt.xlabel('Number of Shards', fontsize=18)
plt.ylabel('Throughput(TPS)', fontsize=18)
plt.legend(title='')


# 显示图表
plt.show()
# fig_tps.savefig('tps_plot.pdf', format='pdf')