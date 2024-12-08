class BTreeNode:
    def __init__(self, block_id=0, parent_id=0, keys=None, values=None, children=None, n=0):
        self.block_id = block_id
        self.parent_id = parent_id
        self.n = n
        self.keys = keys if keys is not None else [0] * 19
        self.values = values if values is not None else [0] * 19
        self.children = children if children is not None else [0] * 20

    def serialize(self) -> bytes:
        block = bytearray(512)
        block[0:8] = self.block_id.to_bytes(8, 'big')
        block[8:16] = self.parent_id.to_bytes(8, 'big')
        block[16:24] = self.n.to_bytes(8, 'big')
        offset = 24
        for k in self.keys:
            block[offset:offset+8] = k.to_bytes(8, 'big')
            offset += 8
        for v in self.values:
            block[offset:offset+8] = v.to_bytes(8, 'big')
            offset += 8
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
        node.keys = [int.from_bytes(block[offset + i*8:offset + (i+1)*8], 'big') for i in range(19)]
        node.values = [int.from_bytes(block[offset + (i+19)*8:offset + (i+20)*8], 'big') for i in range(19)]
        node.children = [int.from_bytes(block[offset + (i+38)*8:offset + (i+39)*8], 'big') for i in range(20)]
        return node

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

    def write_header(self):
        block = bytearray(512)
        block[0:8] = b"4337PRJ3"
        block[8:16] = self.root_id.to_bytes(8, 'big')
        block[16:24] = self.next_block_id.to_bytes(8, 'big')
        self.file.seek(0)
        self.file.write(block)

    def read_header(self):
        self.file.seek(0)
        block = self.file.read(512)
        if len(block) < 512 or block[0:8] != b"4337PRJ3":
            raise ValueError("Invalid header.")
        self.root_id = int.from_bytes(block[8:16], 'big')
        self.next_block_id = int.from_bytes(block[16:24], 'big')
