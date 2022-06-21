#<---------DICTIONARY-------->
#creating and acessing the dictionary's value
'''
myDict = {
    "name": "Shantanu",
    "employeeID": 10703098,
    "anotherDict": {"hobbies": "Singing"}, #nested dictionary
    "marks": [23, 45, 65]
}
myDict["marks"] = [34, 78, 98]
print(myDict["employeeID"])
print(myDict["anotherDict"]["hobbies"])
print(myDict["marks"])

'''

#Dictionary methods--
'''
myDict = {
    "name": "Shantanu",
    "employeeID": 10703098,
    "anotherDict": {"hobbies": "Singing"}, #nested dictionary
    "marks": [23, 45, 65],
    1:2                   #keys and values both can be integers also
}
print(myDict.keys())  #print the keys in the list format but the class will be 'dict_keys'
print(type(myDict.keys()))   #print the class of keys and i.e.<class 'dict_keys'>
print(list(myDict.keys()))   #typecast to list of the above output

print(myDict.values())  #print the values in the dictionary
print(list(myDict.values())) #typecast to list of the above output 

print(myDict.items()) # Prints the (key, value) for all contents of the dictionary

updateDict = {
    "Lovish": "Friend",
    "Divya": "Friend",
    "Rakesh": "Friend",
    "name": "jagdish"    #if we upadte with the same keys it will over-write the previous value
}
myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)


print(myDict.get("marks")) # Prints value associated with key "harry"
print(myDict["marks"]) # Prints value associated with key "harry"
# The difference between .get and [] sytax in Dictionaries?
print(myDict.get("harry2")) # Returns None as harry2 is not present in the dictionary
print(myDict["harry2"]) # throws an error as harry2 is not present in the dictionary

'''

#<---------SETS----------->
'''
It is the collection of non-repetitive elements
'''
#creating and exploring sets
'''
a = {1, 3, 4, 5, 1}
print(type(a)) #tells the type of this object and i.e. 'set'
print(a)     #it will not print '1' again, as repeatition is not allowed in set 

#--empty set
# Important: This syntax will create an empty dictionary and not an empty set
a = {}
print(type(a))

# An empty set can be created using the below syntax:
b = set()
print(type(b))

'''

#--methods in sets
'''
# Creating an empty set
b = set()
print(type(b))

## Adding values to an empty set
b.add(4)
b.add(4)
b.add(5)
b.add(5) # Adding a value repeatedly does not changes a set
b.add((4, 5, 6))

## Accessing Elements
# b.add({4:5}) # Cannot add list or dictionary to sets
print(b)

## Length of the Set
print(len(b)) # Prints the length of this set

## Removal of an Item
b.remove(5) # Removes 5 fromt set b
# b.remove(15) # throws an error while trying to remove 15 (which is not present in the set)
print(b)

print(b.pop()) #it will randomly pop out the element from our set
print(b)

'''

#<-------Practice sets-------->

#problem 1
'''
myDict = {
    "Pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "Item"
}
print("Options are ", myDict.keys())
a = input("Enter the Hindi Word\n")
# print("The meaning of your word is:", myDict[a])

# Below line will not throw an error if the key is not present in the dictionary
print("The meaning of your word is:", myDict.get(a))
'''

#problem 2
'''
num1 = int(input("Enter number 1\n"))
num2 = int(input("Enter number 2\n"))
num3 = int(input("Enter number 3\n"))
num4 = int(input("Enter number 4\n"))
num5 = int(input("Enter number 5\n"))
num6 = int(input("Enter number 6\n"))
num7 = int(input("Enter number 7\n"))
num8 = int(input("Enter number 8\n"))

s = {num1, num2, num3, num4, num5, num6, num7, num8}
print(s)
'''

#problem 3
'''
s = {18, "18", 18.1}
print(s)

'''

#problem 4
'''
favLang = {}
a = input("Enter your favorite language Shubham\n")
b = input("Enter your favorite language Ankit\n")
c = input("Enter your favorite language Sonali\n")
d = input("Enter your favorite language Harshita\n")
favLang['shubham'] = a  #entering key and value to thr dictionary
favLang['ankit'] = b
favLang['sonali'] = c
favLang['harshita'] = d

print(favLang)
'''
# a = {}
# b = set()
