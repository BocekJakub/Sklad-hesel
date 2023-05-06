from tkinter import *
from tkinter import ttk
from func import *

# window
window = Tk()
window.title("Sklad hesel")
window.minsize(400, 500)
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

data = import_db('data.json')

# input frame
title_label = Label(input_frame, text="", width=20, bg=main_color, font=main_font)
search_label = Label(input_frame, text="Hledat: ", width=20, bg=main_color, font=main_font)
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
login_label = Label(text_frame, text="Login: ", width=10, bg=main_color, font=main_font)
login_text = Text(text_frame, height=1, width=30,  borderwidth=2, font=main_font)
login_label.grid(row=0, column=0, padx=5, pady=5)
login_text.grid(row=0, column=1, padx=5, pady=5)

password_label = Label(text_frame, text="Password: ", width=10, bg=main_color, font=main_font)
password_text = Text(text_frame, height=1, width=30, borderwidth=2, font=main_font)
password_label.grid(row=1, column=0, padx=5, pady=5)
password_text.grid(row=1, column=1, padx=5, pady=5)

note_scrollbar = Scrollbar(text_frame)
note_scrollbar.grid(row=2, column=2, sticky=N+S)


note_label = Label(text_frame, text="Poznámka: ", width=10, bg=main_color, font=main_font)
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

# button frame
edit_button = Button(buttons_frame, text="Editovat", width=10, fg=front_color, font=main_font, bg=button_color)
close_button = Button(buttons_frame, text="Zavřít", width=10, fg=front_color, font=main_font , bg=button_color, command=window.destroy)
edit_button.grid(row=0, column=0, padx=20, pady=20)
close_button.grid(row=0, column=1, padx=20, pady=20)

#if not input_box.get():
#    source = list_cycle(filter_list(data, input_box.get()), 'name')
#    print(source) #nastavit event jako v javascript
#    choice_list = ttk.Combobox(input_frame, width=19, font=main_font, values=list_cycle(data, 'name'))

window.mainloop()
