# def python_food():
#     print("spam and eggs")
#
#
# # call the function
# python_food()
# print(python_food())  # returns None


def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


# def center_text(text):
#     text = str(text)
#     left_margin = (80 - len(text)) // 2
#     print(" " * left_margin, text)


def center_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    text = str(text)
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text


# print(center_text("spam and eggs"))
# print(center_text("spam, spam and eggs"))
# print(center_text(12))
# print(center_text("spam, spam, spam and spam"))
# print(center_text("first", "second", 3, 4, "spam", sep=":"))
#
# print("=" + str(12 * 3))
# print(sorted(["b", "d", "c", "a"]))


# center_text(12)  # before added str(): returns err, numbers don't have char length

# print("first", "second", 3, 4, "spam")  # can easily print more than one argument


# s1 = center_text("spam and eggs")
# print(s1)
# s2 = center_text("spam, spam and eggs")
# print(s2)
# s3 = center_text(12)
# print(s3)
# s4 = center_text("spam, spam, spam and spam")
# print(s4)
# s5 = center_text("first", "second", 3, 4, "spam", sep=":")
# print(s5)
#
# print("=" + str(12 * 3))
# print(sorted(["b", "d", "c", "a"]))


with open("menu", "w") as menu:
    s1 = center_text("spam and eggs")
    print(s1, file=menu)
    s2 = center_text("spam, spam and eggs")
    print(s2, file=menu)
    print(center_text(12), file=menu)
    print(center_text("spam, spam, spam and spam"), file=menu)
    s5 = center_text("first", "second", 3, 4, "spam", sep=":")
    print(s5, file=menu)
