#determine if two strings are anagrams

def is_anagram(str1, str2):
    #assume strings composed of 26 chars of alphabet
    count1 = [0] * 26
    count2 = [0] * 26

    str1 = str1.lower()
    str2 = str2.lower()

    if len(str1) != len(str2):
        return False

    for i in range(len(str1)):
        posn = ord(str1[i]) - ord('a')
        count1[posn] = count1[posn] + 1
        posn = ord(str2[i]) - ord('a')
        count2[posn] = count2[posn] + 1

    for i in range(26):
        if count1[i] != count2[i]:
            return False
    return True

def main():
    str1 = "abCde"
    str2 = "bcaed"
    print is_anagram(str1, str2)

main()
