from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=km)

window = Tk()
window.title("Mile to KM Converter")
window.config(padx=100, pady=80)

miles_input = input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to = Label(text="Equals")
is_equal_to.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="KM")
kilometer_label.grid(column=2, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=2, row=3)


window.mainloop()