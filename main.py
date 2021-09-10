# Step 1 receive user input, which will be amount of elements in second line.

n = int(input())

# Step 2  create a list to store numbers

temp = list

# Step 3 store next input into list where each element is separated by ' '

temp = input().split(' ')

# Step 4 for each element run if less than 0 and add one to count.

count = 0

for i in range(n):
    a = int(temp[i])
    if a < 0:
        count += 1
        i += 1
    else:
        i += 1

print(count)
