import math


def main():
    # Example usage
    print("Welcome to the Body Fat Percentage Calculator!")
    print(
        "Type 'help' (h) for sample calculations, 'calculate' (c) to proceed, "
        "or 'exit' (e) to exit the program."
    )

    while True:
        user_input = (
            input("Please enter a command (help (h), " "calculate (c), exit (e)): ")
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

    # # Example usage
    # women_body_fat = body_fat_percentage_women(15, 42, 44, 64)  # Example given for women
    # men_body_fat = body_fat_percentage_men(16, 49, 69)          # Example given for men

    # women_body_fat
    # men_body_fat


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
    # Print the sample information for help
    print("\nSample body fat calculations:\n")
    print("SAMPLE (WOMEN)")
    print(
        "Measurements: Neck = 15 inches; Waist = 40 inches; Hip = 40 inches; Height = 64 inches\n"
    )
    print("SAMPLE (MEN)")
    print("Measurements: Neck = 15 inches; Waist = 40 inches; Height = 69 inches\n")


if __name__ == "__main__":
    main()
