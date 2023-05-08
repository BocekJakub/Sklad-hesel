from tkinter import *
from tkinter import ttk
from func import *
#from edit_w import *

def create_main_window():
    # window
    main_window = Tk()
    main_window.title("Sklad hesel")
    main_window.minsize(400, 500)
    main_window.resizable(True, True)

    # fonts and colors
    main_font = ("Verdana", 12)
    main_color = "#e5eaf1"
    button_color = "#334560"
    front_color = "#f0f3f7"
    main_window.config(bg=main_color)

    # frames
    input_frame = Frame(main_window, bg=main_color)
    text_frame = Frame(main_window, bg=main_color)
    buttons_frame = Frame(main_window, bg=main_color)
    input_frame.pack()
    text_frame.pack()
    buttons_frame.pack()

    data = import_db()

    # input frame
    title_label = Label(input_frame, text="", width=20, bg=main_color, font=main_font, anchor=W)
    search_label = Label(input_frame, text="Hledat: ", width=20, bg=main_color, font=main_font, anchor=W)
    input_box = Entry(input_frame, width=15,  borderwidth=2, font=main_font)
    choice_list = ttk.Combobox(input_frame, width=22, font=main_font, values=list_cycle(data, 'name'))
    def action_with_arg():
        choice_list.set('')  # vymazání hodnoty comboboxu
        choice_list['values'] = (list_cycle(filter_list(data, input_box.get()), 'name'))
        input_box.delete(0, 'end')  # vymazání zadávacího pole
    def callback(self):
        global result
        self.choice = choice_list.get()
        result = choice_password(data, self.choice)
        write_result(result)

    ok_button = Button(input_frame, text='GO', command=action_with_arg)
    choice_list.bind("<<ComboboxSelected>>", callback)
    title_label.grid(row=0, column=0, padx=5, pady=5)
    search_label.grid(row=1, column=0, padx=5, pady=5)
    input_box.grid(row=2, column=1, padx=5, pady=5)
    choice_list.grid(row=2, column=0, padx=5, pady=5)
    ok_button.grid(row=2, column=2, padx=5, pady=5)

    # text frame
    login_label = Label(text_frame, text="Login: ", width=10, bg=main_color, font=main_font, anchor=W)
    login_text = Text(text_frame, height=1, width=30,  borderwidth=2, font=main_font)
    login_label.grid(row=0, column=0, padx=5, pady=5)
    login_text.grid(row=0, column=1, padx=5, pady=5)

    password_label = Label(text_frame, text="Password: ", width=10, bg=main_color, font=main_font, anchor=W)
    password_text = Text(text_frame, height=1, width=30, borderwidth=2, font=main_font)
    password_label.grid(row=1, column=0, padx=5, pady=5)
    password_text.grid(row=1, column=1, padx=5, pady=5)

    note_scrollbar = Scrollbar(text_frame)
    note_scrollbar.grid(row=2, column=2, sticky=N+S)


    note_label = Label(text_frame, text="Poznámka: ", width=10, bg=main_color, font=main_font, anchor=W)
    note_text = Text(text_frame,height=7, width=30, borderwidth=2, font=main_font, wrap=WORD, yscrollcommand=note_scrollbar.set)
    note_label.grid(row=2, column=0, padx=5, pady=5)
    note_text.grid(row=2, column=1, padx=5, pady=5)

    def write_result(result):
        login_text.delete(1.0,END)
        login_text.insert(END, result[0])
        password_text.delete(1.0,END)
        password_text.insert(END, result[1])
        note_text.delete(1.0,END)
        note_text.insert(END, result[2])

    def edit_window():
        edit_w()

    # button frame
    edit_button = Button(buttons_frame, text="Editovat", width=8, fg=front_color, font=main_font, bg=button_color, command=lambda: edit_w(main_window))
    close_button = Button(buttons_frame, text="Zavřít", width=8, fg=front_color, font=main_font , bg=button_color, command=main_window.destroy)
    edit_button.grid(row=0, column=0, padx=20, pady=20)
    close_button.grid(row=0, column=1, padx=20, pady=20)


    main_window.mainloop()
#####################################################

from tkinter import *
from tkinter import ttk
from func import *

