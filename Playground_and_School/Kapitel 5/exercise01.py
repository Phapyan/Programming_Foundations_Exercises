# Function: max three ints
def find_max(val1, val2, val3):
    largest = val1
    if val2 > largest:
        largest = val2
    if val3 > largest:
        largest = val3
    return largest

#Aufruf
print(find_max(3, 5, 2))