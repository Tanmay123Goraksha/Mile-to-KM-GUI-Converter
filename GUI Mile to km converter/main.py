 import tkinter as Tk


window = Tk()
window.title("Miles to KM Converter")
miles_input = Entry()
miles_input.grid(column=1,row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

km_labelfinal = Label(text="NA")
km_labelfinal.grid(column=1,row=1)

kilometer_label =  Label(text="km")
kilometer_label.grid(column=2,row=1)

calculate_button = Button(text = "Calculate")
calculate_button.grid(column=1,row=2)