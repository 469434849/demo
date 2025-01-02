import matplotlib.pyplot as plt
# plt.rcParams['font.family'] = ['Times New Roman']
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 数据设置
# 数据设置调整为4000-10000范围，精确到个位
# 跨分片交易比例 50
shard_numbers = [10, 20, 40, 60, 80, 100]
tps_dual_chain = [4503, 6198, 7821, 8793, 9532, 10998]  # 双链架构
tps_non_coop = [4098, 5687, 6521, 6993, 7169, 7396]     # 非合作分片
tps_monoxide = [4201, 5998, 6912, 7193, 7892, 8198]    # Monoxide 方法

# 分片50
cross_shard_ratios = [10, 30, 50, 70, 90]
tps_dual_chain_ratios = [10503, 9998, 8321, 8032, 7821]  # 超过70%下降加速
tps_non_coop_ratios = [9892, 9193, 6812, 5031, 4909]    # 下降显著
tps_monoxide_ratios = [9918, 9492, 7013, 5510, 4803]    # Monoxide 表现中等
# 图表 1：TPS vs 分片数量，设置 xticks
plt.figure(figsize=(6, 4))
plt.plot(shard_numbers, tps_dual_chain, marker='o', label='双链架构')
plt.plot(shard_numbers, tps_non_coop, marker='s', label='非合作分片方法')
plt.plot(shard_numbers, tps_monoxide, marker='^', label='Monoxide 方法')
plt.xlabel("分片数量", fontsize=12)
plt.ylabel("吞吐量（TPS）", fontsize=12)
plt.title("吞吐量随分片数量变化", fontsize=14)
plt.xticks(shard_numbers)  # 设置横坐标刻度
plt.legend(fontsize=10)
plt.show()

# 图表 2：TPS vs 跨分片交易比例，设置 xticks
plt.figure(figsize=(6, 4))
plt.plot(cross_shard_ratios, tps_dual_chain_ratios, marker='o', label='双链架构')
plt.plot(cross_shard_ratios, tps_non_coop_ratios, marker='s', label='非合作分片方法')
plt.plot(cross_shard_ratios, tps_monoxide_ratios, marker='^', label='Monoxide 方法')
plt.xlabel("跨分片交易比例 (%)", fontsize=12)
plt.ylabel("吞吐量（TPS）", fontsize=12)
plt.title("吞吐量随跨分片交易比例变化", fontsize=14)
plt.xticks(cross_shard_ratios)  # 设置横坐标刻度
plt.legend(fontsize=10)
plt.show()