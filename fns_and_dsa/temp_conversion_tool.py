# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 # F to C
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5 # C to F

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.
    
    Parameters:
    fahrenheit (float): Temperature in Fahrenheit.
    
    Returns:
    float: Temperature in Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.
    
    Parameters:
    celsius (float): Temperature in Celsius.
    
    Returns:
    float: Temperature in Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """
    Main function to run the temperature conversion tool.
    Asks the user to enter a temperature, current unit and conversion type,
    then displays the converted temperature.
    """
    try:
        # Ask the user to enter a temperature
        temperature = float(input("Enter the temperature: "))
        # Ask the user to specify the unit of the temperature
        unit = input("Is this in Celsius or Fahrenheit? (C/F): ").upper()
        
        # Check if the unit is valid and perform the conversion
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature} degrees Celsius is equal to {converted_temp:.2f} degrees Fahrenheit.")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature} degrees Fahrenheit is equal to {converted_temp:.2f} degrees Celsius.")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()