# # jabber = open("/Users/isaachunter/Desktop/sample.txt", 'r')
# jabber = open("sample.txt", 'r')
#
# # # # python reads/iterates through lines of files like a list
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')

# # # end='' is used in print() because file includes \n in file after each new line
#
# jabber.close()  # if this is not present, could corrupt file


# with open("sample.txt", 'r') as jabber:  # no need to close file with "with"
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')


# with open("sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()


# with open("sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')


with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end='')

with open("sample.txt", 'r') as jabber:
    lines = jabber.read()  # .read() is more useful for binary file
print(lines)

for line in lines[::-1]:
    print(line, end='')