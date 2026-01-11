import hashlib

# Creates class mapping the structure of a block on the block chain, 
# concatenating the previous hash with the blocks' transactions, 
# then hashing them all and passing it to the next block.

class simpleblock:
    def __init__ (self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        self.block_data = " - ".join(transaction_list) + " - " + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

# Class with functions to handle appending new blocks to the blockchain and the displaying blockchain
class simplechain:
    def __init__ (self):
        self.chain = []
        self.i = 0
    
    def append_block(self, data, hash):
        self.chain.append(f"""Block {self.i}: {data} 
Block {self.i} hash: {hash}
""")
    def display_chain(self):
        for x in self.chain:
            print(x)

# list of transactions to store and hash on the blockchain

t1 = "George sends 3.1 FC to Joe"
t2 = "Joe sends 2.5 FC to Adam"
t3 = "Adam sends 1.2 FC to Bob"
t4 = "Bob sends 0.5 FC to Charlie"
t5 = "Charlie sends 0.2 FC to David"
t6 = "David sends 0.1 FC to Eric"
t7 = "Luca sends 6 FC to Bisher"
t8 = "Bisher sent 8 FC to Luca"

blockchain1 = simplechain()  

# creates four blocks, more can be added at will
Genesis_block = simpleblock("Genesis block", [t1, t2])
blockchain1.append_block(Genesis_block.block_data, Genesis_block.block_hash)
blockchain1.i += 1

block2 = simpleblock(Genesis_block.block_hash, [t3, t4])
blockchain1.append_block(block2.block_data, block2.block_hash)
blockchain1.i += 1

block3 = simpleblock(block2.block_hash, [t5, t6])
blockchain1.append_block(block3.block_data, block3.block_hash)
blockchain1.i += 1

block4 = simpleblock(block3.block_hash, [t7, t8])
blockchain1.append_block(block4.block_data, block4.block_hash)
blockchain1.i += 1

# Displays blockchain
blockchain1.display_chain()


