#Today practice topic
#lists
#Create a list of 5 numbers and print it.
numbers=[10,20,30,40,50]
print(numbers)
#Print the first element of a list.
print(numbers[0])
#Print the last element of a list.
print(numbers[4])
#Print all elements using a for loop.
for i in numbers:
    print(i)
#Find the length of a list.
print(len(numbers))
numbers=[10,20,30,40]
print(numbers.append(50))
print(numbers)
#Insert an element at the third position.
print(numbers.insert(2,34))
print(numbers)
#Remove an element using remove().
numbers=[10,20,30,40]
print(numbers.remove(30))
print(numbers)
#Remove the last element using pop().
print(numbers.pop())
print(numbers)
# Replace the second element with a new value.
numbers[1]=45
print(numbers)
#Find the largest element in a list.
numbers=[12,67,34,89,23]
largest=max(numbers)
print("largest element:",largest)
