from itertools import product  # Import product from itertools to generate Cartesian product

# Create a list of digits from 0 to 9
digits = [str(i) for i in range(10)]

# Generate all possible 4-digit combinations
combinations = product(digits, repeat=4)

# Initialize an empty list to store passwords
password_list = []

# Add each combination to the password_list
for combination in combinations:
    password_list.append(''.join(combination))  # Convert combination to a string and add to the list
    print(password_list)  # Print the current password list

# Save the password list to a text file
with open('password_list.txt', 'w') as f:
    f.write(f"{password_list}")  # Write the password list to the file
    print("All Password's Save")  # Print a confirmation message
