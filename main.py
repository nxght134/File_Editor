from tkinter import *
import csv
from tkinter import messagebox


def all_children(window):
    _list = window.winfo_children()

    for item in _list:
        if item.winfo_children():
            _list.extend(item.winfo_children())

    return _list


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_menu()

    def create_menu(self):
        self.lbl = Label(self, text="Welcome", font="Arial 50")
        self.lbl.grid(columnspan=2)
        self.bttn_add = Button(self, text="Добавить новую запись в таблицу", font="Arial 20",
                               command=self.add_record)
        self.bttn_add.grid(row=1, column=0)
        self.bttn_show = Button(self, text="Просмотреть все записи в таблице", font="Arial 20",
                                command=self.show_records)
        self.bttn_show.grid(row=1, column=1)

    def file_open(self):
        file = open("database.csv", "a")
        file.write(
            self.write_login.get() + "," + self.write_name.get() + "," + self.password_write.get() + "," + self.write_birthday.get() + "," + self.write_city.get() + "\n")
        file.close()
        widget_list = all_children(self)
        for i in widget_list:
            i.destroy()
        messagebox.showinfo("Успешно", "Новая запись была добавлена в таблицу")
        self.create_menu()

    def add_record(self):
        self.lbl.destroy()
        self.bttn_add.destroy()
        self.bttn_show.destroy()
        self.text_login = Label(self, text='Введите e-mail:', font="Arial 20")
        self.text_login.grid(row=0, column=0, sticky=W)
        self.write_login = Entry(self, font="Arial 20")
        self.write_login.grid(row=0, column=1, sticky=W)
        self.text_name = Label(self, text="Введите имя:", font="Arial 20")
        self.text_name.grid(row=1, column=0, sticky=W)
        self.write_name = Entry(self, font="Arial 20")
        self.write_name.grid(row=1, column=1, sticky=W)
        self.password_text = Label(self, text='Введите пароль:', font="Arial 20")
        self.password_text.grid(row=2, column=0, sticky=W)
        self.password_write = Entry(self, font="Arial 20")
        self.password_write.grid(row=2, column=1, sticky=W)
        self.text_birthday = Label(self, text="Введите дату рождения(дд/мм/гг):", font="Arial 20")
        self.text_birthday.grid(row=3, column=0, sticky=W)
        self.write_birthday = Entry(self, font="Arial 20")
        self.write_birthday.grid(row=3, column=1, sticky=W)
        self.text_city = Label(self, text="Введите город:", font="Arial 20")
        self.text_city.grid(row=4, column=0, sticky=W)
        self.write_city = Entry(self, font="Arial 20")
        self.write_city.grid(row=4, column=1, sticky=W)
        self.bttn = Button(self, text="Зарегистрироваться", font="Arial 20", command=self.file_open)
        self.bttn.grid(row=5, column=0, columnspan=2)

    def show_records(self):
        widget_list = all_children(self)
        for i in widget_list:
            i.destroy()
        file = open("database.csv", "r")
        read = list(csv.reader(file))
        self.text_wind = Text(self, width=115, height=200, wrap=WORD)
        self.text_wind.grid(sticky=W)
        index = 0.0
        for row in read:
            new_record = "Логин: " + row[0] + ", имя: " + row[1] + ", дата рождения: " + row[3] + ", город: " + row[
                4] + "\n"
            self.text_wind.insert(index, new_record)
            index += 1.0
            print(index)
        file.close()

        self.bttn_return = Button(self, text="Вернуться в меню", command=self.create_menu)



root = Tk()
root.title("File Reader and Editor")
root.geometry('920x700')
app = Application(root)
root.mainloop()
