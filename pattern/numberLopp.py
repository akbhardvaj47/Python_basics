# Define the size of the square (for 20 numbers, we need a 5x5 grid)
n = 5

# Initialize the boundaries for the spiral
top, bottom, left, right = 0, n - 1, 0, n - 1
num = 1  # Start from 1

# Loop until the boundaries converge
while top <= bottom and left <= right:
    # Print the top row
    for i in range(left, right + 1):
        print(num, end=" ")
        num += 1
    top += 1  # Move the top boundary down

    # Print the right column
    for i in range(top, bottom + 1):
        print(num, end=" ")
        num += 1
    right -= 1  # Move the right boundary left

    # Print the bottom row (if not already printed)
    if top <= bottom:
        for i in range(right, left - 1, -1):
            print(num, end=" ")
            num += 1
        bottom -= 1  # Move the bottom boundary up

    # Print the left column (if not already printed)
    if left <= right:
        for i in range(bottom, top - 1, -1):
            print(num, end=" ")
            num += 1
        left += 1  # Move the left boundary right

    # Print a new line after each row
    print()
