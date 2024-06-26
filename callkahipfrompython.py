import kahip

#build adjacency array representation of the graph
xadj           = [0,2,5,7,9,12];   # 节点 i 的邻居列表在 [xadj[i] 到 xadj[i+1]-1) 之间。它保存着指向顶点邻接表的指针。数组的大小应该是n + 1。
adjncy         = [1,4,0,2,4,1,3,2,4,0,1,3]; # 邻居节点的列表
vwgt           = [1,1,1,1,1] #每个顶点的权重
adjcwgt        = [1,1,1,1,1,1,1,1,1,1,1,1] #每条边的权重  邻接权值数组，它保存了存在的边的权值。数组的大小应该是2m。如果你的图没有边权值，你可以使用空指针作为参数。
supress_output = 0  #如果启用此选项，则不会将分区库的输出打印到标准输出。
imbalance      = 0.03 # 该参数控制允许的不平衡量。例如，将其设置为0.03指定不平衡为3%，这意味着在未加权图上， |Vi| ≤ (1 + 0.03)|V|/k.
# 设置 imbalance 为0.03意味着允许每个分区的节点数量最多可以是总节点数除以分区数的103%。
# 例如，如果总共有1000个节点并且想要将图分为3个分区，每个理想分区应该有约333个节点。允许0.03的不平衡意味着分区大小可以是327到339个节点（1000 * (1 ± 0.03) / 3）。
nblocks        = 2 #此参数指定要对图进行分区的块的数量
seed           = 0 #用于随机数生成器的种子
#如果质量至关重要，则应该使用Strong;如果需要在分区质量和运行时间之间进行权衡，则应该使用eco;如果关注的是分区速度，则应该使用fast
# 名称中带有social的配置应该用于社交网络和web图形(它们使用不同的粗化方案)。
# set mode 
#const int FAST           = 0;
#const int ECO            = 1;
#const int STRONG         = 2;
#const int FASTSOCIAL     = 3;
#const int ECOSOCIAL      = 4;
#const int STRONGSOCIAL   = 5;
mode = 2 
# edgecut 是一个输出参数。它表示计算分区的切边。
# blocks 它必须是一个已经分配的大小为n的数组。在函数调用之后，这个数组包含了顶点块的信息，即第i个顶点的块在blocks[i]中给出。
edgecut, blocks = kahip.kaffpa(vwgt, xadj, adjcwgt,
                              adjncy,  nblocks, imbalance, 
                              supress_output, seed, mode)

print(edgecut)
print(blocks)


