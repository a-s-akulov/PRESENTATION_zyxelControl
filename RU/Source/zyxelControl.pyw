from os import path, system
from tkinter import Tk, Entry, Label, Button, LEFT, TOP, BOTTOM

class zyxcelControl:
    
    def error_window(self, string):
        root = Tk()
        root.title("ERROR")
        root.resizable(width=False, height=False)
        Label(root, bg="red", text=string, anchor="nw", justify=LEFT, font=("Verdana", 15, "bold")).pack(side=TOP, padx=10, pady=10)
        Button(root, text="Ок", width=20, height=2, bd=4, font=("Verdana", 10, "bold"), command=root.destroy).pack(side=BOTTOM, padx=10, pady=10)
        self.root.tkraise()
        root.tkraise()
        root.mainloop()

    def keyPressed(self, event):
        if event.keysym == "Return":
            self.START()

    def START(self):
        host                        = self.root.hostEntry.get()
        log                         = self.root.logEntry.get()
        pas                         = self.root.passEntry.get()
        if ((host == '') or host.isspace()):
            self.error_window("IP-адрес/имя сервера не может быть пустым!")
            return
        if ((log == '') or log.isspace()):
            self.error_window("Имя пользователя не может быть пустым!")
            return
        if ((pas == '') or pas.isspace()):
            self.error_window("Пароль не может быть пустым!")
            return
        if not path.exists(r"bin\plink.exe"):
            self.error_window(r"Файл 'bin\plink.exe' не найден!\nУбедитесь в наличии файла в корневом каталоге.")
            return
        try:
            returned = system("start \"zyxelControl - akulov.a\" bin\plink.exe -ssh -pw {0} {1}@{2}".format(pas, log, host))
            if returned == 1:
                self.error_window("Не удалось выполнить 'start \"zyxelControl - akulov.a\" bin\plink.exe -ssh -pw {0} {1}@{2}'\nВозможно, у пользователя не достаточно прав для запуска 'bin\plink.exe',\nЛибо запускаемая программа находится на удаленном сервере".format(pas, log, host))
        except:
            self.error_window("Возникла неизвестная ошибка при запуске 'start \"zyxelControl - akulov.a\" bin\plink.exe -ssh -pw {0} {1}@{2}'\nВозможно, у пользователя не достаточно прав для запуска 'bin\plink.exe',\nЛибо запускаемая программа находится на удаленном сервере".format(pas, log, host))

    def main_window(self):

        root = Tk()
        self.root = root
        root.title("Соединиться по SSH")
        root.geometry("+40+40")
        root.resizable(width=False, height=False)
        root.bind("<Key>", self.keyPressed)            

        Label                           (root, text = "Сервер:", anchor="w", bg='#808080', font=("Verdana", 15, "bold")).grid(row=0, padx=10, pady=10, sticky="we")
        root.hostEntry                  = Entry(root, width = 20, bg='#008000', fg='#FFFFFF', highlightcolor="#000000", highlightbackground="#000000", font=("Verdana", 15, "bold"), highlightthickness=1)
        Label                           (root, text = "Имя пользователя:", anchor="w", bg='#808080', font=("Verdana", 15, "bold")).grid(row=2, padx=10, pady=10, sticky="we")
        root.logEntry                   = Entry(root, width = 20, bg='#008000', fg='#FFFFFF', highlightcolor="#000000", highlightbackground="#000000", font=("Verdana", 15, "bold"), highlightthickness=1)
        Label                           (root, text = "Пароль:", anchor="w", bg='#808080', font=("Verdana", 15, "bold")).grid(row=4, padx=10, pady=10, sticky="we")
        root.passEntry                   = Entry(root, width = 20, bg='#008000', fg='#FFFFFF', highlightcolor="#000000", highlightbackground="#000000", font=("Verdana", 15, "bold"), highlightthickness=1)

        Button                          (root, text = "Подключиться", height=1, bd=4, command = self.START, bg='#C0C0C0', font=("Verdana", 15, "bold")).grid(row=6, padx=10, pady=10)

        root.hostEntry.grid             (row=1, padx=10, pady=10)
        root.logEntry.grid              (row=3, padx=10, pady=10)
        root.passEntry.grid             (row=5, padx=10, pady=10)
        root.mainloop()



# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

if __name__ == '__main__':
    main = zyxcelControl()
    main.main_window()

















