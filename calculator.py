import tkinter as tk

def press(key):
    current = str(entry.get())
    entry.delete(0,tk.END)
    entry.insert(0,current+key)

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0,"Error")

def clear():
    entry.delete(0,tk.END)

root = tk.Tk()
root.title("Calculator")
root.configure(bg="black")

entry= tk.Entry(root, width=24, font=('Arial', 28), borderwidth =2, relief ='solid',bg="white",fg='black')
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
buttons=[('7',1,0,'blue'),('8',1,1,'blue'),('9',1,2,'blue'),('/',1,3,"dark orange"),
         ('4',2,0,'blue'),('5',2,1,'blue'),('6',2,2,'blue'),('*',2,3,"dark orange"),
         ('1',3,0,'blue'),('2',3,1,'blue'),('3',3,2,'blue'),('-',3,3,"dark orange"),
         ('0',4,0,'blue'),('.',4,1,'blue'),('+',4,2,"dark orange"),('=',4,3,"green"),
         ('C',5,0,"red")]

for (text,row,col,color) in buttons:
    if text == '=':
        button=tk.Button(root,text=text,width=6,height=3,bg=color,fg='white',command=evaluate)
    elif text == 'C':
        button=tk.Button(root,text=text,width=6,height=3,bg=color,fg='white',command=clear)
    else:
        button=tk.Button(root,text=text,width=6,height=3,bg=color,fg='white',command=lambda t=text: press(t))
    button.grid(row=row,column=col,padx=5,pady=5)
root.mainloop()
