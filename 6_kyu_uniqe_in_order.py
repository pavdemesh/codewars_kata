# https://www.codewars.com/kata/54e6533c92449cc251001667

# Implement the function unique_in_order which takes as argument a sequence and returns a list of items
# without any elements with the same value next to each other and preserving the original order of elements.
# For example:
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]


def unique_in_order(iterable):
    # If empty: return empty list
    if not iterable:
        return []

    # If one element - return this one element
    if len(iterable) == 1:
        return list(iterable)

    # Convert iterable into a list
    iter_list = list(iterable)
    # Create a list called unique and add first element of the iterable to it (index [0])
    unique = [iter_list[0]]

    # Iterate through the iterable list using indexes from 0 to len - 1
    for i in range(len(iter_list) - 1):
        # If current element is not equal to the next element
        # Add this next element to the unique list via append
        if iter_list[i] != iter_list[i + 1]:
            unique.append(iter_list[i + 1])
    return unique


print(unique_in_order([1, 2, 3, 3]))
