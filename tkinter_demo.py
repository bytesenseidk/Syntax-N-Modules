
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import filedialog as fd

class Demo(object):
    def __init__(self, master):
        frame = Frame(master)
        frame.grid()
        tabControl = ttk.Notebook(root)
        tabControl.configure(width=400, height=300)

        self.option = StringVar()
        self.options = ["Option Menu", "Combo Box"]
        self.option.set(0)

        self.first_tab = ttk.Frame(tabControl)
        tabControl.add(self.first_tab, text="Tab 1")
        tabControl.grid()

        self.second_tab = ttk.Frame(tabControl)
        tabControl.add(self.second_tab, text="Tab 2")
        tabControl.grid()

        self.widgets()
    

    def widgets(self):
        label_frame = LabelFrame(self.first_tab, text="Label Frame", width=380, height=300)
        label_frame.grid(column=0, row=0)
        label_frame.grid_propagate(0)

        label = Label(label_frame, text="Label")
        label.grid(column=1, row=0)

        entry = Entry(label_frame, width=45)
        entry.grid(column=0, row=1, columnspan=3)
        entry.insert(0, "Entry field")

        radiobutton_1 = Radiobutton(label_frame, text="Radio 1", value=0)
        radiobutton_1.grid(column=0, row=2)
        radiobutton_2 = Radiobutton(label_frame, text="Radio 2", value=1)
        radiobutton_2.grid(column=1, row=2)
        checkbutton = Checkbutton(label_frame, text="Check")
        checkbutton.grid(column=2, row=2)

        button = Button(label_frame, text="Button")
        button.grid(column=0, row=3)

        menubutton = Menubutton(label_frame, text="Menu Button")
        menubutton.grid(column=1, row=3)
        menubutton.menu = Menu(menubutton, tearoff=0)
        menubutton["menu"] =  menubutton.menu
        menubutton.menu.add_checkbutton(label="first", variable=None)
        menubutton.menu.add_checkbutton(label="last", variable=None)

        scale = Scale(label_frame, from_=0, to=100, orient=HORIZONTAL)
        scale.grid(column=0, row=4)

        scrollbar = Scrollbar(label_frame)
        scrollbar.grid(column=2, row=4)

        list = Listbox(label_frame, yscrollcommand=scrollbar.set, height=5)
        for line in range(5):
            list.insert(END, "Listbox Element " + str(line))
        list.grid(column=2, row=4)
        scrollbar.config(command=list.yview)
        
        optionmenu = OptionMenu(label_frame, self.option, *self.options)
        optionmenu.grid(column=0, row=5)

        combobox = ttk.Combobox(label_frame, values=self.options)
        combobox.grid(column=1, row=5)
        combobox.current(0)

        progress = Progressbar(label_frame, orient=HORIZONTAL, length=100, mode='determinate')
        progress["value"] = 25
        progress.grid(column=2, row=5)

        treeview = ttk.Treeview(self.second_tab)
        treeview["columns"] = ("1","2","3")
        treeview.column("1", width=25)
        treeview.column("2", width=25)
        treeview.column("3", width=25)
        treeview.heading("1", text ="first") 
        treeview.heading("2", text ="second") 
        treeview.heading("3", text ="third")
        treeview.insert("", 'end', text ="Row 1", values=("Tree", "_", "View")) 
        treeview.insert("", 'end', text ="Row 2", values=("Tree", "_", "View")) 
        treeview.insert("", 'end', text ="Row 3", values=("Tree", "_", "View"))
        treeview.grid(column=0, row=0)
        treeview.grid_propagate(0)

if __name__ == '__main__':
    root = Tk()
    root.title("Tkinter Demo")
    Demo(root)
    root.mainloop()

    