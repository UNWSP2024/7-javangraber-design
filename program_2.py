# Programmer: Javan Graber
# Date: 3/5/2026
# Program #2: Larger than n
# In a program, write a function (with NO output) that accepts two arguments: number n, and a list.
# Assume that the list contains numbers.
# The function shell has been written out on line 30, (def display_larger_than_n_list)
# and should display all the numbers in the list that are greater than then number n.

def main():
    # Declare local variables
    number = 5
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Display the number.
    print('Number:', number)

    # Display the list of numbers.
    print('List of numbers:')
    print(f'{number_list}')

    # Display the list of numbers that are larger
    # than the number.
    print(f'List of numbers that are larger than {number}:')
    # Call the display_larger_than_n_list function,
    # passing a number and number list as arguments.
    larger_numbers = display_larger_than_n_list(number, number_list)
    print(f'{larger_numbers}')


# The display_larger_than_n_list function accepts two arguments:
# a list, and a number. The function displays all the numbers
# in the list that are greater than the number.
def display_larger_than_n_list(n, number_list):
    # Write your code to display all the numbers in the list that are greater than then number n. below
    # Create the original larger list
    larger_than_n_list = []

    # Create the loop
    for number in number_list:
        if number > n:
            larger_than_n_list.append(number)
        else:
            larger_than_n_list = larger_than_n_list
    return larger_than_n_list

# Call the main function.
if __name__ == '__main__':
    main()
