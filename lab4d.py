#!/usr/bin/env python3

# Strings 1



str1 = 'Hello World!!'

str2 = 'Seneca College'



num1 = 1500

num2 = 1.50



def first_five(input_str):

    """Return the first five characters of the input string."""

    return input_str[:5]



def last_seven(input_str):

    """Return the last seven characters of the input string."""

    return input_str[-7:]



def middle_number(input_num):

    """Return the second and third characters of the string representation of the number."""

    return str(input_num)[1:3]



def first_three_last_three(str1, str2):

    """Return a string starting with the first three characters of str1 and ending with the last three characters of str2."""

    return str1[:3] + str2[-3:]



if __name__ == '__main__':

    print(first_five(str1))

    print(first_five(str2))

    print(last_seven(str1))

    print(last_seven(str2))

    print(middle_number(num1))

    print(middle_number(num2))

    print(first_three_last_three(str1, str2))

    print(first_three_last_three(str2, str1))

