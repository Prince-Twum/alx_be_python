# pattern_drawing.py
# Ask the user for the size of the square pattern and draw it using a while loop
while True:
    try:
        size = int(input("Enter the size of the pattern: "))
        if size <= 0:
            print("Please enter a positive integer.")
            continue
        break
    except ValueError:
        print("That is not a valid integer. Please try again.")

# row will keep track of which row we're printing (start at 0)
row = 0
while row < size:
    # For each row, print 'size' asterisks on the same line using a for loop
    for col in range(size):
        # print "*" without newline; end="" keeps printing on same line
        print("*", end="")
    # After printing all columns for this row, move to the next line
    print()
    # increment row counter
    row += 1
