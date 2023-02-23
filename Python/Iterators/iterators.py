string = "1234567890"

# for char in string:
#     print(char)

# my_interator = iter(string)
# print(my_interator)
# print(next(my_interator))
# print(next(my_interator))
# print(next(my_interator))
# print(next(my_interator))
# print(next(my_interator))
# print(next(my_interator))
# print(next(my_interator))
# print(next(my_interator))
# print(next(my_interator))
# print(next(my_interator))

# for char in string:
#     print(char)
#
# for char in iter(string):
#     print(char)


list_1 = ["one", "two", "three", "four", "five"]
iter_list = iter(list_1)

# for n in range(0, len(list_1)):
#     print(next(iter_list))

for n in range(0, len(list_1)):
    next_item = next(iter_list)
    print(next_item)
