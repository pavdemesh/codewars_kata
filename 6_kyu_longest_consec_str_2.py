# You are given an array(list) strarr of strings and an integer k.
# Your task is to return the first longest string
# consisting of k consecutive strings taken in the array.
# # Example:
# longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
# # n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

def longest_consec(strarr, k):
    res = ""
    n = len(strarr)

    if 0 < k <= n:
        for index in range(n - k + 1):
            s = "".join(word for word in strarr[index:index + k])
            if len(s) > len(res):
                res = s
    return res


print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))
