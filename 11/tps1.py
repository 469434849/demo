import matplotlib.pyplot as plt

# 设置字体和样式
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 数据设置
shard_numbers = [10, 20, 40, 60, 80, 100]
tps_dual_chain = [4503, 6198, 7821, 8793, 9532, 10998]  # 双链架构
tps_non_coop = [4098, 5687, 6521, 6993, 7169, 7396]     # 非合作分片
tps_monoxide = [4201, 5998, 6912, 7193, 7892, 8198]    # Monoxide 方法

cross_shard_ratios = [10, 30, 50, 70, 90]
tps_dual_chain_ratios = [10503, 9998, 8321, 8032, 7821]  # 超过70%下降加速
tps_non_coop_ratios = [9892, 9193, 6812, 5031, 4909]    # 下降显著
tps_monoxide_ratios = [9918, 9492, 7013, 5510, 4803]    # Monoxide 表现中等

# 创建一个图表，分两部分显示
fig, axs = plt.subplots(1, 2, figsize=(15, 6))

# 图表 1：TPS vs 分片数量
axs[0].plot(shard_numbers, tps_dual_chain, marker='o', label='双链架构')
axs[0].plot(shard_numbers, tps_non_coop, marker='s', label='非合作分片方法')
axs[0].plot(shard_numbers, tps_monoxide, marker='^', label='Monoxide 方法')
axs[0].set_xlabel("分片数量", fontsize=16)
axs[0].set_ylabel("吞吐量（TPS）", fontsize=16)
axs[0].set_title("跨分片交易比例为50%", fontsize=16)
axs[0].set_xticks(shard_numbers)
axs[0].legend(fontsize=14)
axs[0].text(0.5, -0.20, f"（a）吞吐量随分片数量变化情况", transform=axs[0].transAxes, ha='center',
        fontsize=20)

# 图表 2：TPS vs 跨分片交易比例
axs[1].plot(cross_shard_ratios, tps_dual_chain_ratios, marker='o', label='双链架构')
axs[1].plot(cross_shard_ratios, tps_non_coop_ratios, marker='s', label='非合作分片方法')
axs[1].plot(cross_shard_ratios, tps_monoxide_ratios, marker='^', label='Monoxide 方法')
axs[1].set_xlabel("跨分片交易比例 (%)", fontsize=16)
axs[1].set_ylabel("吞吐量（TPS）", fontsize=16)
axs[1].set_title("分片数量为50", fontsize=16)
axs[1].set_xticks(cross_shard_ratios)
axs[1].legend(fontsize=14)
axs[1].text(0.5, -0.20, f"（b）吞吐量随跨分片交易比例变化情况", transform=axs[1].transAxes, ha='center',
        fontsize=20)
plt.subplots_adjust(wspace=1.1)
# 调整布局
plt.tight_layout()
plt.show()
