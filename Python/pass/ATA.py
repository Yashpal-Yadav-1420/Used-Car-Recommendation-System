"""def magical_fruit_garden():
    # Get the number of days from the user
    days = int(input("Enter the number of days you want to grow the fruits: "))

    # Initialize fruit sizes list
    fruit_sizes = []

    for day in range(1, days + 1):
        # Ask user if they watered the fruits
        watered = input(f"Did you water the fruits on day {day}? (yes/no): ")

        # Determine the size of each fruit
        fruit_size = day
        print("fruit_size=",fruit_size) """# Print the value of 'fr

# Calculate total size of all fruits
"""   total_size = sum(fruit_sizes)


    # Count the number of fruits ready for harvesting (even-sized fruits)
    harvest_count = sum(1 for size in fruit_sizes if size % 2 == 0)

    # Display the results
    print("\nResults:")
    print("fruit_sizes=",fruit_sizes)
    print("Total size of all fruits:",total_size)
    print("Number of fruits ready for harvesting:",harvest_count)

# Run the program
magical_fruit_garden()"""

def magical_fruit_garden():
    # Get the number from days from user
    days = int(input("Enter the number days you want to grow the fruit: "))

    #Initialize fruit sizez list
    fruit_sizes = []

    for days in range(1, days + 1):
        #Ask user if they watered the fruits
        watered = input(f"Did you water the fruit on day {days}? (Yes/No): ")

        #Determine the size of each size
        fruit_size = days
        print("fruit_size=", fruit_size)
        if watered == "yes":
            fruit_size *= 2

        fruit_sizes.append(fruit_size)
        print("fruit_sizes=", fruit_sizes)

        total_size = sum(fruit_sizes)

        harvest_count = sum(1 for size in fruit_sizes if size % 2 == 0)

        print("/Results:")
        print("fruit_sizes=", fruit_sizes)
        print("Total size of all fruits: ", total_size)
        print("Number of fruits ready for harvesting: ", harvest_count)

magical_fruit_garden()