print("For x / y")
x = input("What is x? ")
y = input("And what is y? ")


def divide(h, k):
    print("{} / {} is {}".format(str(h), str(k), str(h/k)))


try:
    x = int(x)
    y = int(y)

    divide(x, y)
except ValueError:
    print("Cannot divide strings!")

