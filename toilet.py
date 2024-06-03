import tkinter as tk
import ttkbootstrap as ttkb

def update_expression(symbol):
    expression = entry_var.get()
    entry_var.set(expression + symbol)

def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(str(result))
    except:
        entry_var.set("Error")

def clear():
    entry_var.set("")

app = ttkb.Window(themename="darkly")

app.geometry("300x400")
app.title("Kalkulator dengan Tkinter dan TTKbootstrap")

entry_var = tk.StringVar()
entry = ttkb.Entry(app, textvariable=entry_var, font=("Helvetica", 16), bootstyle="info")
entry.pack(pady=10, padx=10, fill="x")

button_frame = ttkb.Frame(app)
button_frame.pack(pady=10)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

for row in buttons:
    button_row = ttkb.Frame(button_frame)
    button_row.pack(fill="x")
    for symbol in row:
        if symbol == "=":
            btn = ttkb.Button(button_row, text=symbol, command=calculate, bootstyle="success", width=6)
        else:
            btn = ttkb.Button(button_row, text=symbol, command=lambda s=symbol: update_expression(s), bootstyle="secondary", width=6)
        btn.pack(side="left", padx=5, pady=5)

clear_button = ttkb.Button(app, text="Clear", command=clear, bootstyle="danger", width=26)
clear_button.pack(pady=10, padx=10)
app.mainloop()
