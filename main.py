import os
import sys
from bisect import bisect_left


BLOCK_SIZE = 512
MAGIC_NUMBER = b"4337PRJ3"
T = 10  # minimal degree
MAX_KEYS = 2 * T - 1  # 19
MAX_CHILDREN = 2 * T  # 20
class BTreeNode:
    def __init__(self, block_id=0, parent_id=0, keys=None, values=None, children=None, n=0):
        self.block_id = block_id
        self.parent_id = parent_id
        self.n = n
        self.keys = keys if keys is not None else [0]*(MAX_KEYS)
        self.values = values if values is not None else [0]*(MAX_KEYS)
        self.children = children if children is not None else [0]*(MAX_CHILDREN)

    def serialize(self) -> bytes:
        # Create a 512-byte block
        block = bytearray(BLOCK_SIZE)
        # 8 bytes: block_id
        block[0:8] = self.block_id.to_bytes(8, 'big')
        # 8 bytes: parent_id
        block[8:16] = self.parent_id.to_bytes(8, 'big')
        # 8 bytes: n
        block[16:24] = self.n.to_bytes(8, 'big')
        # Keys
        offset = 24
        for k in self.keys:
            block[offset:offset+8] = k.to_bytes(8, 'big')
            offset += 8
        # Values
        for v in self.values:
            block[offset:offset+8] = v.to_bytes(8, 'big')
            offset += 8
        # Children
        for c in self.children:
            block[offset:offset+8] = c.to_bytes(8, 'big')
            offset += 8
        return bytes(block)

    @staticmethod
    def deserialize(block: bytes):
        node = BTreeNode()
        node.block_id = int.from_bytes(block[0:8], 'big')
        node.parent_id = int.from_bytes(block[8:16], 'big')
        node.n = int.from_bytes(block[16:24], 'big')
        offset = 24
        node.keys = []
        for _ in range(MAX_KEYS):
            k = int.from_bytes(block[offset:offset+8], 'big')
            node.keys.append(k)
            offset += 8
        node.values = []
        for _ in range(MAX_KEYS):
            v = int.from_bytes(block[offset:offset+8], 'big')
            node.values.append(v)
            offset += 8
        node.children = []
        for _ in range(MAX_CHILDREN):
            c = int.from_bytes(block[offset:offset+8], 'big')
            node.children.append(c)
            offset += 8
        return node

    def is_leaf(self):
        # A node is a leaf if all children are zero
        return all(c == 0 for c in self.children)

class IndexFile:
    def allocate_node(self) -> BTreeNode:
        node = BTreeNode(block_id=self.next_block_id)
        self.next_block_id += 1
        self.write_header()
        return node

    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.root_id = 0
        self.next_block_id = 1

    def open_readwrite(self):
        self.file = open(self.filename, 'r+b')

    def open_readonly(self):
        self.file = open(self.filename, 'rb')

    def open_create(self):
        self.file = open(self.filename, 'w+b')

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

    def write_node(self, node: BTreeNode):
        block = node.serialize()
        self.file.seek(node.block_id * BLOCK_SIZE)
        self.file.write(block)

    def read_node(self, block_id: int) -> BTreeNode:
        self.file.seek(block_id * BLOCK_SIZE)
        block = self.file.read(BLOCK_SIZE)
        if len(block) < BLOCK_SIZE:
            raise IOError("Node block incomplete.")
        return BTreeNode.deserialize(block)

    def allocate_node(self) -> BTreeNode:
        node = BTreeNode(block_id=self.next_block_id)
        self.next_block_id += 1
        self.write_header()
        return node

    def sync_header(self):
        self.write_header()

    def is_open(self):
        return self.file is not None

    def write_header(self):
        block = bytearray(BLOCK_SIZE)
        # Magic number
        block[0:8] = MAGIC_NUMBER
        # root_id
        block[8:16] = self.root_id.to_bytes(8, 'big')
        # next_block_id
        block[16:24] = self.next_block_id.to_bytes(8, 'big')
        self.file.seek(0)
        self.file.write(block)

    def read_header(self):
        self.file.seek(0)
        block = self.file.read(BLOCK_SIZE)
        if len(block) < BLOCK_SIZE:
            raise IOError("Header block incomplete.")
        if block[0:8] != MAGIC_NUMBER:
            raise ValueError("Invalid magic number.")
        self.root_id = int.from_bytes(block[8:16], 'big')
        self.next_block_id = int.from_bytes(block[16:24], 'big')

