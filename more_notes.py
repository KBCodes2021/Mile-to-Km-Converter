# from tkinter import *
#
#
#
# window = Tk()
# window.title("App")
# window.minsize(width=500, height=300)
# window.config(padx=100, pady=200)
#
# #
#
# my_label = Label(text="Label is here", font=("Arial", 12, "bold"))
#
# #Activate the label we created onto screen
# my_label.grid(column=0, row=0)
#
# my_label["text"] = "New text"
# my_label.config(text="New Text")
# my_label.config(padx=10, pady=10)
#
# #Button
#
# def button_clicked():
#     print("I got clicked")
#
# button = Button(text="Click_me", command=button_clicked)
# button.grid(column=3, row=0)
#
# def button_clicked2():
#     print("I got clicked")
#
# button = Button(text="Click_me", command=button_clicked)
# button.grid(column=2, row=1)
#
#
# #Entry
#
# input = Entry(width=10)
# input.grid(column=4, row=3)
# print(input.get())
#
#
#
#
# window.mainloop()