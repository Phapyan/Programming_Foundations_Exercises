import random
def main():
    for _ in range(5):
        print(random.randint(1, 100))

main()

# Alternative solution using specific import
from random import randint
def main():
    for _ in range(5):
        print(randint(1, 100))

main()
