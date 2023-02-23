# Tuples are lists that can't be changed -> "immutable"

# t = ("a", "b", "c")  # parenthesis are not required, but is most common
# print(t)
#
# print("a", "b", "c")
# print(("a", "b", "c"))


# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Imilda May", 2011
# metallica = "Ride the Lightning", "Metallica", 1984
#
# # print(metallica)
# # print(metallica[0])
# # print(metallica[1])
# # print(metallica[2])
#
# # metallica[0] = "Master of puppets"  #returns error
#
# # imelda = imelda[0], "New Value", imelda[2]  # Created a new tuple with same name
# # print(imelda)
#
# metallica2 = ["Ride the Lightning", "Metallica", 1984]
# print(metallica2)
#
# # metallica2[0] = "Master of Puppets"
# # print(metallica2)
#
# title, artist, year = imelda  # called 'unpacking the tuple'
# print(title)
# print(artist)
# print(year)
#
#
# # metallica2.append("rock")  # returns error
# #
# # title, artist, year = metallica2
# # print(title)
# # print(artist)
# # print(year)
#
# imelda.append("Jazz")  # returns error


# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# # imelda = "More Mayhem", "Imilda May", 2011, (
# #     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))  # *
# imelda = "More Mayhem", "Imilda May", 2011, (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")  # **
#
# print(imelda)
#
# # title, artist, year, tracks = imelda  # *
# title, artist, year, track1, track2, track3, track4 = imelda  # **
# print(title)
# print(artist)
# print(year)
# print(track1)
# print(track2)
# print(track3)
# print(track4)


imelda = "More Mayhem", "Imilda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))  # *

# My version --

# for detail in range(0, len(imelda) - 1):
#     print(imelda[detail])
#
# for track in imelda[3]:
#     print("Track {0:<2}: {1}".format(track[0], track[1]))

# Solution --

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("\tTrack number {}, Title: {}".format(track, title))


imelda2 = "More Mayhem", "Imilda May", 2011, (
    [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")])

print(imelda2)
imelda2[3].append((5, "All For You"))
print(imelda2)  # it is possible to store a list inside a tuple, the list can be changed, but the tuple cannot
