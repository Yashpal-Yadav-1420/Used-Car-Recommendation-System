# Function to simulate fruit growth
"""def magical_fruit_garden(days, watering):
    fruits = [i + 1 for i in range(days)]  # Fruits grow sequentially: 1, 2, 3, ...
    
    for day in range(days):
        if watering[day].lower() == 'yes':
            fruits = [size * 2 for size in fruits]  # Double the size if watered
        
    total_size = sum(fruits)
    even_count = sum(1 for fruit in fruits if fruit % 2 == 0)
    
    return total_size, even_count

# User input
num_days = int(input("Enter the number of days you want to grow the fruits: "))
watering_status = [input(f"Did you water the fruits on day {i+1}? (yes/no): ") for i in range(num_days)]

# Compute results
total_size, even_fruits = magical_fruit_garden(num_days, watering_status)

# Output results
print("Total size of all fruits after", num_days, "days:", total_size)
print("Number of fruits ready for harvesting (even-sized):", even_fruits)"""

def magical_fruit_garden():
    #Ask the user for the number of days they want to grow the fruits.
    num_days = int(input("Enter the number of days to grow the fruits: "))

    # Initialize variables.
    fruit_sizes = [0] * num_days  # To store the size of each fruit on each day.
    total_size = 0
    even_count = 0

    # Calculate fruit sizes and track watering.
    for day in range(num_days):
        # Calculate the base size of the fruit for the current day.
        base_size = day + 1

        # Ask if the user watered the fruits on this day.
        watered = input(f"Did you water the fruits on day {day + 1}? (yes/no): ")

        # Apply watering effect if applicable.
        if watered == "yes":
            fruit_size = base_size * 2
        else:
            fruit_size = base_size

        # Store the fruit size for this day.
        fruit_sizes[day] = fruit_size

        # Update the total size.
        total_size += fruit_size

        # Check if the fruit is even-sized for harvesting.
        if fruit_size % 2 == 0:
            even_count += 1

    # Print the total size of all fruits.
    print(f"\nTotal size of all fruits after {num_days} days: {total_size}")

    # Print the number of fruits ready for harvesting.
    print(f"Number of fruits ready for harvesting (even size): {even_count}")


magical_fruit_garden()
