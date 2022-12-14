from queues import Queue

fifo = Queue("1st", "2nd", "3rd")
print(len(fifo))

for element in fifo:
    print(element)

print(len(fifo))

#fifo.enqueue("1st")
#fifo.enqueue("2nd")
#fifo.enqueue("3rd")

#fifo.dequeue()
#'1st'
#fifo.dequeue()
#'2nd'
#fifo.dequeue()
#'3rd'