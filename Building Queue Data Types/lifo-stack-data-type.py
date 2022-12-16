from queues import Stack

lifo = Stack("1st", "2nd", "3rd")

for element in lifo:
    print(element)

print(len(lifo))
lifo = []

#Adding Elements
lifo.append("1st")
lifo.append("2nd")
lifo.append("3rd")

print(len(lifo))

#Removing Elements
lifo.pop()
'3rd'
lifo.pop()
'2nd'
lifo.pop()
'1st'

print(len(lifo))
