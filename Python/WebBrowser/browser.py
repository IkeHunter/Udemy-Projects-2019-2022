import webbrowser

# webbrowser.open("https://www.python.org/")
#
# help(webbrowser)

# for i in range(10):
#     print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep=';', end=' ')

# webbrowser.open("https://www.python.org/", new=2)

# chrome = webbrowser.get(using='chrome')
# chrome.open_new("https://www.python.org/")

# chrome = webbrowser.get('/usr/bin/google-chrome %s').open_new_tab("https://www.python.org/")  # doesnt work

safari = webbrowser.get(using='safari')
safari.open("https://www.python.org/")
