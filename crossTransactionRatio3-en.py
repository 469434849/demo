import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from mysqlTest import Connect_and_read

# plt.rcParams['font.family'] = ['Times New Roman']
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 示例数据
query = "SELECT * FROM emulator_copy1 where shard_num in (8, 16, 32, 48,64)"
data = Connect_and_read(query)

target_modes = {'Monoxide', 'Metis', 'Proposed'}
target_speeds = [2000, 4000, 6000]
# target_speeds = [2000]
target_shardNumbers = [8, 16, 32, 48,64]

data_by_speed_and_mode = {speed: {mode: [] for mode in target_modes} for speed in target_speeds}

for item in data:
    if item['run_mod'] in target_modes and item['inject_speed'] in target_speeds:
        data_by_speed_and_mode[item['inject_speed']][item['run_mod']].append(item)

prefixes = ['a', 'b', 'c']
# 画子图
fig, axes = plt.subplots(nrows=1, ncols=len(target_speeds), figsize=(20, 6))

for i, speed in enumerate(target_speeds):
    ax = axes[i] if len(target_speeds) > 1 else axes
    # 绘制柱状图
    width = 0.2  # 柱子的宽度
    x = target_shardNumbers
    x_pos = range(len(x))  # x轴上的位置
    # 按照target_modes的顺序绘制柱子
    for j, mode in enumerate(target_modes):
        mode_data = data_by_speed_and_mode[speed][mode]
       # y = [item['cross_transaction_ratio'] for item in mode_data]
       # plt.bar([p + width * i for p in x_pos], y, width, label=mode)
    #for mode, mode_data in data_by_speed_and_mode[speed].items():
        x = [item['shard_num'] for item in mode_data]
        y = [item['cross_transaction_ratio'] for item in mode_data]
        if mode == 'Monoxide':
            ax.bar([p + width * j for p in x_pos], y, width, label=mode,color='gray')
            # ax.plot(x, y, marker='o', label=mode, color='blue')  # 指定 Monoxide 类型线条为蓝色
        elif mode == 'Metis':
            ax.bar([p + width * j for p in x_pos], y, width, label=mode,color='#99CC99')
            # ax.plot(x, y, marker='o', label=mode, color='green')  # 指定 Metis 类型线条为绿色
        elif mode == 'Proposed':
            ax.bar([p + width * j for p in x_pos], y, width, label="DCLPA",color='red')
            # ax.plot(x, y, marker='o', label=mode, color='red')  # 指定 Proposed 类型线条为红色
        # ax.plot(x, y, marker='o', label=mode)
    ax.set_xticks([p - width / 2 + width * len(target_modes) / 2 for p in x_pos], x)
    ax.set_xlabel('分片数', fontsize=16)
    ax.set_ylabel('跨分片交易比例', fontsize=16)
    ax.legend(title='',fontsize=14)
    # ax.set_title(f"Speed {speed}", fontsize=18)
    # 设置子图标题在 x 轴下方
    ax.text(0.5, -0.20, f" ({prefixes[i]}) 交易注入速率 = {speed}(笔/秒)", transform=ax.transAxes, ha='center', fontsize=20)

plt.tight_layout()
plt.show()
# fig.savefig('ctx_ratio_plot.pdf', format='pdf')