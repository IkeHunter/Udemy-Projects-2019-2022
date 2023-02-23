# My version ----
#
# with open("sample.txt", 'a') as poem_file:
#     for i in range(1, 12):
#         print("{0:2} times 2 is {1}".format(i, i*2), file=poem_file)


with open("sample.txt", 'a') as tables:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{1:>2} times {0} is {2}".format(i, j, i * j), file=tables)
        print("-" * 20, file=tables)

