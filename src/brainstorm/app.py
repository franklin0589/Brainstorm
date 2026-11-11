import sys
import os
import tkinter as tk
import tkinter.simpledialog as sdialog
import tkinter.filedialog as fdialog
import tkinter.font as font
class BrainStormApp:
    def __init__(self):
        self.root = tk.Tk()
        self.font = font.Font(family='Helvetica', name='appHighlightFont', size=12, weight='bold')
        self.ideas = []
        self.build_window()
        self.run()
    
    
    def submit(self):
        text = f"{len(self.ideas)+1}) {self.insert_text.get()}\n"
        self.insert_text.set("")
        self.display_text.insert(tk.END, text)
        self.ideas += [text]
    
    def new_file(self):
        cdir = os.getcwd()
        directory = fdialog.askdirectory(initialdir = cdir)
        if directory == "":
            return
        filename = sdialog.askstring("New File", "New File Name:")
        if filename is not None:
            self.ideas = []
            self.display_text.delete('1.0', END)
            self.file_path = f"{directory}/{filename}.txt"
            open(self.file_path, "x")

    def open_file(self):
        cdir = os.getcwd()
        file_path = fdialog.askopenfile(initialdir = cdir)
        if ".txt" in file_path.name: 
            self.file_path = file_path.name
            with open(self.file_path, "r") as f:
                self.ideas = f.readlines()
                for idea in self.ideas:
                    self.display_text.insert(tk.END, idea)
        else:
            print("Invalid File Type Selected")
        
    def save_file(self):
        cdir = os.getcwd()
        with fdialog.asksaveasfile(filetypes=[("Plain Text",".txt")]) as f:
            f.writelines(self.ideas)


    def submit_widget(self):
        submit_box = tk.Frame(self.frame, background="orange")
        submit_box.grid(column=0, row=2, sticky="nsew")
        submit_box.grid_rowconfigure(0, weight=1)
        submit_box.grid_columnconfigure(0, weight=9)
        submit_box.grid_columnconfigure(1, weight=1)
        
        self.insert_text = tk.StringVar()
        _entry = tk.Entry(submit_box,textvariable=self.insert_text)
        _entry.grid(row=0, column=0, sticky="ew")
        
        _button = tk.Button(submit_box, text="Submit", font=self.font, command = self.submit)
        _button.grid(row=0, column=1, sticky="e")
        
    def menu_widget(self):
        menu_box = tk.Frame(self.frame, background="grey")
        menu_box.grid(column=0, row=0, sticky="nsew")
        
        menu_box.grid_rowconfigure(0, weight=1)
        menu_box.grid_columnconfigure(0, weight=1)
        menu_box.grid_columnconfigure(1, weight=1)
        menu_box.grid_columnconfigure(2, weight=1)
        menu_box.grid_columnconfigure(3, weight=1)
        
        button_conf = {
            "background" : "lightgrey",
            "foreground" : "white"
            
        }
        
        _button1 = tk.Button(menu_box,button_conf, text = "New", relief="flat",font=self.font, command=self.new_file)
        _button2 = tk.Button(menu_box,button_conf, text = "Open",relief="flat",font=self.font, command=self.open_file)
        _button3 = tk.Button(menu_box,button_conf, text = "Save",relief="flat",font=self.font, command=self.save_file)
        _button4 = tk.Button(menu_box,button_conf, text = "X",   relief="flat",font=self.font, command=sys.exit)
        _button1.grid(row=0, column=0, sticky="nsew")
        _button2.grid(row=0, column=1, sticky="nsew")
        _button3.grid(row=0, column=2, sticky="nsew")
        _button4.grid(row=0, column=3, sticky="nsew")
    
        
    def display_widget(self):
        self.display = tk.Frame(self.frame)
        self.display.grid(column=0, row=1, sticky="nsew")
    
        v = tk.Scrollbar(self.display)
        v.pack(side = tk.RIGHT, fill = tk.Y)
         
        self.display_text = tk.Text(self.display, width = 15, height = 15, wrap = None, yscrollcommand = v.set)
 
        # insert some text into the text widget

        self.display_text.pack(side=tk.TOP, fill="both", expand=True)
        v.config(command=self.display_text.yview)
         

    def build_window(self):
        self.root.geometry("400x700+20+20")
        self.root.iconbitmap(r"C:\\Users\\Franklin\\Documents\\myCode\\myProjects\\Brainstorm\\data\\brain.ico")
        self.root.title("Brainstorm App")
        self.frame = tk.Frame(self.root, background="lightblue")
        self.frame.pack(expand=True, fill="both")
        
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=18)
        self.frame.grid_rowconfigure(2, weight=1)
        
        
        self.display_widget()
        self.submit_widget()
        self.menu_widget()
        
        
        
    def run(self):
        self.root.mainloop()
