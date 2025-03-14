import tkinter as tk
from tkinter import messagebox

class TodoApp:
       def __init__(self, root):
           self.root = root
           self.root.title("To-Do List App")

           self.tasks = []

           self.frame = tk.Frame(root) #tk.Frame creates a container for widgets.

           self.frame.pack(pady=10)

           self.task_entry = tk.Entry(self.frame, width=40)#tk.Entry is used for input fields.

           self.task_entry.pack(side=tk.LEFT, padx=10)

           self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
           self.add_button.pack(side=tk.LEFT)   #tk.Button creates buttons that can trigger functions.


           self.task_listbox = tk.Listbox(root, width=50, height=10)#tk.Listbox displays a list of items.

           self.task_listbox.pack(pady=10)

           self.remove_button = tk.Button(root, text="Remove Selected Task", command=self.remove_task)
           self.remove_button.pack()

       def add_task(self):
           task = self.task_entry.get()
           if task:
               self.tasks.append(task)
               self.update_task_listbox()
               self.task_entry.delete(0, tk.END)
           else:
               messagebox.showwarning("Warning", "You must enter a task!")

       def remove_task(self):
           selected_task_index = self.task_listbox.curselection()
           if selected_task_index:
               self.tasks.pop(selected_task_index[0])
               self.update_task_listbox()
           else:
               messagebox.showwarning("Warning", "You must select a task to remove!")

       def update_task_listbox(self):
           self.task_listbox.delete(0, tk.END)
           for task in self.tasks:
               self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()  #tk.Tk() creates the main application window.
    app = TodoApp(root)
    root.mainloop()

            