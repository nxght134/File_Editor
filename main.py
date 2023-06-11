from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_menu()

    def create_menu(self):
        Label(self, text="Welcome", font="Arial 50").grid(columnspan=2)
        Button(self, text="Добавить новую запись в таблицу", font="Arial 20", command=self.add_record).grid(row=1,
                                                                                                            column=0)
        Button(self, text="Просмотреть все записи в таблице", font="Arial 20", command=self.show_records).grid(row=1,
                                                                                                               column=1)

    def add_record(self):
        pass

    def show_records(self):
        pass


root = Tk()
root.title("File Reader and Editor")
root.geometry('920x700')
app = Application(root)
root.mainloop()
