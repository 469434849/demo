import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from mysqlTest import Connect_and_read

plt.rcParams['font.family'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False

# 示例数据
query = "SELECT * FROM emulator_copy1"
data = Connect_and_read(query)

target_modes = {'Monoxide', 'Metis', 'Proposed'}
# target_speeds = [2000, 4000, 6000]
target_speeds = [2000, 4000, 6000, 2000, 4000, 6000, 2000, 4000, 6000]

data_by_speed_and_mode = {speed: {mode: [] for mode in target_modes} for speed in target_speeds}

for item in data:
    if item['run_mod'] in target_modes and item['inject_speed'] in target_speeds:
        data_by_speed_and_mode[item['inject_speed']][item['run_mod']].append(item)

prefixes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# 画子图
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(17, 12))
fig.subplots_adjust(hspace=0.0)  # 调整行之间的距离
for i, speed in enumerate(target_speeds):
    rowIdx = int(i / 3)
    ax = axes[rowIdx][i % 3] if len(target_speeds) > 1 else axes
    if rowIdx == 0:
        for mode, mode_data in data_by_speed_and_mode[speed].items():
            x = [item['shard_num'] for item in mode_data]
            y = [item['average_tps'] for item in mode_data]
            if mode == 'Monoxide':
                ax.plot(x, y, marker='o', label=mode, color='blue')  # 指定 Monoxide 类型线条为蓝色
            elif mode == 'Metis':
                ax.plot(x, y, marker='o', label=mode, color='green')  # 指定 Metis 类型线条为绿色
            elif mode == 'Proposed':
                ax.plot(x, y, marker='o', label=mode, color='red')  # 指定 Proposed 类型线条为红色
            # ax.plot(x, y, marker='o', label=mode)
        ax.set_xticks(range(8, 65, 8))
        ax.set_xlabel('Number of Shards', fontsize=16)
        ax.set_ylabel('Throughput(TPS)', fontsize=16)
        ax.set_box_aspect(4 / 7)
        ax.legend(title='')
        # ax.set_title(f"Speed {speed}", fontsize=18)
        # 设置子图标题在 x 轴下方
        # ax.text(0.5, -0.15, f" ({prefixes[i % 3]}) TX arrival rate = {speed}(TXs/sec)", transform=ax.transAxes, ha='center',
        #         fontsize=18)

        ax.text(0.5, -0.28, f" ({prefixes[i]}) TPS, TXs arrival rate = {speed}(TXs/sec)", transform=ax.transAxes, ha='center',
                fontsize=18)

    if rowIdx == 1:
        target_shardNumbers = [8, 16, 32, 48,64]
        # 绘制柱状图
        width = 0.20  # 柱子的宽度
        x = target_shardNumbers
        x_pos = range(len(x))  # x轴上的位置
        for j, mode in enumerate(target_modes):
            mode_data = data_by_speed_and_mode[speed][mode]
            filtered_mode_data = [item for item in mode_data if item['shard_num'] in target_shardNumbers]

            x = [item['shard_num'] for item in filtered_mode_data]
            y = [item['cross_transaction_ratio'] for item in filtered_mode_data]
            if mode == 'Monoxide':
                ax.bar([p + width * j for p in x_pos], y, width, label=mode, color='gray')
                # ax.plot(x, y, marker='o', label=mode, color='blue')  # 指定 Monoxide 类型线条为蓝色
            elif mode == 'Metis':
                ax.bar([p + width * j for p in x_pos], y, width, label=mode, color='#99CC99')
                # ax.plot(x, y, marker='o', label=mode, color='green')  # 指定 Metis 类型线条为绿色
            elif mode == 'Proposed':
                ax.bar([p + width * j for p in x_pos], y, width, label=mode, color='red')
                # ax.plot(x, y, marker='o', label=mode, color='red')  # 指定 Proposed 类型线条为红色
            # ax.plot(x, y, marker='o', label=mode)
        ax.set_xticks([p - width / 2 + width * len(target_modes) / 2 for p in x_pos], x)
        ax.set_xlabel('Number of Shards', fontsize=16)
        ax.set_ylabel('Cross-Shard TXs Ratio', fontsize=16)
        ax.set_ylim(0, max(y) * 1.2)
        ax.set_box_aspect(4 / 7)
        ax.legend(title='')
        # ax.set_title(f"Speed {speed}", fontsize=18)
        # 设置子图标题在 x 轴下方
        ax.text(0.5, -0.28, f" ({prefixes[i]}) CTX ratio, TXs arrival rate = {speed}(TXs/sec)", transform=ax.transAxes,
                ha='center', fontsize=18)
    if rowIdx == 2:
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
        ax.set_ylabel('TXs Confirm Latency(sec)', fontsize=16)
        ax.set_box_aspect(4 / 7)
        ax.legend(title='')
        # ax.set_title(f"Speed {speed}", fontsize=18)
        # 设置子图标题在 x 轴下方
        # ax.text(0.5, -0.15, f" ({prefixes[i % 3]}) TX arrival rate = {speed}(TXs/sec)", transform=ax.transAxes, ha='center',
        #         fontsize=18)

        ax.text(0.5, -0.28, f" ({prefixes[i]}) TCL, TXs arrival rate = {speed}(TXs/sec)", transform=ax.transAxes,
                ha='center',
                fontsize=18)
plt.tight_layout()
plt.show()
fig.savefig('plot333.pdf', format='pdf')
