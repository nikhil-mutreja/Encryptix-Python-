import tkinter as tk
from tkinter import PhotoImage, StringVar, Entry, Frame, Label, Listbox, END

root = tk.Tk()
root.title("To-Do-List")
root.geometry("400x700+400+50")
root.resizable(False, False)

tasks = []

# Load images
image = PhotoImage(file=r"C:\Users\NIKHIL\Downloads\images\task.png")
root.iconphoto(False, image)
top = PhotoImage(file=r"C:\Users\NIKHIL\Downloads\images\topbar.png")
dock = PhotoImage(file=r"C:\Users\NIKHIL\Downloads\images\dock.png")
note = PhotoImage(file=r"C:\Users\NIKHIL\Downloads\images\task.png")

# Add top bar image
Label(root, image=top).pack()

# Add dock and note images
Label(root, image=dock, bg="#32405b").place(x=30, y=25)
Label(root, image=note, bg="#32405b").place(x=340, y=25)

# Heading
heading = Label(root, text="All Tasks", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

# Frame for task entry
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

# Task entry widget
task_var = StringVar()
entry = Entry(frame, width=18, font="arial 20", bd=0, textvariable=task_var)
entry.place(x=10, y=7)

# Listbox for tasks
listbox = Listbox(root, font=('arial', 12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.place(x=10, y=250)

def add_task():
    task = task_var.get()
    if task != "":
        tasks.append(task)
        listbox.insert(END, task)
        task_var.set("")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
        tasks.pop(selected_task_index)
    except IndexError:
        pass

def edit_task():
    try:
        selected_task_index = listbox.curselection()[0]
        selected_task = listbox.get(selected_task_index)
        task_var.set(selected_task)
        listbox.delete(selected_task_index)
        tasks.pop(selected_task_index)
    except IndexError:
        pass

# Button to add tasks
add_button = tk.Button(root, text="Add Task", font="arial 15", bg="#5a95ff", command=add_task)
add_button.place(x=30, y=650)

# Button to delete tasks
delete_button = tk.Button(root, text="Delete Task", font="arial 15", bg="#ff5a5a", command=delete_task)
delete_button.place(x=150, y=650)

# Button to edit tasks
edit_button = tk.Button(root, text="Edit Task", font="arial 15", bg="#5a95ff", command=edit_task)
edit_button.place(x=280, y=650)

root.mainloop()
