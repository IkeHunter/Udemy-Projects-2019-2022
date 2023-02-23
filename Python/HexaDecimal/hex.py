# for i in range(17):
#     print("{0:>2} in hex is {0:>02x}".format(i))
#
# x = 0x20
# y = 0x0a
#
# print(x)
# print(y)
# print(x * y)
#
# print(0b101010)


# challenge ----

# # binary = []
#
# num = int(input("Enter number: "))
#
# binary_num = 0
#
# i = 0
#
# while num > 2**i:
#     i += 1
# i -= 1
# binary_num = 1 * 10**i
# i += 1
# binary_first = binary_num
# j = i
# while i >= 0:
#     if num >= 2**i:
#         # binary.append("1")
#         num -= 2**i
#         binary_num += 1+10**j - 1
#         i -= 1
#         j -= 1
#
#     else:
#         # binary.append("0")
#         i -= 1
#         j -= 1
#
# binary_num -= binary_first
# print(binary_num)
#
# # binary.pop(0)
# # binary_iter = iter(binary)
# # for i in range(0, len(binary)):
# #     print("{}".format(next(binary_iter)), end=" ")


# Instructors version ----

powers = []
for power in range(15, -1, -1):
    powers.append(2 ** power)  # enter 8 for octal

print(powers)

x = int(input("Please enter a number: "))

printing = False

for power in powers:
    # print("power = {0}, x = {1}".format(power, x))
    bit = x // power
    # print("x // power = {}".format(bit))
    if bit != 0 or power == 1:
        printing = True
    if printing:
        print(bit, end='')
        # print("Bit = {}".format(bit))
    x %= power
    # print("x %= power = {}".format(x))
    # print("Break")


# Final solution ----

# num = int(input("Enter number: "))
#
# binary_num = 0
#
# i = 0
#
# while num > 2**i:
#     i += 1
#
# binary_num = 1 * 10**(i - 1)
#
# binary_first = binary_num
# while i >= 0:
#     if num >= 2**i:
#         num -= 2**i
#         binary_num += 1+10**i - 1
#         i -= 1
#
#     else:
#         i -= 1
#
# binary_num -= binary_first
# print(binary_num)
