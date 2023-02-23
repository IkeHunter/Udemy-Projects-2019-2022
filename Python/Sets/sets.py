# # # Sets are like a dictionary of just keys
# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
# print("=" * 40)
#
# wild_animals = set(["lion", "tiger", "panther", "elephant"])
# print(wild_animals)
#
# for animal in wild_animals:
#     print(animal)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)

# empty_set = set()
# empty_set_2 = {}  # creates dictionary
# empty_set.add("a")
# # empty_set_2.add("a")  # returns error because it is a dictionary
#
# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)

# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))
#
# print(even.union(squares))  # could use | operator for union
# print(len(even.union(squares)))
#
# print(squares.union(even))  # same as line 40
#
# print("-" * 40)
#
# print(even.intersection(squares))  # same output, could use & operator like below
# print(even & squares)  # same output
# print(squares.intersection(even))  # same output
# print(squares & even)  # same output


# even = set(range(0, 40, 2))
# print(sorted(even))
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(sorted(squares))
#
# print("even minus squares")
# print(sorted(even.difference(squares)))  # preferred method
# print(sorted(even - squares))
#
# print("squares minus even")
# print(squares.difference(even))  # preferred method
# print(squares - even)
#
# print("=" * 40)
# print(sorted(even))
# print(squares)
# even.difference_update(squares)  # like -= operator
# print(sorted(even))


# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)

# print("symmetric even minus squares")
# print(sorted(even.symmetric_difference(squares)))
#
# print("symmetric squares minus even")
# print(squares.symmetric_difference(even))  # could use ^ operator for symmetric difference

# squares.discard(4)
# squares.remove(16)
# squares.discard(8)
# print(squares)
# # squares.remove(8)  # returns error, discard would not, use for when error is needed
# # if 8 in squares:
# #     squares.remove(8)
# try:
#     squares.remove(8)
# except KeyError:
#     print("The item 8 is not a member of the set")


# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 16)
# squares = set(squares_tuple)
# print(squares)
#
# if squares.issubset(even):  # could use <= operator
#     print("squares is a subset of even")  # even contains all the values of squares
#
# if even.issuperset(squares):  # could use >= operator
#     print("even is a superset of squares")


even = frozenset(range(0, 100, 2))

print(even)
# even.add(3)  # returns error, is immutable, doesn't allow these types of methods



