import tkinter as tk
from tkinter import messagebox

# Functionality for the To-Do List
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def update_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task:
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, new_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def clear_tasks():
    task_listbox.delete(0, tk.END)

def highlight_task(event):
    """Highlight the selected task."""
    for i in range(task_listbox.size()):
        task_listbox.itemconfig(i, bg="white", fg="#333")  # Reset styles
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.itemconfig(selected_task_index, bg="#4caf50", fg="white")  # Highlight selected task
    except IndexError:
        pass

# GUI Setup
root = tk.Tk()
root.title("Modern To-Do List")
root.geometry("500x500")
root.configure(bg="#f0f4f7")

# Title Label
title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 20, "bold"), bg="#f0f4f7", fg="#333")
title_label.pack(pady=15)

# Task Entry Frame
entry_frame = tk.Frame(root, bg="#f0f4f7")
entry_frame.pack(pady=10)

task_entry = tk.Entry(entry_frame, width=35, font=("Helvetica", 14), borderwidth=2, relief="solid")
task_entry.pack(side=tk.LEFT, padx=10, pady=5)

add_button = tk.Button(entry_frame, text="Add Task", command=add_task, bg="#4caf50", fg="white", font=("Helvetica", 12, "bold"), width=12, borderwidth=0)
add_button.pack(side=tk.LEFT, padx=5)

# Task List Frame
list_frame = tk.Frame(root, bg="#f0f4f7")
list_frame.pack(pady=15)

task_listbox = tk.Listbox(
    list_frame,
    width=45,
    height=15,
    font=("Helvetica", 14),
    bg="white",
    fg="#333",
    selectbackground="#4caf50",
    selectforeground="white",
    borderwidth=2,
    relief="solid",
)
task_listbox.pack(side=tk.LEFT, padx=10)

scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Highlight Task on Selection
task_listbox.bind("<<ListboxSelect>>", highlight_task)

# Button Frame
button_frame = tk.Frame(root, bg="#f0f4f7")
button_frame.pack(pady=20)

update_button = tk.Button(button_frame, text="Update Task", command=update_task, bg="#ff9800", fg="white", font=("Helvetica", 12, "bold"), width=15, borderwidth=0)
update_button.grid(row=0, column=0, padx=10)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, bg="#f44336", fg="white", font=("Helvetica", 12, "bold"), width=15, borderwidth=0)
delete_button.grid(row=0, column=1, padx=10)

clear_button = tk.Button(button_frame, text="Clear All", command=clear_tasks, bg="#2196f3", fg="white", font=("Helvetica", 12, "bold"), width=15, borderwidth=0)
clear_button.grid(row=0, column=2, padx=10)

# Run the Application
root.mainloop()
