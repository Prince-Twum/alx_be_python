# Ask the user for a number and convert it to an integer
number = int(input("Enter a number to see its multiplication table: "))

# Loop from 1 to 10
for i in range(1, 11):
    # Calculate product
    product = number * i
    # Print result
    print(f"{number} * {i} = {product}")
