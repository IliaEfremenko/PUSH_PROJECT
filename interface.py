import datetime
from tkinter import *
from tkinter import ttk

class User:
    _id = 0
    _login = ''
    _password = ''
    _name = ''
    _surname = ''
    _phone = ''
    _email = ''
    _birthdate = ''
    _status = 3

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if type(value) != int:
            raise TypeError()
        if value < 1:
            raise ValueError()
        self._id = value

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, log):
        if type(log) != str:
            raise TypeError()
        if log not in 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=_+?/><.,~`':
            raise ValueError()
        if len(log) < 8:
            raise TypeError()
        self._login = log

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if type(value) != str:
            raise TypeError()
        if value not in 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=_+?/><.,~`':
            raise ValueError()
        if len(value) < 8:
            raise TypeError()
        self._login = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        rus = 0
        eng = 0
        value = str(value)
        if not value[0].isupper():
            raise TypeError()
        for i in value:
            if i in '1234567890':
                raise TypeError()
            if i in 'абвгдежзийклмнопрстуфхцчшщьыъэюя':
                rus += 1
            if i in 'abcdefghijklmnopqrstuvwxyz':
                eng += 1
        if not (rus != 0 and eng == 0 or rus ==0 and eng != 0):
            raise TypeError()
        self._name = value

    @property
    def surname(self):
        return self._name

    @surname.setter
    def surname(self, value):
        rus = 0
        eng = 0
        value = str(value)
        if not value[0].isupper():
            raise TypeError()
        for i in value:
            if i in '1234567890':
                raise TypeError()
            if i in 'абвгдежзийклмнопрстуфхцчшщьыъэюя':
                rus += 1
            if i in 'abcdefghijklmnopqrstuvwxyz':
                eng += 1
        if not (rus != 0 and eng == 0 or rus == 0 and eng != 0):
            raise TypeError()
        self._surname = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if value is None:
            self._phone = None
            return
        value = str(value)
        for i in value:
            if i not in '1234567890':
                raise TypeError()
        self._phone = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if value is None:
            self._email = None
            return
        valid = 'abcdefghijklmnopqrstuvwxyz@_.'
        if type(value) != str:
            raise TypeError()
        if value.find('@', 1) == -1:
            raise TypeError()
        for i in value:
            if i not in valid:
                raise TypeError()
        self._email = value

    @property
    def birthdate(self):
        return self._birthdate

    @birthdate.setter
    def birthdate(self, value: str):
        if value is None:
            self._birthdate = None
            return
        if type(value) != str:
            raise TypeError()
        nums = list(map(int, value.split('-')))
        date = datetime.date(nums[0], nums[1], nums[2])
        if date > datetime.date.today():
            raise ValueError()
        self._birthdate = value

    @property
    def status(self):
        return self._name

    @status.setter
    def status(self, value: int):
        if type(value) != int:
            raise TypeError()
        if  value < 0:
            raise ValueError()
        self._status = value

    def __init__(self, user_id, login, password, name, surname, phone, email, birthdate, status):
        self.id = user_id
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.birthdate = birthdate
        self.status = status

    def __repr__(self):
        return f'{self._id}. {self._name}. {self._surname}'

class Adress:
    _id = 0
    _country = ''
    _city = ''
    _street = ''
    _house = ''
    _flat = ''
    _post_index = ''
    _commentary = ''


class Order:
    _id = 0
    _info = ''
    _description = ''
    _sender_id = 0
    _courier_id = 0
    _address_id = 0
    _status = 1

