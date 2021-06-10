#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: June 2021
# This program rotates the values in a list


def rotate_list(list_of_values, rotations):
    # This function rotates the list

    rotated_list = []

    for values in range(rotations, len(list_of_values)):
        rotated_list.append(list_of_values[values])
    for values in range(0, rotations):
        rotated_list.append(list_of_values[values])

    return rotated_list


def main():
    # This function gets the list values

    inputList = []

    # Input & Process
    print("This program rotates the values in a list.")
    print("")
    print("Enter one list value at a time and -1 to end.")
    while True:
        value_input = input("Enter a list value: ")

        if value_input == "-1":
            break
        else:
            inputList.append(value_input)
    rotation_number_string = input("Enter the number of positions that "
                                   "you want the list rotated: ")
    while True:
        try:
            rotation_number_integer = int(rotation_number_string)

            if rotation_number_integer >= 0:
                break
            else:
                rotation_number_string = input("Must be a positive integer "
                                               "Enter the number of positions "
                                               "that you want the list "
                                               "rotated: ")
        except Exception:
            rotation_number_string = input("{} is not a valid input. "
                                           "Enter the number of positions "
                                           "that you want the list rotated: ".
                                           format(rotation_number_string))

    # Call functions
    new_list = rotate_list(inputList, rotation_number_integer)

    # Output
    print("")
    print("The list {0} rotated {1} places is: {2}".
          format(inputList, rotation_number_integer, new_list))
    print("\nDone.")


if __name__ == "__main__":
    main()
