"""
Body Fat Percentage Calculator based on Army Regulation 600-9 (2019)

This script calculates the body fat percentage for both men and women based on the guidelines
outlined in the U.S. Army Regulation 600-9. It prompts users for their measurements including
neck, waist, and hip circumferences (hip only for women), and height, to calculate and output
their body fat percentage. 

The script supports interactive use where the user can choose to either get help information,
perform a calculation, or exit the program.

Functions:
    main() - The main function to run the Body Fat Percentage Calculator.
    body_fat_percentage_women(neck_measurement, waist_measurement, hip_measurement, height) - Calculates body fat percentage for women.
    body_fat_percentage_men(neck_measurement, waist_measurement, height) - Calculates body fat percentage for men.
    print_help_info() - Prints sample calculations and formulae.

Example:
    To run the calculator, execute this script and follow the interactive prompts.

Note:
    This script uses the formulae provided in AR 600-9 (2019), Table B-5 for calculations. 
    It's intended for informational purposes and should not replace professional medical advice.

Copyright (C) 2023 https://github.com/jvossler

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import math


def main():
    """
    The main function to run the Body Fat Percentage Calculator.

    This function prompts the user to either get help information, calculate their body
    fat percentage, or exit the program. It handles user input and guides them through
    the process of entering the necessary measurements for calculating body fat percentage.
    """

    # Example usage
    print("Welcome to the Body Fat Percentage Calculator!")
    print(
        "Type 'help' (h) for sample calculations, 'calculate' (c) to proceed, "
        "or 'exit' (e) to exit the program."
    )

    while True:
        user_input = (
            input("Please enter a command (help (h), calculate (c), exit (e)): ")
            .strip()
            .lower()
        )
        if user_input == "help" or user_input == "h":
            print_help_info()
        elif user_input == "calculate" or user_input == "c":
            gender = (
                input("Please enter your gender (man (m)) OR (woman (w)): ")
                .strip()
                .lower()
            )
            if gender == "woman" or gender == "w":
                neck = float(input("Enter neck measurement in inches: "))
                waist = float(input("Enter waist measurement in inches: "))
                hip = float(input("Enter hip measurement in inches: "))
                height = float(input("Enter height in inches: "))
                women_body_fat = body_fat_percentage_women(neck, waist, hip, height)
                print(f"Body fat percentage for women: {women_body_fat}%")
            elif gender == "man" or gender == "m":
                neck = float(input("Enter neck measurement in inches: "))
                waist = float(input("Enter waist measurement in inches: "))
                height = float(input("Enter height in inches: "))
                men_body_fat = body_fat_percentage_men(neck, waist, height)
                print(f"Body fat percentage for men: {men_body_fat}%")
            else:
                print("Invalid gender entered.")
        elif user_input == "exit" or user_input == "e":
            break
        else:
            print("Invalid command entered.")


# Function for calculating body fat percentage for women
def body_fat_percentage_women(
    neck_measurement, waist_measurement, hip_measurement, height
):
    """
    Calculate the body fat percentage for women using specified measurements.

    Args:
        neck_measurement (float): The neck circumference in inches.
        waist_measurement (float): The waist circumference in inches.
        hip_measurement (float): The hip circumference in inches.
        height (float): The height in inches.

    Returns:
        float: The estimated body fat percentage.
    """
    # Ensure that the log argument is positive to avoid math domain error
    if waist_measurement + hip_measurement <= neck_measurement:
        return (
            "Error: Waist plus hip measurement must be greater than neck measurement."
        )

    # % body fat (women) = [163.205 × log10 (waist + hip − neck)] − [97.684 × log10 (height)] − 78.387
    # Calculate the body fat percentage using the given formula for women
    body_fat_percentage = (
        (163.205 * math.log10(waist_measurement + hip_measurement - neck_measurement))
        - (97.684 * math.log10(height))
        - 78.387
    )
    # print(round(body_fat_percentage, 2))
    return round(body_fat_percentage, 2)


# Function for calculating body fat percentage for men
def body_fat_percentage_men(neck_measurement, waist_measurement, height):
    """
    Calculate the body fat percentage for men using specified measurements.

    Args:
        neck_measurement (float): The neck circumference in inches.
        waist_measurement (float): The waist circumference in inches.
        height (float): The height in inches.

    Returns:
        float: The estimated body fat percentage.
    """
    # Ensure that the log argument is positive to avoid math domain error
    if waist_measurement <= neck_measurement:
        return "Error: Waist measurement must be greater than neck measurement."

    # % body fat (men) = [86.010 × log10 (waist − neck)] − [70.041 × log10 (height)] + 36.76
    # Calculate the body fat percentage using the given formula for men
    body_fat_percentage = (
        (86.010 * math.log10(waist_measurement - neck_measurement))
        - (70.041 * math.log10(height))
        + 36.76
    )
    # print(round(body_fat_percentage, 2))
    return round(body_fat_percentage, 2)


def print_help_info():
    """
    Prints sample calculations and formulae for calculating body fat percentage.

    This function provides users with example measurements and the formulae used
    for calculating body fat percentage for both men and women. It is intended to
    help users understand how the measurements affect the calculation and provide
    a reference for the input format.
    """

    # Print the sample information for help
    print("\nSample body fat calculations (Ref: AR 600-9, Table B-5):\n")
    print("SAMPLE (WOMEN)")
    print(
        "Equation for women is:\n"
        "% body fat (women) = [163.205 × log10 (waist + hip − neck)] − [97.684 × log10 (height)] − 78.387\n"
    )
    print(
        "Example Measurements:\n"
        "Neck = 15 inches\n"
        "Waist = 40 inches\n"
        "Hip = 40 inches\n"
        "Height = 64 inches\n\n"
    )
    print("SAMPLE (MEN)")
    print(
        "Equation for men is:\n"
        "% body fat (men) = [86.010 × log10 (waist − neck)] − [70.041 × log10 (height)] + 36.76\n"
    )
    print(
        "Example Measurements:\n"
        "Neck = 15 inches\n"
        "Waist = 40 inches\n"
        "Height = 69 inches\n\n"
    )

    print(
        "References:\n"
        "United States Army. (2019). Army Regulation 600-9: The Army Body Composition Program. Retrieved from:\n"
        "https://armypubs.army.mil/ProductMaps/PubForm/Details.aspx?PUB_ID=1004922"
        "\n"
    )


if __name__ == "__main__":
    main()
