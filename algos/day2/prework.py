def anagram_checking_off(s1, s2):
    if len(s1) != len(s2):
        return False

    to_check_off = list(s2)

    for char in s1:
        for i, other_char in enumerate(to_check_off):
            if char == other_char:
                to_check_off[i] = None
                # break out of the current for-loop to the outer one and continue searching for the next character
                break
        else:
            # Only executes if the above for loop did NOT break
            # In the case that we did not break, we should return false because char in s1 was never matched to other_char in s2
            return False

    return True

# print(anagram_checking_off('abcd', 'dcba'))
# print(anagram_checking_off('abcd', 'abcc'))
