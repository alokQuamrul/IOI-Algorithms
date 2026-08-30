def counting_chars(text):
    frequency = {}
    for i in text:
        if i in frequency: #Have we seen this character already in the frequency dictionary?
            frequency[i] += 1

        else: #Are we seeing the character for the first time in the dictionary?
            frequency[i] = 1 #as the character is first time in the dictionary, initilize its value as 1
    return frequency



text = input("Enter a string:")
print(counting_chars(text))

