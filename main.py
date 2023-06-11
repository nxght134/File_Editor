from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_menu()

    def create_menu(self):
        pass


root = Tk()
root.title("File Reader and Editor")
root.geometry('1000x700')
app = Application(root)
root.mainloop()
