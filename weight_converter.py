# initiates the program.
while True:
    try:
        # Input weight
        weight = float(input('What is your weight? '))
        while True:
            # Input units
            units = input('Your weight is in Kilograms(kg) or in Pounds(lb)? ')
            if not units:
                print('Enter units.')
                continue
            # Converts weight in kg to pounds
            if units.lower() in ['k', 'kg', 'kgs', 'kilogram', 'kilograms']:
                converted_weight = 2.205 * weight
                print(f'Your weight in Pounds is: {converted_weight} lb(s)')
                break
            # Convert weight in pounds to kg
            elif units.lower() in ['l', 'lb', 'lbs', 'pound', 'pounds']:
                converted_weight = 0.454 * weight
                print(f'Your weight in Kilograms is {converted_weight} kg(s)')
                break
            else:
                print('Enter units correctly.')
                continue
        break

    except ValueError:
        print('Enter numeric value only.')

