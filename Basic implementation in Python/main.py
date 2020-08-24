from Block import Block

blockchain = []

genesis_block = Block("init", ["Jim sent 15 dollars to pam"])

print(genesis_block.block_hash)

second_block = Block(genesis_block.block_hash, ["Jim sent 23 dollars to patrick"])

print(second_block.block_hash)

third_block = Block(second_block.block_hash, ["Pam sent 10 dollars to Dwight"])

print(third_block.block_hash)