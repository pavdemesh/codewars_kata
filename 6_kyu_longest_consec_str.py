# You are given an array(list) strarr of strings and an integer k.
# Your task is to return the first longest string
# consisting of k consecutive strings taken in the array.
# # Example:
# longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
# # n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

def longest_consec(strarr, k):
    # Declare n to store length of the array
    n = len(strarr)
    # Basic check if empty array or k too big or too small
    if n == 0 or k > n or k <= 0:
        return ""

    # Variable to store the starting point of the longest sequence
    longest_start = 0
    # Variable to store maximum length of the string (will be int)
    max_length = None

    # Iterate over the array, stopping at item [n - k]
    # +1 is needed to include the (n-k)th item

    # Enumerate is not optimal since I do not use value
    # I could be  happy with index and range(len-k+1)
    for pos, value in enumerate(strarr[:n - k + 1]):
        # calculate the len of the string at each starting point
        length = sum(len(x) for x in strarr[pos:pos + k])

        # If current len is greater than the maximal len
        # Assign new longest_start position and new maximal length
        if max_length is None or length > max_length:
            longest_start = pos
            max_length = length

    # Return joined items starting from longest_start and including k items
    return "".join(x for x in strarr[longest_start:longest_start + k])


print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))
