my_string = "Kamrul's lesson on String"
my_string2 = 'Ammu says, "Complete your home work now"'

#Method 01
def reversing_string_naive(text):
    rev = ""
    for i in range(len(text)-1,-1,-1): #inverse loop
        rev += text[i]
    return rev

text_input = input("Enter Your text for reversing:")
print(f"The bruteforce approach to reverse a string, {text_input}:{reversing_string_naive(text_input)}")
print(f"Time Complexity:O(n) , Space Complexity: O(n)")


#method 02
def reversing_string_better(text):
    size = len(text)
    text = list(text)
    for i in range(size//2):
        text[i],text[size-i-1] = text[size-i-1],text[i]
    return "".join(text)

text_input = input("Enter Your text for reversing:")
print(f"The better bruteforce approach to reverse a string, {text_input}:{reversing_string_better(text_input)}")
print(f"Time Complexity:O(n/2) , Space Complexity: O(n)")


#method 03 :Best approach
print(f"The best approach to reverse a string, {text_input}:{text_input[::-1]}")
print(f"Time Complexity:O(1) , Space Complexity: O(1)")