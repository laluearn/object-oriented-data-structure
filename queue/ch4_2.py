class Queue:
       def __init__(self):
              self.items = []

       def __str__(self):
              return str(self.items)
              
       def Enqueue(self, items):
            self.items.append(items)
       
       def Dequeue(self):
              if not self.isEmpty():
                     return self.items.pop(0)
              return -1

       def isEmpty(self):
              return self.size() == 0
       
       def size(self):
              return len(self.items)
       
       def Queue(self):
              return self.items
       
       def Value(self, value):
              return self.items[value]
       
       def isFull(self):
              return self.items.full()

inp = input("Enter Input : ").split(",")
queue = Queue()
tempQ = Queue()

for i in inp:
       if "EN" in i:
            queue.Enqueue(i.split(" ")[1])
       elif "ES" in i:
            tempQ.Enqueue(i.split(" ")[1])

       elif "D" in i:
              if not tempQ.isEmpty():
                     print(tempQ.Dequeue())
              elif not queue.isEmpty():
                     print(queue.Dequeue())
              else :
                     print("Empty")