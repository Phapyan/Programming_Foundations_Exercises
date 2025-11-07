def example(a, b=2, c=3):
    print(a, b, c)

example(5, 9, 1) # Positional arguments
example(5, c=7)  # Mixed positional and keyword arguments
example(a=4, b=6, c=8) # All keyword arguments

#Rule: Positional arguments must come before keyword arguments

#false function call examples:
#example(a=4, 6, c=8) # This will raise a Syntax
#example(5, b=6, 8) # This will raise a Syntax
#example(b=6, a=5, 8) # This will raise a Syntax
#example(a, c, b) # this will work but would be wrong order

