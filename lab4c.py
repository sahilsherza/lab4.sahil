#!/usr/bin/env python3



# Dictionaries

dict_york = {

    'Address': '70 The Pond Rd',

    'City': 'Toronto',

    'Country': 'Canada',

    'Postal Code': 'M3J3M6',

    'Province': 'ON'

}

dict_newnham = {

    'Address': '1750 Finch Ave E',

    'City': 'Toronto',

    'Country': 'Canada',

    'Postal Code': 'M2J2X5',

    'Province': 'ON'

}



# Lists

list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']

list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']



def create_dictionary(keys, values):

    """Create a dictionary from two lists: keys and values."""

    new_dict = {}

    index = 0

    while index < len(keys):

        new_dict[keys[index]] = values[index]

        index += 1

    return new_dict



def shared_values(dict1, dict2):

    """Return a set of shared values between two dictionaries."""

    set1 = set(dict1.values())

    set2 = set(dict2.values())

    return set1.intersection(set2)



if __name__ == '__main__':

    # Create dictionary from keys and values

    york = create_dictionary(list_keys, list_values)

    print('York: ', york)

    # Find shared values between two dictionaries

    common = shared_values(dict_york, dict_newnham)

    print('Shared Values', common)
