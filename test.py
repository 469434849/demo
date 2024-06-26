import networkx as nx
import community as community_louvain
import numpy as np
import matplotlib.pyplot as plt
# 新增导入pandas库
import pandas as pd


def read_and_count_transactions_from_csv(file_path, num_records=100):
    """
    从CSV文件读取交易数据并统计每对账户间的交易次数。

    :param file_path: CSV文件路径
    :param num_records: 读取的记录数，默认为1000
    :return: 交易对及其交易次数的列表
    """
    # 读取CSV文件的前num_records行
    df = pd.read_csv(file_path, nrows=num_records)

    # 统计每对账户间交易次数
    transaction_counts = df.groupby(['from', 'to']).size().reset_index(name='count')

    # 转换为交易对和交易次数的列表
    transactions = transaction_counts.apply(lambda row: (row['from'], row['to'], row['count']), axis=1).tolist()

    return transactions


def merge_communities(G, partition, target_num_communities):
    # Convert partition to a format suitable for merging
    communities = {}
    for node, community in partition.items():
        if community not in communities:
            communities[community] = []
        communities[community].append(node)

    # Merge communities until reaching the target number of communities
    while len(communities) > target_num_communities:
        # Find the two smallest communities to merge
        smallest_communities = sorted(communities.items(), key=lambda x: len(x[1]))[:2]
        comm1, nodes1 = smallest_communities[0]
        comm2, nodes2 = smallest_communities[1]

        # Merge the two communities
        new_comm = max(communities.keys()) + 1
        communities[new_comm] = nodes1 + nodes2
        del communities[comm1]
        del communities[comm2]

        # Update partition to reflect the merge
        for node in nodes1 + nodes2:
            partition[node] = new_comm

    return partition
# 创建交易图（示例数据）
G = nx.Graph()
csv_file_path = './2000000to2999999_BlockTransaction.csv'  # 替换为你的CSV文件路径
transactions = read_and_count_transactions_from_csv(csv_file_path)
# 添加账户（节点）和交易（边），并设置交易次数为边权重
# transactions = [
#     ('A', 'B', 3),
#     ('A', 'C', 2),
#     ('B', 'C', 1),
#     ('B', 'D', 4),
#     ('C', 'E', 5),
#     ('D', 'E', 2),
#     ('E', 'F', 1),
#     ('D', 'F', 3)
# ]
G.add_weighted_edges_from(transactions)

# 应用 Louvain 方法进行社区检测
partition = community_louvain.best_partition(G, weight='weight', resolution=1)

# 合并社区以达到预期的社区数
target_num_communities = 8  # 目标社区数
partition = merge_communities(G, partition, target_num_communities)
# 输出社区划分结果
# for node, community in partition.items():
#     print(f"Node {node} is in community {community}")


# 计算和输出每个社区的负载因子
def calculate_load_factor(G, partition, community_id):
    community_nodes = [node for node, com in partition.items() if com == community_id]
    intra_community_edges = [(u, v, d) for u, v, d in G.edges(data=True) if
                             u in community_nodes and v in community_nodes]
    inter_community_edges = [(u, v, d) for u, v, d in G.edges(data=True) if
                             (u in community_nodes and v not in community_nodes) or (
                                     v in community_nodes and u not in community_nodes)]

    total_weight = sum(d['weight'] for u, v, d in intra_community_edges) + sum(
        d['weight'] for u, v, d in inter_community_edges)
    # print(f"Community {community_id} ，total_weight {total_weight}")
    return total_weight / len(community_nodes)


communities = set(partition.values())
load_factors = {community: calculate_load_factor(G, partition, community) for community in communities}

# for community, load_factor in load_factors.items():
#     print(f"Community {community} has a load factor of {load_factor}")

# 计算整体负载因子的方差
load_factors_list = list(load_factors.values())
variance = np.var(load_factors_list)
print(f"Variance of Load Factors: {variance}")

pos = nx.spring_layout(G)

# 根据社区划分结果为节点着色

colors = [partition[node] for node in G.nodes()]

# 绘制图和社区结构
plt.figure(figsize=(12, 8))
# nx.draw(G, pos, node_color=colors, with_labels=True, cmap=plt.cm.jet)
nx.draw(G, pos, node_color=colors, node_size=50, cmap=plt.cm.jet, with_labels=False)
edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
plt.title("Louvain Method Community Detection")
plt.show()
