import json
from tkinter import messagebox


# function import datas (načtení databáze)
def import_db():
    with open('data.json', 'r') as file:
        return json.load(file)


# function save datas (uložení nové databáze)
def save_db(data):
    with open('data.json', 'w') as file:
        json.dump(data, file)


# create list (vytvoření listu podle klíče např. list názvů, list loginu atd.)
def list_cycle(data, key):
    list_passwords = []
    for i in range(0, len(data)):
        list_passwords.append(data[i][key])
    return list_passwords


# filter database by input (vyfiltruje novou databázi podle vstupu)
def filter_list(data, key):
    list_passwords = []
    for i in range(0, len(data)):
        for j in range(0, len(data[i]['alias'])):
            if key in data[i]['alias'][j]:
                list_passwords.append(data[i])
    return list_passwords


# choice datas (výběr z filtrované databáze a výpis dat)
def choice_password(data, names):
    global login
    global password
    global note
    global alias
    for i in range(0, len(data)):
        if data[i]['name'] == names:
            login = data[i]['name']
            password = data[i]['password']
            note = data[i]['note']
            alias = data[i]['alias']
    return [login, password, note, alias]


# find alias
def find_alias(new, data, key):
    new = list_cycle(filter_list(data, key), 'name')

# add new datas to database
def add_new_password(data, name, password, alias, note, win):
    new_password = {
        "alias": alias.strip("\n"),
        "name": name.strip("\n"),
        "password": password.strip("\n"),
        "note": note.strip("\n")
    }
    data.append(new_password)
    save_db(data)
    import_db()
    messagebox.showinfo("Úspěch", "Údaje byly uloženy!")
    win.destroy()

# update data (úprava údaju u hesla)
def update_data(selected_item, login, password, note, alias, win):
    with open('data.json', 'r') as file:
        data = json.load(file)
    for item in data:
        if item['name'] == selected_item[0]:
            item['login'] = login
            item['password'] = password
            item['note'] = note
            item['alias'] = alias
            break
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)
    messagebox.showinfo("Úspěch", "Údaje byly uloženy!")
    win.destroy()


# delete data (vymazání údaju u hesla)
def delete_data(selected_item, win):
    with open('data.json', 'r') as file:
        data = json.load(file)
    for item in data:
        if item['name'] == selected_item[0]:
            data.remove(item)
            break
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)
    messagebox.showinfo("Úspěch", "Údaje byly vymazány!")
    win.destroy()


# function search button
def action_with_arg(choice_list, data, input_box):
    choice_list['values'] = (list_cycle(filter_list(data, input_box.get()), 'name'))

# combobox search
def callback(self, choice_list):
    self.promena = choice_list.get()
    print(self.promena)



