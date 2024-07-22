def queue(inp):
    queue = []
    for i in range(len(inp)):
        ans = inp[i].split()
        # print(ans[0], ans[1])
        if ans[0] == "E":
            queue.append(ans[1])
            print("Add", ans[1], "index is", (len(queue)-1))
        elif ans[0] == "D":
            if len(queue) != 0:
                
                if queue:
                    print("Pop", queue[0], "size in queue is", (len(queue)-1))
                    queue.pop(0)
            else: 
                print("-1")
    
    if len(queue) != 0:
        print("Number in Queue is : ", queue)
    else:
        print("Empty")


inp = input("Enter Input : ").split(",")
queue(inp)