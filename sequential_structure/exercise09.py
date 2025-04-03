"""
Author: Francisco Junior
Date: 03/04/2025 - Brazil format
Description: Converter temperature Fahrenheit for Celsius
"""

temperature_fahrenheit = int(input("Fahrenheit: "))
converter_temperature = 5 * (temperature_fahrenheit - 32) / 9.0
print(
    "The temperature converted F° %.1f -> C° %.1f "
    % (
        temperature_fahrenheit,
        converter_temperature,
    )
)
