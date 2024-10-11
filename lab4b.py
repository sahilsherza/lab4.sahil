#!/usr/bin/env python3

def join_lists(l1, l2):
    # Convert lists to sets, perform union, then convert back to list
    return list(set(l1).union(set(l2)))  # Same as using | operator on sets

def match_lists(l1, l2):
    # Convert lists to sets, perform intersection, then convert back to list
    return list(set(l1).intersection(set(l2)))  # Same as using & operator on sets

def diff_lists(l1, l2):
    # Convert lists to sets, perform symmetric difference, then convert back to list
    return list(set(l1).symmetric_difference(set(l2)))  # Same as using ^ operator on sets

if __name__ == '__main__':
    list1 = list(range(1, 10))  # list1: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list2 = list(range(5, 15))  # list2: [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))  # Should return a list with all unique values
    print('match: ', match_lists(list1, list2))  # Should return a list with common values
    
