# Definition of the main function.
def main():
    get_name()
    print(f'Hello, {name}.') #This causes an error because 'name' is not defined in this scope.

# Definition of the get_name function.
def get_name():
    global name  # This line would fix the error by declaring 'name' as a global variable.
    name = input('What is your name? ') # 'name' is a local variable to this function.

#Call the main function.
main()