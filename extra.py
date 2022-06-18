''''
toDoList = ["Brush", "Gym", "Breakfast", "meeting", "padhai"]
#print(toDoList)

for i in toDoList:
    print(i)
    if (i == "Breakfast"):
        #print(i)
        break
'''
'''
#finding the position of elements using index method
toDoList = ["Brush", "Gym", "Breakfast", "meeting", "padhai"]
#print(toDoList)

for i in toDoList:
    #print(i)
    if (i == "Breakfast"):
        print(toDoList.index(i))
        break    
'''

#finding the position of an element without using index method
toDoList = ["Brush", "Gym", "Breakfast", "meeting", "padhai"]
#print(toDoList)
counter = -1
for i in toDoList:
    #print(i)
    counter += 1
    if (i == "Breakfast"):
        #print(i)
        break
print(counter)


