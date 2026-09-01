#Tkinter window for the calculator.

import tkinter as tk

from main_program import Calculator
import theme


class CalculatorWindow:
    def __init__(self, root):
        self.root = root
        self.calculator = Calculator()

        root.title("Tkinter Calculator")
        root.geometry("400x500")
        root.configure(bg=theme.BACKGROUND)

        self.display = tk.Entry(
            root,
            width=20,
            font=theme.DISPLAY_FONT,
            justify=tk.RIGHT,
            bd=10,
            bg=theme.DISPLAY_BACKGROUND,
            fg=theme.DISPLAY_FOREGROUND,
        )
        self.display.grid(
            row=0,
            column=0,
            columnspan=4,
            padx=10,
            pady=10,
            ipady=20,
            sticky="ew",
        )

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
        ]
        for index, value in enumerate(buttons):
            row, column = divmod(index, 4)
            self._add_button(value, row + 1, column, theme.NUMBER_BACKGROUND)

        self._add_button("C", 5, 0, theme.ACTION_BACKGROUND)
        self._add_button("⌫", 5, 1, theme.ACTION_BACKGROUND, "backspace")

        for row in range(1, 6):
            root.grid_rowconfigure(row, weight=1)
        for column in range(4):
            root.grid_columnconfigure(column, weight=1)

    def _add_button(self, label, row, column, background, value=None):
        tk.Button(
            self.root,
            text=label,
            font=theme.FONT,
            command=lambda: self._press(value or label),
            bg=background,
            fg=theme.FOREGROUND,
        ).grid(row=row, column=column, sticky="nsew")

    def _press(self, value):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.calculator.press(value))


def main():
    root = tk.Tk()
    CalculatorWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()

import tkinter
from tkinter import ttk
import ttkthemes as theme

#from main_program import main_frame_3 as main_3
import main_program

#load main_program and ui
#button click logic
def button_click(value):
    current = entry.get()
    entry.delete(0, tkinter.END)
    entry.insert(tkinter.END, current + str(value))

#backspace logic
def backspace():
    current = entry.get()
    entry.delete(0, tkinter.END)
    entry.insert(tkinter.END, current[:-1])

#evaluate logic
def evaluate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tkinter.END)
        entry.insert(tkinter.END, str(result))
    except Exception as e:
        entry.delete(0, tkinter.END)
        entry.insert(tkinter.END, "Error")

#entery logic
def clear_entry():
    entry.delete(0, tkinter.END)



#make the window
root = tkinter.Tk()
root.geometry("700x500")
root.title("Tkinter calculator")

#load the main frames
entry = tkinter.Entry(root, width=20, font=('Arial', 20), justify=tkinter.RIGHT, bd=10)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=20)

#buttons grids
buttons = ['7', '8', '9', '/',
           '4', '5', '6', '*',
           '1', '2', '3', '-',
           '0', '.', '=', '+']

row_val = 1
col_val = 0

#button loop
for button in buttons:
   tkinter.Button(
        root, text=button, padx=20, pady=20, font=('Arial', 16),
        command=lambda b=button: button_click(b) if b != '=' else evaluate(),
        bg="#61dafb", 
        fg="#282c35"   
    ).grid(row=row_val, column=col_val, sticky="nsew")  

   col_val += 1
   if col_val > 3:
       col_val = 0
       row_val += 1

#button grid pack
tkinter.Button(
    root, text='C', padx=20, pady=20, font=('Arial', 16),
    command=clear_entry, bg="#ff6b6b", fg="#282c35"
).grid(row=row_val, column=0, sticky="nsew")

tkinter.Button(
   root, text='⌫', padx=20, pady=20, font=('Arial', 16),
   command=backspace, bg="#ff6b6b", fg="#282c35"
).grid(row=row_val, column=1, sticky="nsew")


for i in range(1, 5):
   root.grid_rowconfigure(i, weight=1)
   root.grid_columnconfigure(i, weight=1)

#execute entire app
root.mainloop()

