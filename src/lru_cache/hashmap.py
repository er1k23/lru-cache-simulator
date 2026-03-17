#get     → O(1)
#put     → O(1)
#delete  → O(1)

class HashMap:

    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]
        self.size = 0
        self.load_factor_threshold = 0.7


    def _hash(self, key):
        return key % self.capacity


    def _resize(self):
        # RESIZE STARTS HERE
        old_table = self.table  # keep old data

        #increase number of buckets (capacity doubles)
        self.capacity *= 2

        # create new empty table with bigger capacity
        self.table = [[] for _ in range(self.capacity)]

        #reset size because we will reinsert everything
        self.size = 0

        #REHASHING PROCESS:
        # We must recompute index for each key using new capacity
        for bucket in old_table:
            for key, node in bucket:
                # Each key is hashed again with new capacity
                # new_index = key % new_capacity
                self.put(key, node)


    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for existing_key, node in bucket:
            if existing_key == key:
                return node

        return None


    def put(self, key, node):

        index = self._hash(key)
        bucket = self.table[index]

        for entry in bucket:
            if entry[0] == key:
                entry[1] = node
                return

        bucket.append([key, node])
        self.size += 1

        # LOAD FACTOR CHECK:
        # if too many elements per bucket → trigger resize
        if self.size / self.capacity > self.load_factor_threshold:
            self._resize()  #triggers resizing + rehashing


    def delete(self, key):

        index = self._hash(key)
        bucket = self.table[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                del bucket[i]
                self.size -= 1
                return