def edit_w(main_window):

    window = Tk()
    window.title("Sklad hesel - editace")
    window.minsize(400, 550)
    window.resizable(True, True)

    # fonts and colors
    main_font = ("Verdana", 12)
    main_color = "#e5eaf1"
    button_color = "#334560"
    front_color = "#f0f3f7"
    window.config(bg=main_color)

    # frames
    input_frame = Frame(window, bg=main_color)
    text_frame = Frame(window, bg=main_color)
    buttons_frame = Frame(window, bg=main_color)
    input_frame.pack()
    text_frame.pack()
    buttons_frame.pack()

    data = import_db()

    # input frame
    title_label = Label(input_frame, text="Editace hesel", width=20, bg=main_color, font=main_font, anchor=W)
    search_label = Label(input_frame, text="Hledat: ", width=20, bg=main_color, font=main_font, anchor=W)
    input_box = Entry(input_frame, width=15, borderwidth=2, font=main_font)
    choice_list = ttk.Combobox(input_frame, width=22, font=main_font, values=list_cycle(data, 'name'))

    def action_with_arg():
        choice_list.set('')  # vymazání hodnoty comboboxu
        choice_list['values'] = (list_cycle(filter_list(data, input_box.get()), 'name'))
        input_box.delete(0, 'end')  # vymazání zadávacího pole

    def callback(self):
        global result
        self.choice = choice_list.get()
        result = choice_password(data, self.choice)
        write_result(result)
        print(result)



    ok_button = Button(input_frame, text='GO', command=action_with_arg)
    choice_list.bind("<<ComboboxSelected>>", callback)
    title_label.grid(row=0, column=0, padx=5, pady=5)
    search_label.grid(row=1, column=0, padx=5, pady=5)
    input_box.grid(row=2, column=1, padx=5, pady=5)
    choice_list.grid(row=2, column=0, padx=5, pady=5)
    ok_button.grid(row=2, column=2, padx=5, pady=5)

    # text frame
    login_label = Label(text_frame, text="Login: ", width=10, bg=main_color, font=main_font, anchor=W)
    login_text = Text(text_frame, height=1, width=30, borderwidth=2, font=main_font)
    login_label.grid(row=0, column=0, padx=5, pady=5)
    login_text.grid(row=0, column=1, padx=5, pady=5)

    password_label = Label(text_frame, text="Password: ", width=10, bg=main_color, font=main_font, anchor=W)
    password_text = Text(text_frame, height=1, width=30, borderwidth=2, font=main_font)
    password_label.grid(row=1, column=0, padx=5, pady=5)
    password_text.grid(row=1, column=1, padx=5, pady=5)

    note_scrollbar = Scrollbar(text_frame)
    note_scrollbar.grid(row=2, column=2, sticky=N + S)

    note_label = Label(text_frame, text="Poznámka: ", width=10, bg=main_color, font=main_font, anchor=W)
    note_text = Text(text_frame, height=7, width=30, borderwidth=2, font=main_font, wrap=WORD,
                     yscrollcommand=note_scrollbar.set)
    note_label.grid(row=2, column=0, padx=5, pady=5)
    note_text.grid(row=2, column=1, padx=5, pady=5)

    alias_label = Label(text_frame, text="Alias: ", width=10, bg=main_color, font=main_font, anchor=W)
    alias_text = Text(text_frame, height=7, width=30, borderwidth=2, font=main_font, wrap=WORD)
    alias_label.grid(row=3, column=0, padx=5, pady=5)
    alias_text.grid(row=3, column=1, padx=5, pady=5)



    def write_result(result):
        login_text.delete(1.0, END)
        login_text.insert(END, result[0])
        password_text.delete(1.0, END)
        password_text.insert(END, result[1])
        note_text.delete(1.0, END)
        note_text.insert(END, result[2])
        alias_text.delete(1.0, END)
        alias_text.insert(END, result[3])

    # button frame
    def close_window():
        window.destroy()
        main_window.destroy()
        create_main_window()


    save_button = Button(buttons_frame, text="Uložit", width=8, fg=front_color, font=main_font, bg=button_color, command=lambda: (update_data(result, login_text.get(1.0, END), password_text.get(1.0, END), note_text.get(1.0, END), alias_text.get(1.0, END), window), edit_w(main_window)))
    add_button = Button(buttons_frame, text="Přidat", width=8, fg=front_color, font=main_font, bg=button_color, command=lambda: (add_new_password(data, login_text.get(1.0, END), password_text.get(1.0, END), alias_text.get(1.0, END), note_text.get(1.0, END), window), edit_w(main_window)))
    delete_button = Button(buttons_frame, text="Vymazat", width=8, fg=front_color, font=main_font, bg=button_color, command=lambda: (delete_data(result, window), edit_w(main_window)))
    close_button = Button(buttons_frame, text="Zavřít", width=8, fg=front_color, font=main_font, bg=button_color, command=close_window)
    save_button.grid(row=0, column=0, padx=5, pady=20)
    add_button.grid(row=0, column=1, padx=5, pady=20)
    delete_button.grid(row=0, column=2, padx=5, pady=20)
    close_button.grid(row=0, column=3, padx=5, pady=20)

    #edit_w.protocol('WM_DELETE_WINDOW', close_window)
    #edit_w.mainloop()


create_main_window()
