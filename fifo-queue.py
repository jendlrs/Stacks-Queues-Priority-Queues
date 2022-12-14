from queues import Queue

fifo = Queue("1st", "2nd", "3rd")
print(len(fifo)) #Printing the number of items

for element in fifo:
    print(element) #Printing all the elements

print(len(fifo)) #Updated number of elements

#Other Way

#Adding Elements
fifo.enqueue("1st") 
fifo.enqueue("2nd")
fifo.enqueue("3rd")

print(len(fifo))

#Removing Elements
fifo.dequeue()
'1st'
fifo.dequeue()
'2nd'
fifo.dequeue()
'3rd'

print(len(fifo))