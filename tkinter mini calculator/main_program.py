from tkinter import *
from tkinter import ttk
import theme as secondary
import main_window as window

#head of script
main_frame = ttk.Frame(window)
main_frame.pack(padx=0, pady=10)
main_frame['padding'] = 5              
main_frame['padding'] = (335, 10)        
main_frame['padding'] = (5, 7, 10, 12) 

ttk.Label(main_frame, text="Welcome To My App!").pack()

ttk.Label(
    main_frame,
    text="This is my first tkinter app",
).pack()


ttk.Button(
    main_frame,
    text="Enter your name"
).pack()


ttk.Checkbutton(
    main_frame,
    text='like'
).pack

ttk.Entry(main_frame).pack()
