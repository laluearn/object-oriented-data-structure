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
# set value
myQueue = Queue()
yourQueue = Queue()
myAct = Queue()
yourAct = Queue()
score = 0

activities = {'0':'Eat', '1':'Game', '2':'Learn', '3':'Movie'}
locations = {'0':'Res.', '1':'ClassR.', '2':'SuperM.', '3':'Home'}

for i in inp:
    ans = i.split(" ")
    mine = ans[0].split(":")
    your = ans[1].split(":")
    if mine == your: 
        score += 4
    elif mine[1] == your[1]: 
        score += 2
    elif mine[0] == your[0]: 
        score += 1
    else: 
        score -= 5

    myQueue.Enqueue(ans[0])
    yourQueue.Enqueue(ans[1])
    a = activities.get(mine[0]) + ":" + locations.get(mine[1])
    myAct.Enqueue(a)
    a = activities.get(your[0]) + ":" + locations.get(your[1])
    yourAct.Enqueue(a)

print("My   Queue = " + str(myQueue).replace("\'",'').replace("[",'').replace("]",''))
print("Your Queue = " + str(yourQueue).replace("\'",'').replace("[",'').replace("]",''))
print("My   Activity:Location = " + str(myAct).replace("\'",'').replace("[",'').replace("]",''))
print("Your Activity:Location = " + str(yourAct).replace("\'",'').replace("[",'').replace("]",''))

if score >= 7:
    print("Yes! You're my love! : Score is " + str(score) + '.')
elif score > 0:
    print("Umm.. It's complicated relationship! : Score is " + str(score) + '.')
else:
    print("No! We're just friends. : Score is " + str(score) + '.')