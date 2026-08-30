text = input("Give any random text: ")
sort = sorted(text) #insertion sort+merge sort
sorted_string = "".join(sort)
print(sorted_string)


#quick sort
def quickSort(text):
    if len(text) <= 1:
        return text 
    pivot = text[0]
    less = [x for x in text[1:] if x <= pivot]
    greater = [x for x in text[1:] if x > pivot]

    return quickSort(less) + [pivot] + quickSort(greater)

print("".join(quickSort(text)))