"""
CP1404/CP5632 - Practical
Convert temperatures between files
"""
import random


def main():
    """
    Convert input file of one temperature unit to output file of another unit.
    """
    number_temps = int(input("Number of temperatures: "))
    while number_temps < 15:
        print("Number of temps must be greater than or equal to 15")
        number_temps = int(input("Number of temperatures: "))
    create_input_file(number_temps)
    create_output_file()


def create_input_file(number_temps):
    """
    Write temperatures to file.
    """
    file = open("temps_input.txt", "w")
    for i in range(number_temps):
        temp = random.uniform(-200, 200)
        file.write(f"{temp}\n")
    file.close()
    return file


def create_output_file():
    """
    Read the values in temps_input.txt as Fahrenheit values and write the converted Celsius values
    to temps_output.txt
    """
    input_file = open("temps_input.txt", "r")
    output_file = open("temps_output.txt", "w")
    for line in input_file:
        celsius = convert_fahrenheit_to_celsius(float(line))
        output_file.write(f"{celsius}\n")
    output_file.close()
    input_file.close()
    return output_file


def convert_fahrenheit_to_celsius(fahrenheit):
    """
    Convert fahrenheit to celsius.
    """
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
