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
       
       def items(self):
              return self.items

def checkMap(width, height, roomSize):
    mapStatus = False
    if len(roomSize) != height:
        return False
    else:
        for i in roomSize:
            if len(i) != width:
                return False
            if "F" in i:
                mapStatus = True
    return mapStatus

width, height, room = input("Enter width, height, and room: ").split(" ")
width = int(width)
height = int(height)
roomSize = room.split(",")

queue = Queue()
final = []
path = []

for row in roomSize:
    tempRoom = []
    for col in row:
        tempRoom.append(col)
        if col == "F":
            path.append((row.index(col), roomSize.index(row)))
            queue.Enqueue((row.index(col), roomSize.index(row)))
    if not checkMap(width, height, roomSize):
        print("Invalid map input.")
        exit()
    final.append(tempRoom)

scan_set = [(0,-1),(1,0),(0,1),(-1,0)]
while not queue.isEmpty():
    print(f'Queue: {queue}')
    x,y = queue.Dequeue()
    for setx,sety in scan_set:
        if y+sety >= 0 and y+sety < height and x+setx >= 0 and x+setx < width:
            pos = final[y+sety][x+setx]
            if pos == 'O':
                print('Found the exit portal.')
                exit()
            elif pos == '_' and (x+setx,y+sety) not in path :
                path.append((x+setx,y+sety))
                queue.Enqueue((x+setx,y+sety))
print('Cannot reach the exit portal.')