# In which I remember Modulus ? Modulo? Percenty things exist

def convert_int(num):
     # Converting to a string because strings are arrays in Python
    # thus I can pull individual numbers as part of the overall value
    numlength = len(str(num))
    ones = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'}
    tens = {
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety'
        } 
    numword = ''
    ones_place = num % 10
    tens_place = (( num % 100) - ones_place) / 10
    hundreds_place = (( num % 1000 ) - (tens_place * 10) - ones_place) / 100
    if num <= 0:
        numword = 'I do not support this. Please use a positive number above 0.'
    elif numlength > 6:
        numword = 'I do not have this kind of money. (really I just ran out of time implementing million+)'
    elif num > 0 and num < 20:
        numword = ones.get(num)
    
    # Tens
    if tens_place >= 2:
        tens_word = ('{}-{}'.format(tens.get(tens_place), ones.get(ones_place)))
    elif tens_place == 1:
        tens_word = '%s' % ones.get(num % 100)
    elif tens_place < 1 and ones_place != 0:
        tens_word = '%s' % ones.get(ones_place)
    else:
        tens_word = ''
    
    if hundreds_place > 0:
        hund_word = ('%s hundred ' % ones.get(hundreds_place))
    else:
        hund_word = ''

    # now to deal with the thousands:
    thou_place = int(num % 1000000 / 1000)
    str_num = str(thou_place)
    if thou_place >= 1 and thou_place < 20:
        thou_word = '%s thousand ' % ones.get(thou_place)
    elif thou_place >= 20 and thou_place < 100:
        if str_num[1] != '0':
            thou_word = '{}-{} thousand '.format(
                                            tens.get(int(str_num[0])),
                                            ones.get(int(str_num[1])))
        else:
            thou_word = '%s thousand ' % tens.get(int(str_num[0]))
    elif thou_place >= 100:
        if str_num[2] != '0' and int(str_num[1]) < 2:
            thou_word = '{} hundred {} thousand '.format(
                                                    ones.get(int(str_num[0])),
                                                    ones.get(int(str_num[2])))
        elif str_num[2] != '0' and int(str_num[1]) >= 2:
            thou_word = '{} hundred {}-{} thousand '.format(
                                                       ones.get(int(str_num[0])),
                                                       tens.get(int(str_num[1])),
                                                       ones.get(int(str_num[2])))
        elif str_num[2] == '0' and int(str_num[1]) >= 2:
            thou_word = '{} hundred {} thousand '.format(
                                                    ones.get(int(str_num[0])),
                                                    tens.get(int(str_num[1])))
        elif str_num[2] == '0' and str_num[1] == '0':
            thou_word = '%s hundred thousand ' % ones.get(int(str_num[0]))
    else:
        thou_word = ''

    if numword == '':
        numword = '{}{}{}'.format(thou_word, hund_word, tens_word)

    print(numword)

convert_int(100003)
convert_int(300)
convert_int(12008)
