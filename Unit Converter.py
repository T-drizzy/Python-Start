import time

while True:
    #Intro 
    print()
    print("** UNIT CONVERTER **")
    print()

    conversions_available = [(1, 'km', 'mi'),
                        (2, 'mi', 'km'),
                        (3, 'kg', 'lbs'),
                        (4, 'lbs', 'kg'),
                        (5, '°F', '°C'),
                        (6, '°C', '°F'),
                        (7, 'L', 'gal(US)'),
                        (8, 'gal(US)', 'L'),
                        (9, 'cm', 'inch'),
                        (10, 'inch', 'cm')]

    print ("Conversions available:")
    print()

    #Printing options
    for conversion_number, from_unit, to_unit in conversions_available:
        print(f'{conversion_number} {from_unit} -> {to_unit}')

    print()

    #Checking if input valid
    while True:
        try:
            conversion = int(input("Enter the number of the conversion to use: "))
            if 1 <= conversion <= 10:
                print("Please wait...")
                time.sleep(1)
                break
            else:
                print("Invalid input. Please enter a whole number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a whole number between 1 and 10.")

    #Converting user input into float, so conversion can be done precisely
    conversion_index = int(conversion)-1

    conversion_number, from_unit, to_unit = conversions_available[conversion_index]
    print()
    from_value = float(input(f'Enter {from_unit}: '))
    print()

    # Conversion: km to mi
    if conversion_number == 1:
        to_value = from_value * 0.609344
        print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

    # Conversion: mi to km
    elif conversion_number == 2:
        to_value = from_value * 1.609344
        print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

    # Conversion: kg to lbs
    elif conversion_number == 3:
        to_value = from_value * 2.20462262
        print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

    # Conversion: lbs to kg
    elif conversion_number == 4:
        to_value = from_value * 0.45359
        print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

    # Conversion: °F to °C
    elif conversion_number == 5:
        to_value = (from_value-32)*0.5556
        print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

    # Conversion: °C to °F
    elif conversion_number == 6:
        to_value = (from_value*1.8)+32
        print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

    # Conversion: L to gal(US)
    elif conversion_number == 7:
        to_value = from_value*0.264172
        print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

    # Conversion: gal(US) to L
    elif conversion_number == 8:
        to_value = from_value/0.264172
        print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

    # Conversion: cm to inch
    elif conversion_number == 9:
        to_value = from_value/2.54
        print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

    # Conversion: inch to cm
    elif conversion_number == 10:
        to_value = from_value*2.54
        print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

    rerun = input("Do you want to convert another value? (yes/no): ")

    if rerun.lower() != 'yes':
        break