
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tkinter Homework")
root.geometry("400x600")


left_frame = tk.Frame(root, bg='white')
left_frame.pack(side="left", fill="y")

def but1():
    with open(file= "built.txt", mode='r') as file:
        content = file.read()
    text_widget.config(state="normal")
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, content)
    text_widget.config(state="disabled")

def but2():
    with open(file= "fib.txt", mode='r') as file:
        content = file.read()
    text_widget.config(state="normal")
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, content)
    text_widget.config(state="disabled")

def but3():
    with open(file= "tower.txt", mode='r') as file:
        content = file.read()
    text_widget.config(state="normal")
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, content)
    text_widget.config(state="disabled")


button1 = tk.Button(left_frame, text='First Homework', width=20, height=4, background="gray", command=but1)
button1.pack()
button2 = tk.Button(left_frame, text='Second Homework', width=20, height=4, background="gray", command=but2)
button2.pack()
button3 = tk.Button(left_frame, text='Third Homework', width=20, height=4, background="gray", command=but3)
button3.pack()

right_frame = tk.Frame(root, highlightcolor='black', highlightthickness=2)
right_frame.pack(side="right", fill="both", expand=True)

scrollbar = tk.Scrollbar(right_frame)
scrollbar.pack(side="right", fill="y")

text_widget = tk.Text(right_frame, wrap="word", yscrollcommand=scrollbar.set)
text_widget.pack(side="left", fill="both", expand=True)

scrollbar.config(command=text_widget.yview)


def close_frame():
    text_widget.config(state="normal")
    text_widget.delete(1.0, tk.END)
    text_widget.config(state="disabled")


close_button = tk.Button(left_frame, text='Main Page', width=20, height=4, background="red", command=close_frame)
close_button.pack()

root.mainloop()
