from itertools import product  # Import product from itertools to generate Cartesian product

def generate_pin_combinations():
    # Take input from the user for the number of digits in the password
    num_digits = int(input("Enter the number of digits for the PIN: "))
    
    # Ask the user for the mode of generation
    print("Select the mode of generation:")
    print("1. Fast Mode")
    print("2. Slow Mode with H4c👑 Effect")
    query = int(input("Enter 1 or 2: "))

    # Create a list of digits from 0 to 9
    digits = [str(i) for i in range(10)]

    # Generate all possible combinations based on user input
    combinations = product(digits, repeat=num_digits)

    # Create a filename based on the number of digits
    filename = f'{num_digits}_digit_{10**num_digits}_password_list.txt'
    
    if query == 1:
        print("Generating combinations in Fast Mode...")
        # Open the file in write mode
        with open(filename, 'w') as f:
            for combination in combinations:
                # Join the combination tuple into a string and write it to the file
                f.write(''.join(combination) + '\n')

        print(f"All {num_digits}-digit passwords have been successfully saved to {filename}.")
    
    elif query == 2:
        print("Generating combinations in Slow Mode with H4c👑 Effect...")
        # Initialize an empty list to store passwords
        password_list = []

        # Add each combination to the password_list
        for combination in combinations:
            password_list.append(''.join(combination))  # Convert combination to a string and add to the list
            print(f"Current combinations: {password_list}")  # Print the current password list (optional)

        # Save the password list to a text file
        with open(filename, 'w') as f:
            f.write('\n'.join(password_list))  # Write the password list to the file
            print(f"All {num_digits}-digit passwords have been successfully saved to {filename}.")

# Call the function
generate_pin_combinations()
