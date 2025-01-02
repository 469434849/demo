import matplotlib.pyplot as plt

# 设置字体和样式
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 数据设置：交易确认延迟 (单位: 毫秒)，精确到两位小数
shard_numbers = [10, 20, 40, 60, 80, 100]
delay_dual_chain = [40.12, 50.45, 56.32, 75.78, 84.23, 95.56]  # 双链架构
delay_non_coop = [65.34, 70.89, 85.12, 105.45, 130.67, 155.89]  # 非合作分片方法
delay_monoxide = [52.45, 63.34, 78.56, 95.78, 110.23, 135.67]   # Monoxide 方法

cross_shard_ratios = [10, 30, 50, 70, 90]
delay_dual_chain_ratios = [60.23, 63.56, 70.34, 85.78, 101.12]  # 双链架构
delay_non_coop_ratios = [70.45, 75.67, 98.45, 135.78, 160.89]  # 非合作分片方法
delay_monoxide_ratios = [65.12, 71.34, 87.23, 120.45, 140.67]   # Monoxide 方法

# 创建一个图表，分两部分显示
fig, axs = plt.subplots(1, 2, figsize=(15,6))

# 图表 1：交易确认延迟 vs 分片数量
axs[0].plot(shard_numbers, delay_dual_chain, marker='o', label='双链架构')
axs[0].plot(shard_numbers, delay_non_coop, marker='s', label='非合作分片方法')
axs[0].plot(shard_numbers, delay_monoxide, marker='^', label='Monoxide 方法')
axs[0].set_xlabel("分片数量", fontsize=16)
axs[0].set_ylabel("交易确认延迟（ms）", fontsize=16)
axs[0].set_title("跨分片交易比例为50%", fontsize=16)
axs[0].set_xticks(shard_numbers)
axs[0].legend(fontsize=14)
axs[0].text(0.5, -0.20, f"（a）交易确认延迟随分片数量变化", transform=axs[0].transAxes, ha='center',
        fontsize=20)

# 图表 2：交易确认延迟 vs 跨分片交易比例
axs[1].plot(cross_shard_ratios, delay_dual_chain_ratios, marker='o', label='双链架构')
axs[1].plot(cross_shard_ratios, delay_non_coop_ratios, marker='s', label='非合作分片方法')
axs[1].plot(cross_shard_ratios, delay_monoxide_ratios, marker='^', label='Monoxide 方法')
axs[1].set_xlabel("跨分片交易比例 (%)", fontsize=16)
axs[1].set_ylabel("交易确认延迟（ms）", fontsize=16)
axs[1].set_title("分片数量为50", fontsize=16)
axs[1].set_xticks(cross_shard_ratios)
axs[1].legend(fontsize=14)
axs[1].text(0.5, -0.20, f"（b）交易确认延迟随跨分片交易比例变化", transform=axs[1].transAxes, ha='center',
        fontsize=20)
plt.subplots_adjust(wspace=1.1)
# 调整布局
plt.tight_layout()
plt.show()
