def char_freq(string):
    frequency_of_characters = {}
    for char in string.lower():
        if char not in frequency_of_characters and char in "abcdefghijklmnopqrstuvwxyz":
            frequency_of_characters[char] = 1
        elif char in frequency_of_characters and char in "abcdefghijklmnopqrstuvwxyz":
            frequency_of_characters[char] += 1
    return frequency_of_characters


def main():
    frequency_of_characters = char_freq("abbabcbdbabdbdbabababcbcbab")
    print(frequency_of_characters)


if __name__ == '__main__':
    main()
