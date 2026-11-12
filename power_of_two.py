#!/usr/bin/env python3
# Created By: Victor Victor-Calixte
# Date: 09/16/26
# This program calculates the power of the given numbers from the user

import constants


def main():

    # Getting the inputs from the user
    base_str = input(constants.BASE_MSG)
    expo_str = input(constants.EXPO_MSG)

    # the try statement will make sure the code safely with invalid user inputs
    try:
        # Converting both inputs to integers
        base = int(base_str)
        expo = int(expo_str)

        # Checking if the numbers are invalid
        if base < 0 or expo < 0:
            print(constants.ERR_MSG.format(base_str, expo_str))
        else:
            # Setting the sum
            sum_num = 1

            # Calculating the sum starting the counter at 0
            for counter in range(0, expo):

                sum_num *= base

            # Displaying the sum to the user
            print(constants.ANSWER_MSG.format(base, expo, sum_num))

    except:
        print(constants.ERR_MSG.format(base_str, expo_str))


if __name__ == "__main__":
    main()
