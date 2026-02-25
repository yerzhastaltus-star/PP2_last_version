# 1. Square generator
def square_generator(n):
    for i in range(n+1):
        yield i*i


# 2. Even numbers
def even_numbers(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i


# 3. Divisible by 3 and 4
def divisible(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


# 4. Squares in range
def squares(a, b):
    for i in range(a, b+1):
        yield i*i


# 5. Countdown
def countdown(n):
    while n >= 0:
        yield n
        n -= 1



# Testing section
# This block runs only when the file is executed directly.
# It demonstrates how each generator function works
# by calling them with example values and printing the results.

if __name__ == "__main__":

    # Testing square_generator: prints squares from 0 to 5
    print("Squares up to 5:")
    for num in square_generator(5):
        print(num)

    # Testing even_numbers: user enters n, program prints all even numbers up to n
    n = int(input("Enter n for even numbers: "))
    print(",".join(str(x) for x in even_numbers(n)))

    # Testing divisible: prints numbers up to 100 divisible by both 3 and 4
    print("Divisible by 3 and 4 up to 100:")
    for num in divisible(100):
        print(num)

    # Testing squares: prints squares of numbers from 3 to 7
    print("Squares from 3 to 7:")
    for num in squares(3, 7):
        print(num)

    # Testing countdown: prints numbers from 5 down to 0
    print("Countdown from 5:")
    for num in countdown(5):
        print(num)