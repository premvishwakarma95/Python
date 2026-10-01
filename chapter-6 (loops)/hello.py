# We’ll cover for, range(), while, break, and continue.

# for loop
for number in range(3):
    print("Prem")


for character in "Prem":
    print(character)


# Using range()
# range(start, stop, step)
# start: where to begin; defaults to 0.
# stop: where to stop; this value is excluded.
# step: how much to increase or decrease; defaults to 1.

# range() produces a sequence of integers that we can loop through.
# range(5)          --	    0, 1, 2, 3, 4
# range(1, 6)       --	    1, 2, 3, 4, 5
# range(2, 11, 2)	--      2, 4, 6, 8, 10
# range(5, 0, -1)   ---     5, 4, 3, 2, 1


# Count backwards from 5 to 1
for number in range(5, 0, -1):
    print(number)



# The while loop
# A while loop repeats as long as its condition is true.
number = 1

while number <= 5:
    print(number)
    number += 1



# break — exit the loop 
# break immediately ends the nearest enclosing loop.
for number in range(1, 6):
    if number == 3:
        break

    print(number)
# Output:
# 1
# 2



# 6. continue — skip the current iteration
for number in range(1, 6):
    if number == 3:
        continue

    print(number)
# Output:
# 1
# 2
# 4
# 5
# The loop skips printing 3, then continues with 4 and 5.