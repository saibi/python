import tkinter

# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum


# print(add(1, 2, 3, 4, 5))


# def calculate(n, **kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     n += kwargs["add"]
#     n *= kwargs["mul"]
#     print(n)

# calculate(2, add=3, mul=5)


# window = tkinter.Tk()
# window.title("first tkinter gui")
# window.minsize(width=500, height=300)
# window.config(padx=10, pady=10)

# my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label["text"] = "New Text"
# my_label.grid(column=0, row=0)

# button = tkinter.Button(text="Click Me")


# def button_clicked():
#     my_label.config(text=input.get())


# button["command"] = button_clicked
# button.grid(column=1, row=1)


# def new_button_clicked():
#     print("new button clicked")


# new_button = tkinter.Button(text="New Button", command=new_button_clicked)
# new_button.grid(column=2, row=0)

# input = tkinter.Entry(width=10)
# input.insert(tkinter.END, string="Some text to")
# input.grid(column=3, row=2)

# window.mainloop()


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=10, pady=10)

input_miles = tkinter.Entry(width=10)
input_miles.grid(column=1, row=0)

label_miles = tkinter.Label(text="Miles")
label_miles.grid(column=2, row=0)

label_equal = tkinter.Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_result_km = tkinter.Label()
label_result_km.grid(column=1, row=1)

label_km = tkinter.Label(text="Km")
label_km.grid(column=2, row=1)


def button_clicked():
    km = float(input_miles.get()) * 1.609
    label_result_km.config(text=km)


button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
