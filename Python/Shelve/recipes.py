import shelve

# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

# with shelve.open('recipes') as recipes:  # Method 1, unchanged
with shelve.open('recipes', writeback=True) as recipes:  # Method 2, writeback=True
    # recipes["blt"] = blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrambled_eggs
    # recipes["pasta"] = pasta
    # recipes["soup"] = soup

    # recipes["blt"].append("butter")
    # recipes["pasta"].append("tomato")  # does not work to update data

    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list  # does work to update data, method 1
    #
    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list

    # recipes["soup"].append("croutons")  # does work to update data, method 2
    recipes["soup"] = soup
    recipes.sync()  # sync placement makes it unable to update soup
    soup.append("cream")

    for snack in recipes:
        print(snack, recipes[snack])
