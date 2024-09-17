import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from mysqlTest import Connect_and_read

plt.rcParams['font.family'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False

# 示例数据
query = "SELECT * FROM emulator_copy1"
data = Connect_and_read(query)

target_modes = {'Monoxide', 'Metis', 'Proposed'}
target_speeds = [2000, 4000, 6000]

data_by_speed_and_mode = {speed: {mode: [] for mode in target_modes} for speed in target_speeds}

for item in data:
    if item['run_mod'] in target_modes and item['inject_speed'] in target_speeds:
        data_by_speed_and_mode[item['inject_speed']][item['run_mod']].append(item)

prefixes = ['a', 'b', 'c']
# 画子图
fig, axes = plt.subplots(nrows=1, ncols=len(target_speeds), figsize=(20, 6))

for i, speed in enumerate(target_speeds):
    ax = axes[i] if len(target_speeds) > 1 else axes
    for mode, mode_data in data_by_speed_and_mode[speed].items():
        x = [item['shard_num'] for item in mode_data]
        y = [item['transaction_confirm_latency'] for item in mode_data]
        if mode == 'Monoxide':
            ax.plot(x, y, marker='o', label=mode, color='blue')  # 指定 Monoxide 类型线条为蓝色
        elif mode == 'Metis':
            ax.plot(x, y, marker='o', label=mode, color='green')  # 指定 Metis 类型线条为绿色
        elif mode == 'Proposed':
            ax.plot(x, y, marker='o', label=mode, color='red')  # 指定 Proposed 类型线条为红色
        # ax.plot(x, y, marker='o', label=mode)
    ax.set_xticks(range(8, 65, 8))
    ax.set_xlabel('Number of Shards', fontsize=16)
    ax.set_ylabel('Average Latency(sec)', fontsize=16)
    ax.legend(title='')
    # ax.set_title(f"Speed {speed}", fontsize=18)
    # 设置子图标题在 x 轴下方
    ax.text(0.5, -0.15, f" ({prefixes[i]}) TXs arrival rates:{speed}(TXs/s)", transform=ax.transAxes, ha='center', fontsize=18)

plt.tight_layout()
plt.show()
fig.savefig('tcl_plot.pdf', format='pdf')