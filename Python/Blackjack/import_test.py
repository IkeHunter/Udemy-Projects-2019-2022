# from blackjack import *  # all the names from bj namespace is now in this name space
import blackjack

# g = sorted(globals())
#
# for x in g:
#     print(x)

# blackjack._deal_card(blackjack.dealer_card_frame)

# print(__name__)
# blackjack.play()
# print(blackjack.cards)


personal_details = ("Tim", 24, "Australia")

name, _, country = personal_details  # _ as opposed to 'age' bc it isn't needed
print(name, country)  # print(_) would still work

# underscores:
# # > use one after var name when name would conflict with predefined python var
# # > starting var name with underscore means it's supposed to be protected/private, doesn't prevent
# # > anything with two leading and two following underscores shouldn't be changed
# # > when var name is just an _, it means it's a throwaway value, useless

