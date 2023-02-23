# # x = 8 = 5  # SyntaxError
# x = 8 - 5
# y = x / 0  # ZeroDivisionError


def factorial(n):
    """ calculates n! recursively """
    if n <= 1:
        return 1
    else:
        # print(n / 0)
        return n * factorial(n-1)


try:
    print(factorial(900))
except (RecursionError, OverflowError):
    print("This program cannot calculate factorials that large")
# except ZeroDivisionError:
#     print("What are you doing dividing by zero???")

print("Program terminating")
