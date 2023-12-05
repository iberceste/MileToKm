from tkinter import *

window = Tk()
window.title("Mile to Km Calculate")
window.minsize(width=300, height=200)


def button_clicked():
    km = int((miles_input.get()))
    km_input.config(text=round((km*1.6)))
# Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_input = Label(text=0)
km_input.grid(column=1, row=1)


# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)




window.mainloop()