"""
This is a simple Roman Numerals convertor
"""
roman_number = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M',
    'vinculum': '\u0305' # The vinculum (horizontal bar over a letter)
}

def get_roman(value):
    """
    Recursive function to get the roman numerial string.
    """
    key = 1
    temp_value = value
    while (temp_value // 10) > 0:
        key = key * 10
        temp_value = temp_value // 10

    digit = value // key
    string = ""
    if (key > 1000) or (key == 1000 and digit > 3):
        if digit == 9:
            string = roman_number[key/1000] + roman_number['vinculum']
            string +=(roman_number[key/1000 * 10] + roman_number['vinculum'])
        elif digit >= 5:
            string +=(roman_number[key/1000 * 5] + roman_number['vinculum'])
            string +=((roman_number[key/1000] + roman_number['vinculum']) * (digit - 5))
        elif digit == 4:
            string +=(roman_number[key/1000] + roman_number['vinculum'])
            string +=(roman_number[key/1000 * 5] + roman_number['vinculum'])
        else:
            string +=((roman_number[key/1000] + roman_number['vinculum']) * digit)
    else:
        if digit == 9:
            string +=(roman_number[key])
            string +=(roman_number[key * 10])
        elif digit >= 5:
            string +=(roman_number[key * 5])
            string +=(roman_number[key] * (digit - 5))
        elif digit == 4:
            string +=(roman_number[key])
            string +=(roman_number[key * 5])
        else:
            string +=(roman_number[key] * digit)

    if value < 10:
        return string

    return string + get_roman(value - (digit * key))

# Main function to ask for user input of a number between 1 and 1000000
if __name__ == '__main__':
    while True:
        try:
            number = int(input("Please enter a number between 1 and 1000000 (-1 to end): "))
            if 0 < number < 1000001:
                roman = get_roman(number)
                print(f"The Roman numerals of {number} is {roman}")
            elif number == -1:
                break
            else:
                print("Number must be between 1 and 1000000 (-1 to end).")
        except ValueError:
            print("Invalid input.")
