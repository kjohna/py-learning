# determine if a string of any unicode char is anagram, case sensitive
# change strings to lowercase for simple anagram testing

def is_anagram(str1, str2):

    if len(str1) != len(str2):
        return 'False, not same length'

    tally = {}

    for char in str1:
        if char in tally:
            tally[char] = tally[char] + 1
        else:
            tally[char] = 1

    for char in str2:
        if char in tally:
            tally[char] = tally[char] - 1
        else:
            return 'False, "' + char + '" exists in str2 but not str 1'

    for key in tally:
        if tally[key] > 0:
            return 'False, more "' + key + '" chars in str 1'
        elif tally[key] < 0:
            return 'False, more "' + key + '" chars in str 2'

    return True

def main():
    str1 = 'aB^09f'
    str2 = 'a0b9^9'
    print is_anagram(str1, str2)

main()