class Window(Tk):
    def __init__(self, add_user_func, load_users_func, get_statuses_dict_func):
        super().__init__()
        self.title('Post Service')
        self.geometry('+300+100')

        notebook = ttk.Notebook()
        notebook.pack(expand=True, fill=BOTH)
        frame1 = ttk.Frame(notebook)
        frame1.pack()
        notebook.add(frame1, text='Просмотр пользователей')

        frame2 = ttk.Frame()
        frame2.pack()
        notebook.add(frame2, text='Добавление пользователя')

        columns = ['id', 'login', 'password', 'name', 'surname', 'phone', 'email', 'birthdate', 'status']
        self.users_table = ttk.Treeview(columns=columns, show='heading', master=frame1)

        self.users_table.heading('id', text='ID')
        self.users_table.column('#1', stretch=NO, width=30)

        self.add_user_api_func = add_user_func
        self.load_users_api_func = load_users_func
        self.get_statuses_api_func = get_statuses_dict_func

        self.add_user_label = Label(text='Добавление пользователя', master=frame2)
        self.add_user_label.grid(row=0, column=0, columnspan=3, padx=3, pady=3)

        self.login_label = Label(text='Логин*:', master=frame2)
        self.login_label.grid(row=1, column=0, padx=3, pady=3)
        self.login_input = ttk.Entry()
        self.login_input.grid(row=1, column=1, padx=3, pady=3)
        self.login_error = Label()
        self.login_error.grid(row=1, column=2, padx=3, pady=3)
        self.login_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'[a-zA-Z0-9!@#$%^&*()=_+?/><.,~`-]{8,}', self.login_error,
                                         'Неверная длина или символы')), '%P'))

        self.password_label = Label(text="Пароль*:", master=frame2)
        self.password_label.grid(row=2, column=0, padx=3, pady=3)
        self.password_input = ttk.Entry()
        self.password_input.grid(row=2, column=1, padx=3, pady=3)
        self.password_error = Label()
        self.password_error.grid(row=2, column=2, padx=3, pady=3)
        self.login_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'[a-zA-Z0-9!@#$%^&*()=_+?/><.,~`-]{8,}', self.password_error,
                                         'Неверная длина или символы')), '%P'))

        self.name_label = Label(text="Имя*:", master=frame2)
        self.name_label.grid(row=3, column=0, padx=3, pady=3)
        self.name_input = ttk.Entry()
        self.name_input.grid(row=3, column=1, padx=3, pady=3)
        self.name_error = Label()
        self.name_error.grid(row=3, column=2, padx=3, pady=3)
        self.name_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^(?:[А-ЯЁ][а-яё]*|[A-Z][a-z]*)$', self.name_error,
                                         'Значение не является')), '%P'))

        self.surname_label = Label(text="Фамилия*:", master=frame2)
        self.surname_label.grid(row=4, column=0, padx=3, pady=3)
        self.surname_input = ttk.Entry()
        self.surname_input.grid(row=4, column=1, padx=3, pady=3)
        self.surname_error = Label()
        self.surname_error.grid(row=4, column=2, padx=3, pady=3)
        self.surname_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^(?:[А-ЯЁ][а-яё]*|[A-Z][a-z]*)$', self.surname_error,
                                         'Значение не является')), '%P'))

        self.phone_label = Label(text="Телефон:", master=frame2)
        self.phone_label.grid(row=5, column=0, padx=3, pady=3)
        self.phone_input = ttk.Entry()
        self.phone_input.grid(row=5, column=1, padx=3, pady=3)
        self.phone_error = Label()
        self.phone_error.grid(row=5, column=2, padx=3, pady=3)
        self.phone_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^(?:[8][0-9]{10}|[+][0-9]{10,})$', self.phone_error,
                                         'Значение не является')), '%P'))

        self.email_label = Label(text="Почта:", master=frame2)
        self.email_label.grid(row=6, column=0, padx=3, pady=3)
        self.email_input = ttk.Entry()
        self.email_input.grid(row=6, column=1, padx=3, pady=3)
        self.email_error = Label()
        self.email_error.grid(row=6, column=2, padx=3, pady=3)
        self.email_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^[a-zA-Z0-9!#$%^&*()=_+?/><,~`-]{1,}[@][a-zA-Z]{1,}[.][a-zA-Z]{2,3}$', self.email_error,
                                         'Значение не является')), '%P'))

        self.birthdate_label = Label(text="Дата рождения:", master=frame2)
        self.birthdate_label.grid(row=7, column=0, padx=3, pady=3)
        self.birthdate_input = ttk.Entry()
        self.birthdate_input.grid(row=7, column=1, padx=3, pady=3)
        self.birthdate_error = Label()
        self.birthdate_error.grid(row=7, column=2, padx=3, pady=3)
        self.birthdate_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'[1-2][0 - 9]{3}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2][0-9]|3[0-1])',
                                         self.birthdate_error,
                                         'Формат даты: ГГГГ-ММ-ДД')), '%P'))

        self.status_label = Label(text="Статус*:", master=frame2)
        self.birthdate_label.grid(row=8, column=0, padx=3, pady=3)
        self.statuses_list = list(self.get_statuses_api_func().keys())
        self.status_combobox = ttk.Combobox(values=self.statuses_list)
        self.status_combobox.grid(row=8, column=1, padx=3, pady=3)
        self.status_error = Label()
        self.status_error.grid(row=8, column=2, padx=3, pady=3)

        self.add_user_button = ttk.Button(text='Добавить пользователя', command=self.add_user, master=frame2)
        self.add_user_button.grid(row=9, column=1, padx=3, pady=3)

        self.users_list_variable = Variable()
        self.users_listbox = Listbox(listvarible=self.users_list_variable, master=frame1)
        self.users_listbox.grid(row=10, column=0, columnspan=3, padx=3, pady=3)

        self.load_users_button = ttk.Button(text='Обновить', command=self.load_users_list, master=frame1)
        self.load_users_button.grid(row=11, column=1, padx=3, pady=3)

        self.mainloop()

    def add_user(self):
        login = self.login_input.get()
        password = self.password_input.get()
        name = self.name_input.get()
        surname = self.surname_input.get()
        phone = self.phone_input.get() if self.self.phone_input.get() != '' else None
        email = self.email_input.get() if self.self.email_input.get() != '' else None
        birthdate = self.birthdate_input.get() if self.self.birthdate_input.get() != '' else None
        status = self.get_statuses_api_func().get(self.status_combobox.get())
        user = User(0, login, password, name, surname, phone, email, birthdate, status)
        self.add_user_api_func(user)


    def load_users_list(self):
        users = self.load_users_api_func()
        users_list = []
        for user in users:
            users_list.append(f'{user.id}. {user.login}, {user.password}, {user.name}, {user.surname}, {user.phone}, {user.email}, {user.birthdate}, {user.status}')
        self.users_list_variable.set(users_list)