class BTree:

    def __init__(self, idx_file: IndexFile):
        self.idx_file = idx_file

    def _insert_nonfull(self, node: BTreeNode, key: int, value: int):
        # node guaranteed to have space
        node = self._reload_node(node)
        i = node.n - 1
        if node.is_leaf():
            # Insert into leaf
            while i >= 0 and key < node.keys[i]:
                node.keys[i+1] = node.keys[i]
                node.values[i+1] = node.values[i]
                i -= 1
            node.keys[i+1] = key
            node.values[i+1] = value
            node.n += 1
            self.idx_file.write_node(node)
        else:
            # Insert into internal node
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            child_id = node.children[i]
            child = self.idx_file.read_node(child_id)
            if child.n == MAX_KEYS:
                self._split_child(node, i)
                # After split, decide which child to go down
                if key > node.keys[i]:
                    i += 1
                child_id = node.children[i]
                child = self.idx_file.read_node(child_id)
            self._insert_nonfull(child, key, value)

    def search(self, key: int):
        if self.idx_file.root_id == 0:
            return None
        return self._search_node(self.idx_file.root_id, key)

    def _search_node(self, block_id, key):
        node = self.idx_file.read_node(block_id)
        keys = node.keys[:node.n]
        i = bisect_left(keys, key)
        if i < node.n and keys[i] == key:
            return node.values[i]
        if node.is_leaf():
            return None
        return self._search_node(node.children[i], key)
    
    def _split_child(self, parent: BTreeNode, i: int):
        # Split child at index i
        parent = self._reload_node(parent)
        full_child_id = parent.children[i]
        full_child = self.idx_file.read_node(full_child_id)

        new_node = self.idx_file.allocate_node()
        new_node.parent_id = parent.block_id

        # Move keys and values
        mid = T-1  # median index (9 for T=10)
        new_node.n = T - 1  # 9
        for j in range(T-1):
            new_node.keys[j] = full_child.keys[j+T]
            new_node.values[j] = full_child.values[j+T]

        # If not leaf, move children
        if not full_child.is_leaf():
            for j in range(T):
                new_node.children[j] = full_child.children[j+T]
                full_child.children[j+T] = 0

        full_child.n = T-1  # 9

        # Insert new_node in parent
        for j in range(parent.n, i, -1):
            parent.children[j+1] = parent.children[j]
        parent.children[i+1] = new_node.block_id

        # Move parent's keys/values
        for j in range(parent.n-1, i-1, -1):
            parent.keys[j+1] = parent.keys[j]
            parent.values[j+1] = parent.values[j]

        # Middle key up
        parent.keys[i] = full_child.keys[mid]
        parent.values[i] = full_child.values[mid]

        # Clear the moved key/value from full_child
        full_child.keys[mid] = 0
        full_child.values[mid] = 0
        for k in range(mid+1, mid+T):
            full_child.keys[k] = 0
            full_child.values[k] = 0

        parent.n += 1

        self.idx_file.write_node(full_child)
        self.idx_file.write_node(new_node)
        self.idx_file.write_node(parent)

    def insert(self, key: int, value: int):
        # Check for duplicate
        if self.search(key) is not None:
            print("Error: key already exists.")
            return
        if self.idx_file.root_id == 0:
            # Tree empty, create root
            root = self.idx_file.allocate_node()
            root.n = 1
            root.keys[0] = key
            root.values[0] = value
            self.idx_file.root_id = root.block_id
            self.idx_file.write_node(root)
            self.idx_file.sync_header()
        else:
            root = self.idx_file.read_node(self.idx_file.root_id)
            if root.n == MAX_KEYS:
                # Need a new root
                new_root = self.idx_file.allocate_node()
                new_root.children[0] = root.block_id
                root.parent_id = new_root.block_id
                self.idx_file.write_node(root)
                self._split_child(new_root, 0)
                self._insert_nonfull(new_root, key, value)
                self.idx_file.root_id = new_root.block_id
                self.idx_file.write_node(new_root)
                self.idx_file.sync_header()
            else:
                self._insert_nonfull(root, key, value)

def main():
    idx_file = None
    btree = None

    def ensure_open():
        if idx_file is None or not idx_file.is_open():
            print("Error: No index file is open.")
            return False
        return True

    while True:
        print("Commands: create, open, insert, search, load, print, extract, quit")
        cmd = input("Enter command: ").strip().lower()
        if cmd == "quit":
            if idx_file:
                idx_file.close()
            break
        elif cmd == "create":
            fname = input("Enter new index file name: ").strip()
            if os.path.exists(fname):
                ans = input(f"File {fname} exists. Overwrite? (y/n) ")
                if ans.lower() != 'y':
                    continue
            # create file
            if idx_file:
                idx_file.close()
            idx_file = IndexFile(fname)
            idx_file.open_create()
            idx_file.root_id = 0
            idx_file.next_block_id = 1
            idx_file.write_header()
            btree = BTree(idx_file)