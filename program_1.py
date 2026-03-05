# Programmer: Javan Graber
# Date: 3/5/2026
# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year,
# the average monthly rainfall, # and the months with the highest and lowest amounts.



# Create the main function that will call all the functions and display the information
def main():

    # Get the rainfall list from the rainfall list function
    rainfall_list = create_rainfall_list()

    # Get the total rainfall from the total rainfall function
    total_rainfall = find_total_rainfall(rainfall_list)

    # Display the total rainfall
    print(f"The total rainfall was {total_rainfall:.2f} inches")

    # Get the average rainfall from the average rainfall function
    average_rainfall = find_average_rainfall(rainfall_list, total_rainfall)

    # Display the average rainfall
    print(f"The average rainfall was {average_rainfall:.2f} inches")

    # Get the highest rainfall and lowest rainfall with their months from
    # the rainfall months function
    lowest_rainfall, highest_rainfall, high_rainfall_month, low_rainfall_month = find_rainfall_months(
        rainfall_list,
    )

    # Print the highest month
    print(f"Month {high_rainfall_month} had the highest rainfall with {highest_rainfall} inches")

    # Print the lowest month
    print(f"Month {low_rainfall_month} had the highest rainfall with {lowest_rainfall} inches")



# Create a function that makes the list from the values given by the user
def create_rainfall_list():

    # Create an empty list
    rainfall_list = []

    # Create a constant to display the month we are asking for
    month_order = 1

    # Ask for the rainfall for each of the 12 months and add it to a list
    for number in range(12):

        # Ask for the total rainfall for the month
        month_rainfall = float(input(f"Enter the total rainfall for month {month_order} in inches: "))

        # Add this value to the list
        rainfall_list.append(month_rainfall)

        # Move to the next month
        month_order += 1

    return rainfall_list



# Create a function that finds the total rainfall
def find_total_rainfall(rainfall_list):

    # Create an accumulator variable
    total_rainfall = 0

    # Create a loop that adds the elements in the list
    for rainfall in rainfall_list:
        total_rainfall += rainfall

    # Return the total_rainfall
    return total_rainfall



# Create a function that finds the average rainfall
def find_average_rainfall(rainfall_list, total_rainfall):

    # Divide the total rainfall by the length of the rainfall list values to find the average
    average_rainfall = total_rainfall / len(rainfall_list)

    # Return the average rainfall
    return average_rainfall



# Create a list that finds the highest and lowest amounts of rainfall in the rainfall list
def find_rainfall_months(rainfall_list):

    # Find the lowest amount of rainfall in the rainfall list
    lowest_rainfall = min(rainfall_list)

    # Find the index of the lowest amount of rainfall
    small_rainfall_index = rainfall_list.index(lowest_rainfall)

    # Find the month with the low rainfall amount from the index
    low_rainfall_month = small_rainfall_index + 1

    # Find the highest amount of rainfall in the rainfall list
    highest_rainfall = max(rainfall_list)

    # Find the index of the highest amount of rainfall
    high_rainfall_index = rainfall_list.index(highest_rainfall)

    # Find the month with the high rainfall amount from the index
    high_rainfall_month = high_rainfall_index + 1

    # Return the lowest and highest rainfall amounts
    return lowest_rainfall, highest_rainfall, high_rainfall_month, low_rainfall_month

# Call for main function
if __name__ == '__main__':
    main()
