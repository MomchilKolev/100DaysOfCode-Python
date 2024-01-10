from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=20, pady=20)


def miles_to_km():
    km = int(miles_input.get()) * 1.609344
    rounded_km = round(km, 1)
    km_output_label.config(text=rounded_km)


miles_input = Entry(width=6)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

km_output_label = Label(text="0")
km_output_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
