# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:23:33 2025

@author: gabri
"""

def calculate_bmi(weight_lb: float, height_in: float) -> float:
    """
    Calculate BMI using weight in pounds and height in inches.
    """
    weight_kg = weight_lb * 0.45359237
    height_m = height_in * 0.0254

    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must be greater than zero.")

    return round(weight_kg / (height_m ** 2), 2)


def main() -> None:
    weight_lb = float(input("Enter your weight in pounds: "))
    height_in = float(input("Enter your height in inches: "))

    bmi = calculate_bmi(weight_lb, height_in)

    print(f"BMI: {bmi}")


if __name__ == "__main__":
    main()