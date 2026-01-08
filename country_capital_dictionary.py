# -*- coding: utf-8 -*-
"""
Created on Dec  7 01:21:11 2020
@author: Khadija Bouadi
"""

# Existing dictionary
my_dict = {
    "Morocco": "Rabat",
    "Germany": "Berlin",
    "Singapore": "Singapore",
    "Canada": "Ottawa",
    "Egypt": "Cairo",
    "France": "Paris",
    "Italy": "Rome",
    "Japan": "Tokyo",
    "Spain": "Madrid"
}

while True:
    country_input = input("Enter a country (or 'exit' to end): ").strip()

    if country_input.lower() == 'exit':
        break  # Exit the loop

    # Case-insensitive search
    found = False
    for country, capital in my_dict.items():
        if country.lower() == country_input.lower():
            print(f"The capital of {country} is {capital}")
            found = True
            break

    if not found:
        print(f"Sorry, the capital of {country_input} is not available.")
        add_country = input(f"Do you want to add {country_input} to the dictionary? (yes/no): ").strip().lower()

        if add_country == 'yes':
            new_capital = input(f"Enter the capital of {country_input}: ").strip()
            my_dict[country_input] = new_capital
            print(f"{country_input} and its capital {new_capital} added to the dictionary.")
        else:
            print("Okay, not adding to the dictionary.")

# Display the final dictionary
print("Final Dictionary:")
print(my_dict)
