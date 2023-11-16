import math


def main():

    body_fat_percentage_calculator(43.5, 18.5, 70.5)


def body_fat_percentage_calculator(waist_measurement, neck_measurement, height):
    # Ensure waist_measurement is greater than neck_measurement to avoid math domain error
    if waist_measurement <= neck_measurement:
        return "Waist measurement must be greater than neck measurement for a valid calculation."

    # Given measurements
    # waist_measurement = 25  # Waist circumference in inches
    # neck_measurement = 70.5  # Neck circumference in inches

    # % body fat = [86.010 x Log10 (waist – neck)] – [70.041 x Log10 (height)] + 36.76
    # Body fat percentage calculation for male using the given formula
    body_fat_percentage = (86.010 * math.log10(waist_measurement - neck_measurement)) - (70.041 * math.log10(height)) + 36.76
    print(f"Body fat percentage: {round(body_fat_percentage, 2)}%")
    return body_fat_percentage


if __name__ == "__main__":
    main()
