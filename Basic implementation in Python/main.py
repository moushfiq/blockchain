from Block import Block

blockchain = []


def transaction(name, amount, previous):

    temp = name + " paid " + amount
    if previous:
        temp_block = Block(previous, temp)
        blockchain.append(temp_block.block_hash)
        return blockchain
    else:
        genesis_block = Block("init", temp)
        blockchain.append(genesis_block.block_hash)
        return blockchain


print(transaction("M", "62", blockchain[-1] if blockchain else 0))
print(transaction("s", "94", blockchain[-1] if blockchain else 0))
print(transaction("f", "86", blockchain[-1] if blockchain else 0))

print("")
print("")

#print(transaction("Numan", "95", ""))
#print(transaction("Ashraf", "22", "3291896b2b9e7a43fe2da68b5bab9e7fcacc1c61d5a43024362578a3fd3d9cef"))
#print(transaction("Nafir", "61", "5a18a02fac2b05791c8c214a337394a2a1ace1d24786c58c756bf209e66371d8"))

# genesis_block = Block("init", "temp")
#
# print(genesis_block.block_hash)
#
# second_block = Block(genesis_block.block_hash, ["Jim sent 28 dollars to Angela"])
#
# print(second_block.block_hash)
#
# third_block = Block(second_block.block_hash, ["Pam sent 12 dollars to Dwight"])
#
# print(third_block.block_hash)
#
# fourth_block = Block(third_block.block_hash, ["Michael sent 38 dollars to kelly"])
#
# print(fourth_block.block_hash)
