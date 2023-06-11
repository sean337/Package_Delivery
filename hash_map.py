# Class creates and implements a hash map
class HashMap:

    def __init__(self, initial_size=40):
        self.list = []
        for num in range(initial_size):
            self.list.append([])

    # Inserts a new item in the hash map
    # Citing Source: W-1_ChainingHashTable_zyBooks_Key-Value.py
    def insert(self, key, item):  # does both insert and update
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Removes an item from the hash map
    def remove(self, key, item):
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        for index, key_value in enumerate(bucket_list):
            if key == key_value[0]:
                del bucket_list[index]
                return True

    # looks up an existing item in the hash map
    def lookup(self, key):
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]
        for pair in bucket_list:
            if key == pair[0]:
                return pair[1]
