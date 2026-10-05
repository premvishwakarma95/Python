# In this program we have created a list name marks, it's same as JS array and have used it's methods (max, min, len)
marks = [75, 82, 60, 95, 48]
total = sum(marks)
average = total / len(marks)
print("Total:", total)
print("Average:", average)
print("Highest:", max(marks))
print("Lowest:", min(marks))

for mark in marks:
    if mark >= 50:
        print(mark, "Pass")
    else:
        print(mark, "Fail")


# Create a list of five fruits and print it. Add a fruit using append().
fruits = ['apple', 'mango', 'banana', 'fruit4', 'fruit5'];
fruits.append('fruite6')
print(fruits);

# Insert a fruit at index 2 And then remove.
fruits.insert(2, 'newFruit');
print(fruits)
fruits.remove('newFruit')
print(fruits)

# Print every fruit using a for loop.
for fruit in fruits:
    print(fruit)

# Check whether "Apple" exists in the list.
isExists = "apple" in fruits;
print(f"apple exists or not: {isExists}")