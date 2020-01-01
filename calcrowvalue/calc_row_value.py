
def calc_row_value(input_string):
    """
    1) adds the value of every odd digit multiplied by its position in the row
    2) subtract the value of every even digit multiplied by 5
    Other requirements include:
    a) It should make use of the enumerate() function.
    b) It should raise a ValueError when the input is not a string.
    ---
    input: a string of integers
    output: return an integer based on 1 and 2 above
    """

    try:
        int(input_string)
    except ValueError:
        print("Unrecognized characters in input string")
        raise

    dict_of_digits = {}
    value_of_input = 0
    for place, digit in enumerate(input_string):
        if digit.isdecimal():
            dict_of_digits[place+1] = int(digit)

    for placedict, values in dict_of_digits.items():
        if placedict % 2 == 0:
            value_of_input -= values * 5
        else:
            value_of_input += values * placedict
    return value_of_input

print(calc_row_value("7154226105g"))