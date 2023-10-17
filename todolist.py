from tkinter import *
def addTask():
    task=entry.get()
    if task:
        listbox.insert(END,task)
        entry.delete(0,END)
def deleteTask():
    selected_index = listbox.curselection()
    listbox.delete(selected_index)

window=Tk()
window.title("TO DO LIST")

listbox=Listbox(window)
listbox.pack()

entry=Entry(window,bg="black",fg="white")
entry.pack()

add_button = Button(window, text="Add Task", command=addTask)
add_button.pack()

delete_button = Button(window, text="Delete Task", command=deleteTask)
delete_button.pack()

window.mainloop()
