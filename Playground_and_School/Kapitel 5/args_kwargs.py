def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print (add(2, 3))          # Output: 6