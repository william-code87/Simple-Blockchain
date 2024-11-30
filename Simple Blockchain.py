import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_to_hash = (str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode()
        return hashlib.sha256(data_to_hash).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), time.time(), data, latest_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                print(f"Block {current_block.index} has been tampered with!")
                return False

            if current_block.previous_hash != previous_block.hash:
                print(f"Block {current_block.index} is not linked to the previous block!")
                return False

        return True

if __name__ == "__main__":
    blockchain = Blockchain()

    blockchain.add_block("Transaction 1: Alice pays Bob 10 BTC")
    blockchain.add_block("Transaction 2: Bob pays Charlie 5 BTC")

    for block in blockchain.chain:
        print(f"Index: {block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Hash: {block.hash}")
        print(f"Previous Hash: {block.previous_hash}\n")

    print("Is blockchain valid?:", blockchain.is_chain_valid())