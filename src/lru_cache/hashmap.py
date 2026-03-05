#get     → O(1)
#put     → O(1)
#delete  → O(1)

class HashMap:

    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]


    def _hash(self, key):
        return key % self.capacity


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


    def delete(self, key):

        index = self._hash(key)
        bucket = self.table[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                del bucket[i]
                return