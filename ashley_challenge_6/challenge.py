import heapq

def sliding_window(sequence, k, n):
    result = ""
    start = 0
    heap = [-1*x for x in sequence[0:k]]

    if len(sequence) < k:
        return result

    #average and maximum for the first window
    average = sum(sequence[0:k])/k

    #initialize heap for max heap
    heapq.heapify(heap)
    maximum = -1*heap[0]

    result += str(average)+","+str(maximum)
    
    start += 1 
    
    for stop in range(k, n):
        average = ((average*k)-sequence[start-1]+sequence[stop])/k

        #find maximum
        heapq.heappush(heap, -1*sequence[stop])

        #if element outside the window isn't maximum, it doesn't have to be removed
        #else, remove it

        if heap[0] == -1*sequence[start-1]:
            heapq.heappop(heap)
        # print(heap)
        maximum = -1*heap[0]

        result += "\n"+str(average)+","+str(maximum)
        
        start += 1

    return result

#input
line = input().split()
n = int(line[0])
k = int(line[1])
sequencestr = input().split()
sequence = []
for i in sequencestr:
    sequence.append(int(i))

print(sliding_window(sequence, k, n))
