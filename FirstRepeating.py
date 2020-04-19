class FirstRepeating:

    def first_repeating(string):
        temp = {}
        for letter in string:
            if letter in temp:
                return letter
            else:
                temp[letter] = 0
        return '\nNo repeated characters.'

    word = input("Enter: ")
    output = first_repeating(word)
    print(output)