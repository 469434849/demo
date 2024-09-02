import random

# 定义交易结构
class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

# 定义分片结构
class Shard:
    def __init__(self, shard_id):
        self.shard_id = shard_id
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

# 初始化分片
def initialize_shards(num_shards):
    return [Shard(i) for i in range(num_shards)]

# 随机生成交易
def generate_transactions(num_transactions, num_accounts):
    transactions = []
    for _ in range(num_transactions):
        sender = random.randint(1, num_accounts)
        receiver = random.randint(1, num_accounts)
        amount = random.randint(1, 100)
        transactions.append(Transaction(sender, receiver, amount))
    return transactions

# 将交易分配到分片
def assign_transactions_to_shards(transactions, shards, num_shards):
    for tx in transactions:
        shard_id = tx.sender % num_shards
        shards[shard_id].add_transaction(tx)

# 处理跨分片交易
def handle_cross_shard_transactions(shards):
    cross_shard_txs = []
    for shard in shards:
        for tx in shard.transactions:
            if tx.sender % len(shards) != tx.receiver % len(shards):
                cross_shard_txs.append(tx)
    return cross_shard_txs

# 主函数
def main():
    num_shards = 4
    num_transactions = 100000
    num_accounts = 5000

    shards = initialize_shards(num_shards)
    transactions = generate_transactions(num_transactions, num_accounts)
    assign_transactions_to_shards(transactions, shards, num_shards)

    print("各分片中的交易:")
    for shard in shards:
        print(f"分片 {shard.shard_id}: {len(shard.transactions)} 个交易")

    cross_shard_txs = handle_cross_shard_transactions(shards)
    print(f"跨分片交易: {len(cross_shard_txs)} 个")

if __name__ == "__main__":
    main()
