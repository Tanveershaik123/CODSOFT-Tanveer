import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql

def add_task():
    task_string = task_field.get()
    print(f"Task to add: {task_string}") 
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        tasks.append(task_string)
        the_cursor.execute('INSERT INTO tasks (title_text) VALUES (?)', (task_string,))
        the_connection.commit()  
        list_update()
        task_field.delete(0, 'end')

def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task) 

def delete_task():
    try:
        selected_index = task_listbox.curselection()
        if not selected_index:
            raise ValueError('No Task Selected.')
        
        the_value = task_listbox.get(selected_index)
        if the_value in tasks:
            tasks.remove(the_value)
            list_update()
            the_cursor.execute('DELETE FROM tasks WHERE title_text = ?', (the_value,))
            the_connection.commit()  
    except ValueError as ve:
        messagebox.showinfo('Error', str(ve))
    except Exception as e:
        messagebox.showinfo('Error', 'Failed to delete task: ' + str(e))

def delete_all_tasks():
    message_box = messagebox.askyesno('Delete All', 'Are you Sure?')
    if message_box:
        tasks.clear()  
        the_cursor.execute('DELETE FROM tasks')
        the_connection.commit()  
        list_update()

def clear_list():
    task_listbox.delete(0, 'end')

def close():
    print(tasks)
    the_connection.commit() 
    the_cursor.close()  
    the_connection.close() 
    guiwindow.destroy()

def retrieve_database():
    tasks.clear()  
    for row in the_cursor.execute('SELECT title_text FROM tasks'):
        tasks.append(row[0])

if __name__ == "__main__":
    guiwindow = tk.Tk()
    guiwindow.title("To-Do List Manager - Tanveer")
    guiwindow.geometry("500x450+750+250")
    guiwindow.resizable(0, 0)
    guiwindow.configure(bg="#FAEBD7")

    the_connection = sql.connect('listofTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT)') 

    tasks = []
    header_frame = tk.Frame(guiwindow, bg="dark blue")
    functions_frame = tk.Frame(guiwindow, bg="dark blue")
    listbox_frame = tk.Frame(guiwindow, bg="dark blue")

    header_frame.pack(fill="both")
    functions_frame.pack(side='left', expand=True, fill="both")
    listbox_frame.pack(side="right", expand=True, fill='both')
    
    header_label = ttk.Label(
        header_frame,
        text="To-Do List",
        font=("Alice", "30", "bold"),
        background="dark blue",
        foreground='#FFFFFF'
    )
    header_label.pack(padx=10, pady=10)

    task_label = ttk.Label(
        functions_frame,
        text="Enter the Task:",
        font=("Alice", "11", "bold"),
        background="dark blue",
        foreground="#FFFFFF"
    )
    task_label.place(x=30, y=40)

    task_field = ttk.Entry(
        functions_frame,
        font=("Consolas", "15"),
        width=18,
        background="dark blue",
        foreground="brown"
    )
    task_field.place(x=30, y=80)

    add_button = ttk.Button(
        functions_frame,
        text="Add Task",
        width=24,
        command=add_task
    )

    delete_button = ttk.Button(
        functions_frame,
        text="Delete Task",
        width=24,
        command=delete_task
    )
    
    exit_button = ttk.Button(
        functions_frame,
        text="Exit",
        width=24,
        command=close
    )
    
    add_button.place(x=30, y=120)
    delete_button.place(x=30, y=160)
    exit_button.place(x=30, y=200)

    task_listbox = tk.Listbox(
        listbox_frame,
        width=26,
        height=13,
        selectmode='SINGLE',
        background="#FFFFFF",
        foreground="#000000",
        selectbackground='#CD853F',
        selectforeground='#FFFFFF'
    )
    task_listbox.place(x=10, y=20)

    retrieve_database()
    list_update()
    guiwindow.mainloop()
