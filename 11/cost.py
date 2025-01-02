import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 数据设置
cross_shard_ratios = [10, 30, 50, 70, 90]
comm_dual_chain_ratios = [0.8, 1.2, 1.8, 2.5, 3.4]  # 双链架构
comm_non_coop_ratios = [1.2, 2.3, 3.8, 5.6, 8.2]    # 非合作分片方法
comm_monoxide_ratios = [1.0, 1.8, 2.9, 4.1, 6.0]    # Monoxide 方法

shard_numbers = [10, 20, 40, 60, 80, 100]
comm_dual_chain_shards = [0.9, 1.2, 1.7, 2.2, 2.8, 3.4]  # 双链架构
comm_non_coop_shards = [1.5, 2.4, 4.1, 5.8, 7.3, 8.2]    # 非合作分片方法
comm_monoxide_shards = [1.2, 1.9, 3.2, 4.5, 5.8, 6.7]    # Monoxide 方法

# 创建柱状图，分两部分显示
fig, axs = plt.subplots(1, 2, figsize=(15,6))

# 设置柱状图的宽度
bar_width = 0.25

# 图表 2：通信开销 vs 分片数量
x_shard_numbers = np.arange(len(shard_numbers))
axs[0].bar(x_shard_numbers - bar_width, comm_dual_chain_shards, width=bar_width, label='双链架构')
axs[0].bar(x_shard_numbers, comm_non_coop_shards, width=bar_width, label='非合作分片方法')
axs[0].bar(x_shard_numbers + bar_width, comm_monoxide_shards, width=bar_width, label='Monoxide 方法')
axs[0].set_xlabel("分片数量", fontsize=16)
axs[0].set_ylabel("通信开销（KB）", fontsize=16)
axs[0].set_title("跨分片交易比例为50%", fontsize=16)
axs[0].set_xticks(x_shard_numbers)
axs[0].set_xticklabels(shard_numbers)
axs[0].legend(fontsize=14)
axs[0].text(0.5, -0.20, f"（a）通信开销随跨分片数量变化情况", transform=axs[0].transAxes, ha='center',
        fontsize=20)

# 图表 1：通信开销 vs 跨分片交易比例
x_cross_shard = np.arange(len(cross_shard_ratios))
axs[1].bar(x_cross_shard - bar_width, comm_dual_chain_ratios, width=bar_width, label='双链架构')
axs[1].bar(x_cross_shard, comm_non_coop_ratios, width=bar_width, label='非合作分片方法')
axs[1].bar(x_cross_shard + bar_width, comm_monoxide_ratios, width=bar_width, label='Monoxide 方法')
axs[1].set_xlabel("跨分片交易比例 (%)", fontsize=16)
axs[1].set_ylabel("通信开销（KB）", fontsize=16)
axs[1].set_title("分片数量为50", fontsize=16)
axs[1].set_xticks(x_cross_shard)
axs[1].set_xticklabels(cross_shard_ratios)
axs[1].legend(fontsize=14)
axs[1].text(0.5, -0.20, f"（b）通信开销随跨分片交易比例变化情况", transform=axs[1].transAxes, ha='center',
        fontsize=20)
plt.subplots_adjust(wspace=1.1)

# 调整布局
plt.tight_layout()
plt.show()
