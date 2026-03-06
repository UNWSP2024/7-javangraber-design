# Programmer: Javan Graber
# Date: 3/5/2026
# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input)
# and will return (as output) the distance between those points in space.
# The 3-dimensional coordinates must be stored as tuples.

# Now write a mainline that has the user enter the two tuples.
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)

# Import the math function
import math

# Create the function that makes the lists and tuples
def create_lists_tuples():

    # Create two original lists
    list1 = []
    list2 = []

    # Ask for the 3-dimensional values for both groups
    try:
        # Get the first value for the first group
        first_value = int(input("Enter the value for x in the first coordinate group: "))
        list1.append(first_value)

        # Get the second value for the first group
        second_value = int(input("Enter the value for y in the first coordinate group: "))
        list1.append(second_value)

        # Get the third value for the first group
        third_value = int(input("Enter the value for z in the first coordinate group: "))
        list1.append(third_value)

        # Get the first value for the second group
        first_value2 = int(input("Enter the value for x in the second coordinate group: "))
        list2.append(first_value2)

        # Get the second value for the second group
        second_value2 = int(input("Enter the value for y in the second coordinate group: "))
        list2.append(second_value2)

        # Get the third value for the second group
        third_value2 = int(input("Enter the value for z in the second coordinate group: "))
        list2.append(third_value2)

        # Turn these lists into tuples
        tuple1 = tuple(list1)
        tuple2 = tuple(list2)

        return (first_value, second_value, third_value, first_value2,
                second_value2, third_value2, tuple1, tuple2)

    except ValueError:
        # Print an error message
        print('Sorry, you have entered an invalid input. Please try again.')

# Create a function that calculates the distance by the formula
def perform_calculation(first_value, second_value, third_value, first_value2, second_value2, third_value2):

    # Knowing our formula sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2), we insert our values
    # to find the distance
    distance = math.sqrt((first_value2 - first_value)**2 +(second_value2 - second_value)**2 +
                         (third_value - third_value2)**2)
    return distance

# Create the main function
def main():

    # Get the tuples and values from the tuple function
    first_value, second_value, third_value, first_value2, second_value2, third_value2, tuple1, tuple2 = (
        create_lists_tuples())

    # Get the distance for the tuples from the calculations function
    distance = perform_calculation(first_value, second_value, third_value,
                                   first_value2, second_value2, third_value2)

    # Print the results
    print(f"The distance between {tuple1} and {tuple2} is {distance:.2f}")



# Call the main function.
if __name__ == '__main__':
    main()
