def spam1():

    def spam2():

        def spam3():
            # z = " even more spam"
            z = " even"
            z += y
            print("In spam3, locals are {}".format(locals()))
            return z

        # y = " more spam"
        y = " more " + x  # y must exist before spam3 is called
        y += spam3()  # do not combine assignments
        print("In spam2, locals are {}".format(locals()))
        return y

    x = "spam"  # x must exist before spam() is called
    x += spam2()  # do not combine assignments
    # # 'x = "spam" + spam2()' would return err, x would not be defined in spam2()
    print("In spam1, locals are {}".format(locals()))
    return x


print(spam1())
print(locals())  # same output as globals()
print(globals())


# # python searches for var names in this order, resolves names:
# # # LEGB - Local, Enclosing(used in this file), Global, Builtins
