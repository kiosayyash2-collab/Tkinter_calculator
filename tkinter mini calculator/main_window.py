import tkinter
from tkinter import ttk

#from main_program import main_frame_3 as main_3
import theme
import main_program

#load main_program and ui
#button click logic
def button_click(value):
    current = entry.get()
    entry.delete(0, ttk.END)
    entry.insert(ttk.END, current + str(value))

#backspace logic
def backspace():
    current = entry.get()
    entry.delete(0, ttk.END)
    entry.insert(ttk.END, current[:-1])

#evaluate logic
def evaluate():
    try:
      expression = entry.get()
      result = eval(expression)
      entry.delete(0, ttk.END)
      entry.insert(ttk.END, str(result))
    except Exception as e:
      entry.delete(0, ttk.END)
      entry.insert(ttk.END, "Error")

#entery logic
def clear_entry():
    entry.delete(0, ttk.END)      



#make the window
root = tkinter.Tk()
root.geometry("700x500")
root.title("Tkinter calculator")

#load the main frames
entry = ttk.Entry(root, width=20, font=('Arial', 20), justify=tk.RIGHT, bd=10)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=20)

#buttons grids
buttons = ['7', '8', '9', '/',
           '4', '5', '6', '*',
           '1', '2', '3', '-',
           '0', '.', '=', '+']

row_val = 1
col_val = 0

#button loop
for button in buttons():
   ttk.Button(root, text='C', padx=20, pady=20, font=('Arial', 16),
              command=lambda b=button: button_click(b) if b != '=' else evaluate(),
              bg="#61dafb", 
              fg="#282c35"   
              col_val += 1
              if col_val >= 3
                 col_val == 0
                 row_val += 1)




#execute entire app
root.mainloop()

