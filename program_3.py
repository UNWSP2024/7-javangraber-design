# Programmer: Javan Graber
# Date: 3/5/2026
# Program #3: US_Population
# Have the user input (using a loop) various information that contains three pieces of data:
# year, name of state, and population.
# Store all of this information in a list of lists.  For example, it might be stored like this:

# [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa",3421988]]
# Now have the user enter a year.
# The program will add the populations from all states in the list of list for that year only.
# Pass the list and year to the sum_population_for_year


# Create the main function
def main():

    # Create the main list
    all_entered_values = []

    # Change the all entered values list by calling for the find list values function
    all_entered_values = find_list_values(all_entered_values)

    # Have the user enter the year for the population count
    year_to_sum = int(input("Enter the year for the population count: "))

    # Get the total population count from sum population function
    total_population = sum_population_for_year(all_entered_values, year_to_sum)

    # Print the total population
    print(f"The total population for {year_to_sum} is {total_population:,}")



# Create a function that finds the values for the lists
def find_list_values(all_entered_values):

    # Create a variable to control the loop
    again = 'y'

    # Keep track of the loops
    total_loops = 0

    # Create a loop that makes the lists that will be in the all entered values list
    while again == 'y' or again == 'Y':

        # Create the first internal list
        internal_list = []

        # Ask for the year
        year = int(input('Enter the year: '))

        # Add the year to the list
        internal_list.append(year)

        # Ask for the state
        state = str(input('Enter the state: '))

        # Add the state to the list
        internal_list.append(state)

        # Ask for the population
        population = int(input('Enter the population: '))

        # Add the population to the list
        internal_list.append(population)

        # Add the internal list to the all entered values list
        all_entered_values.append(internal_list)

        # Identify the loop and keep track of it
        total_loops += 1

        # Ask if they want to add another list
        again = str(input('Add another group (enter "y" for yes or enter "n" for no): '))

    # Return the new list
    return all_entered_values


def sum_population_for_year(all_entered_values, year_to_sum):

    total_population = 0

    for row in all_entered_values:

        # Determine if the row contains the year selected
        if row[0] == year_to_sum:

            # If it does, add the population element to the total
            total_population += row[2]

    # Return the total population
    return total_population


# Call the main function.
if __name__ == '__main__':
    main()
