# from queue import PriorityQueue

# q = PriorityQueue()

# q.put(-11)
# q.put(-5)
# q.put(-2)
# q.put(-5)
# q.put(-6)
# # q.put(0)

# # while not q.empty():
# #     next_item = q.get()
# #     print(next_item, end = " ")

# print(-1 * q.queue[0])

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return " ".join([str(i) for i in self.queue])
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def insert(self, ele):
        self.queue.append(ele)
    
    def delete(self):
        try:
            max_val = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max_val]:
                    max_val = i
            item = self.queue[max_val]
            del self.queue[max_val]
            return item
        except IndexError:
            print(e)
            exit()

if __name__ == "__main__":
    myQueue = PriorityQueue()
    myQueue.insert(1)
    myQueue.insert(-1)
    myQueue.insert(10)

    while not myQueue.isEmpty():
        print(myQueue.delete())