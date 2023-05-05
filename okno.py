from tkinter import *
from tkinter import ttk

# window
window = Tk()
window.title("Sklad hesel")
window.minsize(400, 500)
window.resizable(True, True)

# fonts and colors
main_font = ("Verdana", 12)
main_color = "grey"
button_color = "blue"
window.config(bg=main_color)

# frames
input_frame = Frame(window, bg=main_color)
text_frame = Frame(window, bg=button_color)
buttons_frame = Frame(window, bg=button_color)
input_frame.pack()
text_frame.pack()
buttons_frame.pack()

# input frame
title_label = Label(input_frame, text="", width=20, bg=main_color, borderwidth=0, font=main_font)
search_label = Label(input_frame, text="Hledat: ", width=20, bg=main_color, borderwidth=0, font=main_font)
input_box = Entry(input_frame, width=20, borderwidth=3, font=main_font)
choice_list = ttk.Combobox(input_frame, width=20, font=main_font)
title_label.grid(row=0, column=0, padx=5, pady=5)
search_label.grid(row=1, column=0, padx=5, pady=5)
input_box.grid(row=2, column=1, padx=5, pady=5)
choice_list.grid(row=2, column=0, padx=5, pady=5)

# text frame
login_label = Label(text_frame, text="Login: ", width=10, bg=main_color, font=main_font)
login_text = Listbox(text_frame, height=1, width=30, font=main_font)
login_text.insert(END, "položka seznamu")
login_label.grid(row=0, column=0)
login_text.grid(row=0, column=1)

password_label = Label(text_frame, text="Password: ", width=10, bg=main_color, font=main_font)
password_text = Listbox(text_frame, height=1, width=30, font=main_font)
password_text.insert(END, "položka")
password_label.grid(row=1, column=0)
password_text.grid(row=1, column=1)

note_label = Label(text_frame, text="Poznámka: ", width=10, bg=main_color, borderwidth=0, font=main_font)
note_text = Listbox(text_frame,height=4, width=30, font=main_font)
note_label.grid(row=2, column=0)
note_text.grid(row=2, column=1)

# button frame
edit_button = Button(buttons_frame, text="Editovat", width=10, font=main_font, bg=button_color)
close_button = Button(buttons_frame, text="Zavřít", width=10, font=main_font , bg=button_color, command=window.destroy)
edit_button.grid(row=0, column=0)
close_button.grid(row=0, column=1)


window.mainloop()