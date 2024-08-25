class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)
    
    def enqueue(self, i):
        self.items.append(i)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

queue = Queue()
inp = input("Enter Input : ").split(",")

for i in inp:
    item = i.split()
    if item[0] == "E":
        queue.enqueue(item[1])
        print(f"Add {item[1]} index is {queue.size() - 1}")
    elif item[0] == "D":
        if not queue.isEmpty():
            print(f"Pop {queue.dequeue()} size in queue is {queue.size()}")
        else:
            print("-1")

if not queue.isEmpty():
    print(f"Number in Queue is :  {queue}")
else:
    print("Empty")