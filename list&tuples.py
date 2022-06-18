#<------------LIST----------------->
 
# Create a list using []
a = [1, 2 , 4, 56, 6]

# Print the list using print() function
print(a)

# Access using index using a[0], a[1], a[2]
print(a[2])

# Change the value of list using
a[0] = 98
print(a)

# We can create a list with items of different types
c = [45, "Harry", False, 6.9]
print(c)

# List slicing
friends = ["Harry", "Tom", "Rohan", "Sam", "Divya", 45]
print(friends[0:4])
print(friends[-4:])

l1 = [1, 8, 7, 2, 21, 15]
print(l1)
# l1.sort() # sorts the list
# l1.reverse() # reverses the list
#l1.append(45) # adds 45 at the end of the list 
# l1.insert(2, 544) # inserts 544 at index 2
# l1.pop(2) # removes element at index 2
l1.remove(21) # removes 21 from the list
print(l1) #-------------- other methods can be explore in python official documents




#<-----------TUPLES---------->


# Creating a tuple using ()
t = (1, 2, 4, 5)

# t1 = () # Empty tuple
# t1 = (1) # Wrong way to declare a Tuple with Single element
t1 = (1,) # Tuple with Single element
print(t1)

# Printing the elements of a tuple
# print(t[0])

# Cannot update the values of a tuple
# t[0] = 34 # throws an error

#tuple method
# Creating a tuple using ()
t = (1, 2, 4, 5, 4, 1, 2,1 ,1)

print(t.count(1))
print(t.index(5))



#<---------Practice set------------->
#problem1
'''
f1 = input("Enter Fruit Number 1: ")
f2 = input("Enter Fruit Number 2: ")
f3 = input("Enter Fruit Number 3: ")
f4 = input("Enter Fruit Number 4: ")
f5 = input("Enter Fruit Number 5: ")
f6 = input("Enter Fruit Number 6: ")
f7 = input("Enter Fruit Number 7: ")

myFruitList = [f1, f2, f3, f4, f5, f6, f7]
print(myFruitList)
'''
#problem 2
'''
m1 = int(input("Enter Marks for Student Number 1: "))
m2 = int(input("Enter Marks for Student Number 2: "))
m3 = int(input("Enter Marks for Student Number 3: "))
m4 = int(input("Enter Marks for Student Number 4: "))
m5 = int(input("Enter Marks for Student Number 5: "))
m6 = int(input("Enter Marks for Student Number 6: "))

myList = [m1, m2, m3, m4, m5, m6]
myList.sort() #For marks sorting
print(myList)
'''

#problem 3
'''
a = [2, 4, 56, 7]

print(a[0] + a[1] + a[2] + a[3]) 
print(sum(a)) #sum method of list to sum up the elements
'''

# if (14<7): 
#     print(True)
# else:
#     print(False)
        

