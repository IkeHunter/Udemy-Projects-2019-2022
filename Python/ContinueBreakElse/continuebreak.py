# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == 'spam':
#         break  # || continue
#
#     print("Buy " + item)


meal = ["egg", "bacon", "beans", "sausages"]
nasty_food_item = ''

for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
else:  # if loop is able to be carried out until the end "else there is no break -> do this"
    # nasty_food_item = ''
    print("I'll have a plate of that, then, please")


if nasty_food_item == 'spam':
    print("Can't I have anything without spam in it?")
