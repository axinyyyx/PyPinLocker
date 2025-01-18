from itertools import product  # Import product from itertools to generate Cartesian product

def generate_pin_combinations():
    # Take input from the user for the number of digits in the password
    num_digits = int(input("Enter the number of digits for the PIN: "))

    # Create a list of digits from 0 to 9
    digits = [str(i) for i in range(10)]

    # Generate all possible combinations based on user input
    combinations = product(digits, repeat=num_digits)

    # Initialize an empty list to store passwords
    password_list = []

    # Add each combination to the password_list
    for combination in combinations:
        password_list.append(''.join(combination))  # Convert combination to a string and add to the list
        print(password_list)  # Print the current password list (optional)

    # Create a filename based on the number of digits
    filename = f'{num_digits}_digit_{10**num_digits}_password_list.txt'

    # Save the password list to a text file
    with open(filename, 'w') as f:
        f.write(f"{password_list}")  # Write the password list to the file
        print(f"All {num_digits}-digit passwords saved to {filename}")  # Print a confirmation message

# Call the function
generate_pin_combinations()
