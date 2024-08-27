# Step 1: Created an empty list
my_list = []
print("Initial list:", my_list)

# Step 2: Appended numbers to the list one at a time
my_list.append(10)  # Appended 10 to the list
print("After appending 10:", my_list)

my_list.append(20)  # Appended 20 to the list
print("After appending 20:", my_list)

my_list.append(30)  # Appended 30 to the list
print("After appending 30:", my_list)

my_list.append(40)  # Appended 40 to the list
print("After appending 40:", my_list)

# (Alternative) Could have added all numbers at once using extend()
# my_list.extend([10, 20, 30, 40])  # Adds 10, 20, 30, and 40 to the list together
# print("After extending with [10, 20, 30, 40]:", my_list)

# Step 3: Inserted the number 15 at the second position (index 1)
my_list.insert(1, 15)  # Inserted 15 after 10
print("After inserting 15 at index 1:", my_list)

# Step 4: Created another list with more numbers
new_list = [50, 60, 70]  # Created new_list with 50, 60, 70

# Extended my_list with the new_list
my_list.extend(new_list)  # Added all elements from new_list to my_list
print("After extending with new_list:", my_list)

# Step 5: Removed the last number from the list
my_list.pop()  # Removed the last item (70) from the list
print("After popping the last element:", my_list)

# Step 6: Sorted the list in ascending order
my_list.sort()  # Sorted my_list from smallest to largest
print("After sorting:", my_list)

# Step 7: Found the index of the number 30
index_of_30 = my_list.index(30)  # Found the position of 30 in the list
print("The index of 30 in my_list is:", index_of_30)


##//HERE IS THE OUTPUT FOR THE ABOVE CODE.
# Initial list: []
# After appending 10: [10]
# After appending 20: [10, 20]
# After appending 30: [10, 20, 30]
# After appending 40: [10, 20, 30, 40]
# After inserting 15 at index 1: [10, 15, 20, 30, 40]
# After extending with new_list: [10, 15, 20, 30, 40, 50, 60, 70]
# After popping the last element: [10, 15, 20, 30, 40, 50, 60]   
# After sorting: [10, 15, 20, 30, 40, 50, 60]
# The index of 30 in my_list is: 3