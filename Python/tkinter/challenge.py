import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Calculator")
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = 10

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=2)
mainWindow.columnconfigure(4, weight=5)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=2)
mainWindow.rowconfigure(2, weight=2)
mainWindow.rowconfigure(3, weight=2)
mainWindow.rowconfigure(4, weight=2)
mainWindow.rowconfigure(5, weight=2)
mainWindow.rowconfigure(6, weight=5)

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
num_names = ["num_1", "num_2", "num_3", "num_4", "num_5", "num_6", "num_7", "num_8", "num_9"]
characters = ["+", "-", "*", "/", "="]
char_names = ["plus", "minus", "mult", "div"]
meta = ["C", "CE"]
meta_name = ["c_val", "ce_val"]

answer = tkinter.Entry(mainWindow)
answer.grid(row=0, column=0, columnspan=4, sticky='nsew')

for i in range(0, 2):
    meta_name[i] = tkinter.Button(mainWindow, text=meta[i])
    meta_name[i].grid(row=1, column=i, sticky='nsew')

for i in range(0, 9):
    if i <= 3:
        for j in range(0, 3):
            num_names[i] = tkinter.Button(mainWindow, text=numbers[i + j - 3])
            num_names[i].grid(row=4, column=j, sticky='nsew')
    elif (i <= 6) & (i > 3):
        for k in range(0, 3):
            num_names[i] = tkinter.Button(mainWindow, text=numbers[i + k - 3])
            num_names[i].grid(row=3, column=k, sticky='nsew')
    elif (i <= 9) & (i > 6):
        for l in range(0, 3):
            num_names[i] = tkinter.Button(mainWindow, text=numbers[i + l - 2])
            num_names[i].grid(row=2, column=l, sticky='nsew')

num_0 = tkinter.Button(mainWindow, text="0")
num_0.grid(row=5, column=0, sticky='nsew')

equal = tkinter.Button(mainWindow, text=characters[4])
equal.grid(row=5, column=1, columnspan=2, sticky='nsew')

for i in range(0, 4):
    char_names[i] = tkinter.Button(mainWindow, text=characters[i])
    char_names[i].grid(row=i+2, column=3, sticky='nsew')


mainWindow.mainloop()
