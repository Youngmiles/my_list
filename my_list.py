# Creating an empty list
my_list = []

# Appending elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)

# Extending list
my_list.extend([50, 60, 70])

# Removing the last element
my_list.pop()

# Sorting
my_list.sort()

# printing the index of the value 30
index_30 = my_list.index(30)
print("Index of 30:", index_30)

print("Final List:", my_list)
