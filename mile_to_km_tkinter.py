from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")


# window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=120)
window.config(padx=20, pady=20)
window.configure(background="pink", relief="raised", highlightcolor="black",
                 highlightbackground="black", highlightthickness=5)

# miles entry
miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)
miles_input.configure(relief="sunken")

# miles label
miles_label = Label(text="Miles", font=("Arial", 10, "normal"))
miles_label.config(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.configure(background="pink")

# miles label
miles_label = Label(text="K.S GUI", font= ("Arial", 8, "bold"))
miles_label.config(text="K.S GUI")
miles_label.grid(column=0, row=0)
miles_label.configure(background="pink")

# is equal label
is_equal_label = Label(text="is equal to", font=("Arial", 10, "normal"))
is_equal_label.config(text="is equal to")
is_equal_label.grid(column=0, row=1)
is_equal_label.configure(background="pink")

# km label
km_label = Label(text="Km", font=("Arial", 10, "normal"))
km_label.config(text="Km")
km_label.grid(column=2, row=1)
km_label.configure(background="pink")

# km result label
km_result_label = Label(text="0", font=("Arial", 10, "normal"))
km_result_label.config(text="0")
km_result_label.grid(column=1, row=1)
km_result_label.configure(background="pink")

# calculate button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)
calculate_button.configure(relief="raised")

window.mainloop()
