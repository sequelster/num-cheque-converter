# Numbers to consider when designing this:
# 10, 3, 500, 1008, 13452, 400850, 18234567
def convert_int(integer):
    # Converting to a string because strings are arrays in Python
    # thus I can pull individual numbers as part of the overall value
    str_int = str(integer)
    total_digits = len(str_int)
    ones = {
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen'}
    tens = {
        '2': 'twenty',
        '3': 'thirty',
        '4': 'forty',
        '5': 'fifty',
        '6': 'sixty',
        '7': 'seventy',
        '8': 'eighty',
        '9': 'ninety'
        }


    # Now the tediousness begins!
    if integer < 20:
        final_string = ones.get(str_int)

    if integer > 20 and integer < 100:
        first_digit = tens.get(str_int[0])
        second_digit = ones.get(str_int[1])
        final_string = '{} {}'.format(first_digit, second_digit)

    if total_digits == 3:
        first_digit = ones.get(str_int[0])
        final_string = '{} hundred'.format(first_digit)
        if str_int[1] != '0':
            second_digit = tens.get(str_int[1])
            final_string = '{} {}'.format(final_string, second_digit)
        if str_int[2] != '0':
            third_digit = ones.get(str_int[2])
            final_string = '{} {}'.format(final_string, third_digit)

    if total_digits == 4:
        first_digit = ones.get(str_int[0])
        final_string = '{} thousand'.format(first_digit)
        if str_int[1] !='0':
            second_digit = ones.get(str_int[1])
            final_string = '{} {} hundred'.format(final_string, second_digit)
        if str_int[2] !='0':
            third_digit = tens.get(str_int[2])
            final_string = '{} {}'.format(final_string, third_digit)
        if str_int[3] !='0':
            fourth_digit = ones.get(str_int[3])
            final_string = '{} {}'.format(final_string, fourth_digit)

    print(final_string)
    
        

convert_int(3)
convert_int(32)
convert_int(421)
convert_int(5946)