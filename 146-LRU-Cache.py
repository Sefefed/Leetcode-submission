class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity 
        self.cache = {}
        self.size = 0

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head
    def add_Node(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node     
        self.head.next = node
    def delete_Node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def pop_tail(self):
        res = self.tail.prev
        self.delete_Node(res)
        return res
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key, None)
        if not node:
            return -1
        else:
            self.delete_Node(node)
            self.add_Node(node)
        return node.val    
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.cache.get(key, None)
        if not node:
            node = Node(key, value)
            self.cache[key] = node
            self.add_Node(node)
            self.size += 1
            if self.size > self.capacity:
                tail = self.pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.val = value
            self.delete_Node(node)
            self.add_Node(node)        


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)